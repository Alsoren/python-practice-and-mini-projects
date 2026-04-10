# File Handling Flush // Ara bellekte tutmadan veriyi anında diske yazmaya yarar
import time

with open("Files/flushMethod4.txt", "w", encoding="utf-8") as f:
    
    for i in range(7):
        f.write(f"Bu bir test yazısı {i + 1}\n")
        f.flush()  # Veriyi anında diske yaz
        time.sleep(0.1)  # 0.1 saniye bekle

        # Flush kullanılmadığı taktirde veriler ara bellekte kalır ve hepsi birden yazılırdı yalnız flush methodu sayesinde okunan veriler anında diske yazılır.