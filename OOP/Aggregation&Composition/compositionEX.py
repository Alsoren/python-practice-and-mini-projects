class Library:
    def __init__(self,name, books):
        self.name = name
        self.books = [Book(title, author) for title, author in books] # Composition // Book nesneleri doğrudan Library içinde oluşturulur
    def lists_books(self):
        print(f"Name of Library: {self.name}")
        for item in self.books:
            print(f"Title: {item.title} // Author: {item.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("City Library", [("Alice in Wonderland", "Lewis Carroll"), ("1984", "George Orwell")])
library.lists_books()  # Library classı içinde Book nesneleri tutulur ve yönetilir