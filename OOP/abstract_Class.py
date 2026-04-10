from abc import ABC, abstractmethod

#Abstract Class
class Shape(ABC): #Abstract Class parent class // abstract classdan nesne türetilemez
    @abstractmethod #Her child class kendi area ve perimeter metodunu tanımlamak zorundadır aynı isimle
    def area (self):
        pass

    @abstractmethod
    def perimeter (self):
        pass # Abstract method, boş bırakılır, child classlarda implement edilmelidir

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height= height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

rect = Rectangle(5, 10)
print(f"Rectangle Area: {rect.area()}")  # Rectangle Area: 50
print(f"Rectangle Perimeter: {rect.perimeter()}")  # Rectangle Perimeter: 30
circle = Circle(7)
print(f"Circle Area: {circle.area()}")  # Circle Area: 153.86
print(f"Circle Perimeter: {circle.perimeter()}")  # Circle Perimeter: 43.96
