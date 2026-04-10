# translate_subs.py
# İngilizce altyazıyı Türkçe'ye çevirir; zaman kodlarını ve numaraları korur.
# Gerekenler: openai (resmi SDK), python-dotenv (opsiyonel)
import os
import sys
import time
import re
from typing import List, Tuple
from dataclasses import dataclass

try:
    from openai import OpenAI  # resmi SDK
except ImportError:
    print("Hata: 'openai' paketi yüklü değil. `pip install openai` komutunu çalıştırın.")
    sys.exit(1)

# --------- Basit veri yapıları ---------
@dataclass
class Cue:
    idx: str          # '1', '2', ... (VTT'de boş olabilir)
    timing: str       # '00:00:01,000 --> 00:00:03,000' veya VTT formatı
    text_lines: List[str]  # bir ya da daha çok metin satırı

# --------- Yardımcılar ---------
SRT_SEP_RE = re.compile(r"\r?\n\r?\n")
TIMING_RE = re.compile(r"-->\s")  # SRT veya VTT zaman çizgisi python subtitle.py video.en.srt video_tr.srt

def detect_format(text: str) -> str:
    if text.lstrip().startswith("WEBVTT"):
        return "vtt"
    return "srt"

def parse_subs(text: str) -> List[Cue]:
    """Hem .srt hem basit .vtt için yeterli bir ayırıcı (güçlü kenar durumları hedeflenmemiştir)."""
    blocks = re.split(SRT_SEP_RE, text.strip(), flags=0)
    cues: List[Cue] = []
    for b in blocks:
        lines = b.splitlines()
        if not lines:
            continue
        # VTT'de ilk satır WEBVTT olabilir
        if lines[0].strip().upper().startswith("WEBVTT"):
            lines = lines[1:]
            if not lines:
                continue
        # SRT tipik: idx, timing, text...
        # VTT tipik: [optional idx or cue-id], timing, text...
        if len(lines) >= 2 and TIMING_RE.search(lines[1]):
            idx = lines[0].strip()
            timing = lines[1].strip()
            text_lines = [ln.rstrip() for ln in lines[2:]]
        else:
            # Bazı VTT'lerde cue-id yoktur: ilk zaman satırını bul
            timing_idx = None
            for i, ln in enumerate(lines):
                if TIMING_RE.search(ln):
                    timing_idx = i
                    break
            if timing_idx is None:
                # geçersiz blok – olduğu gibi yaz (atla)
                continue
            idx = "" if timing_idx == 0 else lines[0].strip()
            timing = lines[timing_idx].strip()
            text_lines = [ln.rstrip() for ln in lines[timing_idx + 1:]]
        cues.append(Cue(idx=idx, timing=timing, text_lines=text_lines))
    return cues

def serialize_subs(cues: List[Cue], fmt: str) -> str:
    parts = []
    if fmt == "vtt":
        parts.append("WEBVTT\n")
    for c in cues:
        if fmt == "srt":
            # SRT zorunlu numara
            parts.append(c.idx if c.idx else str(len(parts) + 1))
        else:
            # VTT'de cue-id opsiyonel
            if c.idx:
                parts.append(c.idx)
        parts.append(c.timing)
        parts.extend(c.text_lines if c.text_lines else [""])
        parts.append("")  # blok ayırıcı boş satır
    return "\n".join(parts).strip() + "\n"

def chunk_cues(cues: List[Cue], max_cues_per_batch: int = 40, max_chars: int = 8000):
    """Model giriş boyutunu aşmamak için toplu çevrim (batch)."""
    batch, char_count = [], 0
    for cue in cues:
        # tahmini boyut
        cue_text = "\n".join(cue.text_lines)
        est_len = len(cue_text) + len(cue.timing) + 16
        if batch and (len(batch) >= max_cues_per_batch or char_count + est_len > max_chars):
            yield batch
            batch, char_count = [], 0
        batch.append(cue)
        char_count += est_len
    if batch:
        yield batch

