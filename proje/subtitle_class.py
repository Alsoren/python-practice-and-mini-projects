import re

class Subtitle:
    def __init__(self, time, title):
        """
        time: saniye cinsinden kaydırma miktarı (pozitif veya negatif)
        title: altyazı dosyası (.srt) adı veya yolu
        """
        self.time = float(time)
        self.title = title
        self.timestamp_re = re.compile(
            r'(?P<h>\d{1,2}):(?P<m>\d{2}):(?P<s>\d{2}),(?P<ms>\d{3})'
        )

    def read(self):
        """
        Dosyayı güvenli şekilde okur.
        UTF-8 değilse cp1254 (Türkçe Windows kodlaması) ile tekrar dener.
        """
        try:
            with open(self.title, "r", encoding="utf-8") as f:
                return f.readlines()
        except UnicodeDecodeError:
            with open(self.title, "r", encoding="cp1254") as f:
                return f.readlines()

    def _format_time(self, total_seconds):
        """
        Toplam saniyeyi SRT formatına (hh:mm:ss,mmm) dönüştürür.
        Negatif değerleri 00:00:00,000'a sabitler.
        """
        if total_seconds < 0:
            total_seconds = 0.0

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = total_seconds - hours * 3600 - minutes * 60
        seconds = round(seconds, 3)

        # saniye taşarsa (ör. 59.9995 → 60.000)
        if seconds >= 60:
            seconds -= 60
            minutes += 1
            if minutes >= 60:
                minutes -= 60
                hours += 1

        hh = f"{hours:02d}"
        mm = f"{minutes:02d}"
        ss_ms = f"{seconds:06.3f}".replace(".", ",")
        return f"{hh}:{mm}:{ss_ms}"

    def finding_timers(self):
        """
        Her zaman damgasını (timestamp) kaydırır.
        """
        lines = self.read()
        new_lines = []

        for line in lines:
            if "-->" in line:
                # her iki timestamp'i de bulur ve kaydırır
                def repl(match):
                    h = int(match.group("h"))
                    m = int(match.group("m"))
                    s = int(match.group("s"))
                    ms = int(match.group("ms"))
                    total = h * 3600 + m * 60 + s + ms / 1000.0
                    total += self.time
                    return self._format_time(total)

                new_line = self.timestamp_re.sub(repl, line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        return new_lines

    def fixing_text(self):
        """
        Kaydırılmış altyazıları dosyaya yazar.
        """
        new_texts = self.finding_timers()
        with open(self.title, "w", encoding="utf-8") as f:
            for line in new_texts:
                f.write(line)
