import os
import json

FILE_NAME =  "Json/JsonUygulama.json"

class Person:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open (FILE_NAME, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)
    
    def read_people(self):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_people(self, people):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(people, f, ensure_ascii=False, indent=4)

    def add_person(self):
        name = input("Name: ")
        age = int(input("Age: "))
        city = input("City: ")

        new_person = {"Name":name, "Age":age, "City":city}

        people = self.read_people()
        people.append(new_person)
        self.save_people(people)

        print(f"{name} has been added")

    def delete_person(self):
        name = input("Enter the name of the person to delete: ")
        people = self.read_people()
        updated_people = []

        for person in people:
            if person["Name"] != name:
                updated_people.append(person)

        if len(updated_people) == len(people):
            print(f"{name} not found!")

        else:
            self.save_people(updated_people)
            print(f"{name} has been deleted")

    def show_people(self):
        people = self.read_people()
        if not people:
            print("No people found!")
        else:
            for person in people:
                print(f"Name: {person['Name']}, Age: {person['Age']}, City: {person['City']}")


class App:
    def __init__(self):
        self.manager = Person()

    def run(self):
        while True:
            print("\n1- Add Person")
            print("2- Delete Person")
            print("3- Show People")
            print("4- Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.manager.add_person()
            elif choice == "2":
                self.manager.delete_person()
            elif choice == "3":
                self.manager.show_people()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = App()
    app.run()