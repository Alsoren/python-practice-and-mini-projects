# Polimorfizm (Çok Biçimlilik)
# Her bir class kendi area metodunu tanımlayabilir
# ve bu metodlar aynı isimde olsa bile farklı davranışlar sergileyebilir
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
# Kullanım
shapes = [Circle(5), Triangle(4, 6), Rectangle(3, 4)]
for item in shapes:
    print(f"Area: {item.area()}")  # Polimorfizm sayesinde farklı şekillerin alanlarını hesaplayabiliriz