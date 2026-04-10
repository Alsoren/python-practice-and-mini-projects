# Python/bankaHesap.py
# Banka Hesap Programı  
class BankaHesap:
    def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if(miktar > 0):
            self.bakiye += miktar
            print(f"{miktar} TL başarıyla yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")

    def para_cek(self, miktar):
        if(miktar > 0 and miktar <= self.bakiye):
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Çekilecek miktar sıfırdan büyük olmalı ve bakiyenizden fazla olmamalıdır.")
    def bakiye_goruntule(self):
        print(f"Mevcut bakiye: {self.bakiye} TL")

def hesap_olustur():
    hesap_no = int(input("Hesap numaranızı giriniz: "))
    bakiye = float(input("Başlangıç bakiyenizi giriniz: "))
    return BankaHesap(hesap_no, bakiye)

# Ana program
geçerli_hesap = None
BankaHesap1 = BankaHesap(1232, 1000)
BankaHesap2 = BankaHesap(1233, 2000)
BankaHesap3 = BankaHesap(1234, 3000)
banka_hesaplar = [BankaHesap1, BankaHesap2, BankaHesap3]
# Kullanıcıdan hesap numarası al
print("Banka Hesap Programına Hoşgeldiniz")
choice = input("(1) Hesap numaranızı giriniz (2) Yeni hesap oluşturmak için 'Yeni' yazınız: ")

if choice == "yeni":
        new_hesap = hesap_olustur()
        banka_hesaplar.append(new_hesap)
        print(f"{new_hesap.hesap_no} numaralı hesap oluşturuldu. Başlangıç bakiyesi: {new_hesap.bakiye} TL")
        geçerli_hesap = new_hesap
elif choice == "1":
    hesap_no = int(input("Hesap numaranızı giriniz: "))
    for hesap in banka_hesaplar:
        if hesap.hesap_no == hesap_no:
            geçerli_hesap = hesap
            break
else:
    print("Hesap bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")
    exit()

while True:
    print("\n1. Para Yatır")
    print("2. Para Çek")
    print("3. Bakiye Görüntüle")
    print("4. Çıkış")

    secim = input("Lütfen bir işlem seçiniz: ")

    if secim == "1":
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
        geçerli_hesap.para_yatir(miktar)
    elif secim == "2":
        miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
        geçerli_hesap.para_cek(miktar)
    elif secim == "3":
        geçerli_hesap.bakiye_goruntule()
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")