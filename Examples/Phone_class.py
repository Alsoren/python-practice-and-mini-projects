import os
import datetime
class PhoneBook:

    FILE_NAME = "phonebook.txt"
    
    def __init__(self):
        self.FILE_NAME = os.path.join(os.path.dirname(__file__), "phonebook.txt")

        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", encoding="utf-8") as f:
                pass

    def add_contact(self, first_name, last_name, phone_number):
        if len(phone_number) == 11 and phone_number.isdigit():
            with open(self.FILE_NAME, "r", encoding="utf-8") as f:
                contacts = f.readlines()
            for contact in contacts:
                if phone_number == contact.strip().split(","):
                    print("Bu telefon numarası zaten kayıtlı.")
                    return
            
            with open(self.FILE_NAME, "a", encoding="utf-8") as f:
                f.write(f"{first_name},{last_name},{phone_number}\n")
            print(f"{first_name} {last_name} kişisi eklendi.")
        else:
            print("Geçersiz telefon numarası.")

    def show_contacts(self):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            contacts = f.readlines()

        if not contacts:
            print("\nTelefon rehberi boş.")
            return
        else:
            print("\nTelefon Rehberi:")

            for contact in contacts:
                first_name, last_name, phone_number = contact.strip().split(",")
                #strip metindeki " " \n \t gibi karakterleri temizler
                #split metindeki virgüllere göre verileri ayırır
                print(f"{first_name} {last_name} - {phone_number}")

    def delete_contact(self, number):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            contacts = f.readlines()
        contact_found = False

        with open(self.FILE_NAME, "w", encoding="utf-8") as f:
            for contact in contacts:
                first_name, last_name, phone_number = contact.strip().split(",")
                if number == phone_number:
                    contact_found = True
                    deleted_contact = (first_name, last_name)
                else:
                    f.write(contact)

        if contact_found:
            print(f"{deleted_contact[0]} {deleted_contact[1]} kişisi silindi.")
        else:
            print("Kişi bulunamadı.")
    
    def call_contact(self, number):
        with open(self.FILE_NAME, "r", encoding="utf-8") as f:
            contacts = f.readlines()
        
        for contact in contacts:
            first_name, last_name, phone_number = contact.strip().split(",")
            if number == phone_number:
                print(f"{first_name} {last_name} aranıyor...")
                return
            
        print("Kişi bulunamadı.")