# Static Methods // Sınıfın kendisi ile ilgili olan ve sınıfın nesnesine ihtiyaç duymayan metotlardır
# Sınıfın kendisi ile ilgili işlemler için kullanılır

class MathOperations:

    @staticmethod # Static method olarak tanımlanır
    def add(x, y): 
        return x + y
    @staticmethod
    def subtract(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Division by zero is not allowed."
        return x / y
    
# Kullanım // Static methodlar sınıfın nesnesi olmadan çağrılabilir
print(MathOperations.add(5, 3))        # 8
print(MathOperations.subtract(10, 4))   # 6
print(MathOperations.multiply(2, 3))    # 6
print(MathOperations.divide(10, 2))     # 5.0
print(MathOperations.divide(10, 0))     # Division by zero is not allowed.