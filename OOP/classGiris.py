class myClass:
    surname = "Doe" #property

    def __init__(self, name): #constructor // MAGIC method
        self.name = name #instance variable

    def __str__(self): #string representation //  MAGIC method
        return f"{self.name} {self.surname}"
    
    def __repr__(self): #representation // MAGIC method
        return f"{self.name!r} {self.surname!r}"

    def greet(self): #method
        print(f"Hello, {self.name} {self.surname}!")

p1 = myClass("Alice")
print(p1)  # Calls __str__ Kullanıcı dostu çıktı
print(repr(p1))  # Calls __repr__ Geliştirici dostu çıktı
p1.greet()