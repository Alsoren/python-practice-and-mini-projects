# Erişim Belirleyicileri (Access Modifiers)
#Public, __Private, _Protected Methods
class Animal:
    def __init__(self, name, species): # Constructor Private method
        self.name = name  # Public attribute
        self._species = species  # Protected attribute
    
    def _make_sound(self): # Protected method
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed): # Constructor Private method
        super().__init__(name, "Dog")
        self.breed = breed  # Public attribute

    def display_info(self):  # Public method
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {self._species}")
    
    def make_sound(self):  # Public method
        return "Woof!"
    
dog = Dog("Buddy", "Golden Retriever")
dog.display_info()  # Access public and protected attributes
print(dog.make_sound())  # Access public method
print(dog._make_sound())  # This would be discouraged but still accessible