def build_prompt(batch: List[Cue], fmt: str) -> str:
    """Model için net ve katı talimat. Çıktıyı aynı altyazı biçiminde ister."""
    header = (
        "You are a professional subtitle translator. "
        "Translate ONLY the dialogue lines from English to Turkish.\n"
        "- KEEP the cue numbers (if present) and the timing line EXACTLY unchanged.\n"
        "- Preserve line breaks and italic/formatting tags like <i>...</i> or [Music].\n"
        "- Do NOT add extra commentary. Output must be valid {fmt_upper} blocks.\n"
    ).format(fmt_upper=fmt.upper())
    example = (
        "\nExample input cue:\n"
        "12\n"
        "00:00:01,000 --> 00:00:02,000\n"
        "I'm fine.\n\n"
        "Example output cue (only text translated):\n"
        "12\n"
        "00:00:01,000 --> 00:00:02,000\n"
        "İyiyim.\n"
        "----\n"
    )
    body_lines = []
    for c in batch:
        if fmt == "srt":
            body_lines.append(c.idx if c.idx else "0")
        else:
            if c.idx:
                body_lines.append(c.idx)
        body_lines.append(c.timing)
        body_lines.extend(c.text_lines if c.text_lines else [""])
        body_lines.append("")  # blok ayracı
    body = "\n".join(body_lines).strip()
    return header + example + "\nNow translate the following cues:\n\n" + body

# --------- OpenAI çağrısı ---------
def translate_text_with_openai(prompt: str, model: str = None, retry: int = 3) -> str:
    """
    OpenAI Responses API ile tek bir toplu çeviri isteği yapar ve düz metin döndürür.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY ortam değişkeni bulunamadı.")
    client = OpenAI()
    model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    last_err = None
    for attempt in range(1, retry + 1):
        try:
            # Güncel SDK: Responses API
            # Kaynak: resmi dökümantasyondaki responses.create kullanımı. 
            # print(response.output_text) ile nihai metni alır. 
            response = client.responses.create(
                model=model,
                input=prompt,
                # Güvenli ve kısıtlı çıktı için (yalın metin srt/vtt):
                max_output_tokens=2000,  # batch boyutuna göre ayarlayın
            )
            return response.output_text
        except Exception as e:
            last_err = e
            # basit geriye çekilme
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"OpenAI isteği başarısız: {last_err}")

def merge_batch_output(orig_batch: List[Cue], batch_out: str, fmt: str) -> List[Cue]:
    """
    Modelden dönen blokları tekrar Cue listesine çevirir.
    Varsayım: Model, girdideki blok biçimini aynen koruyup yalnız metinleri çevirdi.
    """
    out_cues = parse_subs(batch_out)
    # Eğer sayılar tutuyorsa doğrudan döndür.
    if len(out_cues) == len(orig_batch):
        return out_cues
    # Aksi durumda (seyrek) en güvenlisi: zaman çizgileri ile hizala
    aligned: List[Cue] = []
    out_map = {(c.timing, c.idx): c for c in out_cues}
    for oc in orig_batch:
        key = (oc.timing, oc.idx)
        if key in out_map:
            aligned.append(out_map[key])
        else:
            # eşleşme yoksa: orijinalin textini bırak (bozulmayı engelle)
            aligned.append(oc)
    return aligned

# --------- Ana akış ---------
def main():
    if len(sys.argv) < 3:
        print("Kullanım: python translate_subs.py input.srt output.tr.srt [MODEL_ADI]")
        sys.exit(1)
    inp, outp = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) >= 4 else os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    with open(inp, "r", encoding="utf-8-sig") as f:
        raw = f.read()

    fmt = detect_format(raw)
    cues = parse_subs(raw)
    if not cues:
        print("Uyarı: Geçerli altyazı bloğu bulunamadı.")
        sys.exit(2)

    translated: List[Cue] = []
    for batch in chunk_cues(cues):
        prompt = build_prompt(batch, fmt)
        out_text = translate_text_with_openai(prompt, model=model)
        out_cues = merge_batch_output(batch, out_text, fmt)
        translated.extend(out_cues)

    result = serialize_subs(translated, fmt)
    with open(outp, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✓ Bitti: {outp}")

if __name__ == "__main__":
    main()
