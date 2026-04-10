# Class Methodu Amacı
#1-Sınıfın genel özelliklerini değiştirmek veya erişmek.
#2-Farklı bir şekilde nesne oluşturmak için "alternative constructor" olarak kullanmak.
#3-Tüm nesnelerden bağımsız, sınıf düzeyinde işlem yapmak.

class Employee:
    company_name = "TechCorp"  # Sınıf düzeyinde bir özellik

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name  # Sınıf düzeyindeki özelliği değiştirir

    @classmethod
    def get_value(cls, name, salary):
        return cls(name, int(salary))  # Alternatif constructor
    
    def display_info(cls):
        print(f"Name: {cls.name}, Salary: {cls.salary}, Company: {cls.company_name}")

# Kullanım
emp1 = Employee.get_value("Alice", 50000)