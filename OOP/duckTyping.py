#Duck Typing Example
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
# In this example, both Dog and Cat classes have a speak method.
# The animal_sound function can accept any object that has a speak method, demonstrating duck typing.