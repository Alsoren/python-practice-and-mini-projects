import os
from Phone_class import PhoneBook 

pb = PhoneBook()

while True:

    print("\nTelefon Rehberi")
    print("1. Kişi Ekle")
    print("2. Tüm Kişileri Göster")
    print("3. Kişi Sil")
    print("4. Kişi Ara")
    print("5. Çıkış")

    choice = input("Seçiminizi yapın (1-5): ")

    if choice == '1':
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        phone_number = input("Phone Number: ")
        pb.add_contact(first_name, last_name, phone_number)
    elif choice == '2':
        pb.show_contacts()
    elif choice == '3':
        phone_number = input("Silenecek kişinin telefon numarasını girin: ")
        pb.delete_contact(phone_number)
    elif choice == '4':
        phone_number = input("Aranacak kişinin numarası: ")
        pb.call_contact(phone_number)
    elif choice == '5':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-5 arasında bir değer girin.")
