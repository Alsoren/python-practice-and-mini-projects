class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def lists_books(self):
        print(f"Name of Library: {self.name}")
        for item in self.books:
            print(f"Title: {item.title} // Author: {item.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
book1 = Book("Alice in Wonderland", "Lewis Carroll")
book2 = Book("1984", "George Orwell")
library = Library("City Library")
library.add_book(book1)
library.add_book(book2)
library.lists_books()  # Library classı içinde Book nesneleri tutulur ve yönetilir