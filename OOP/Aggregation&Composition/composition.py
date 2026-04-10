# Composition // Bir classın nesnesini başka bir classın içinde doğrudan oluşturması durumudur
# Güçlü bir ilişki vardır, yani bir class diğerine bağımlıdır
# Eğer Department classı silinirse Employee classı kullanılamaz hale gelir

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Department:
    def __init__(self, dep_name, employees):
        self.dep_name = dep_name
        self.employees = [Employee(e[0], e[1]) for e in employees] # Composition // Employee nesneleri doğrudan Department içinde oluşturulur // List comprehension kullanıldı
    def display_employees(self):
        print(f"Department: {self.dep_name}")
        for emp in self.employees:
            print(f"Employee Name: {emp.name}, ID: {emp.emp_id}")


dept = Department("Software Eng", [("Turgut", 1001), ("Selin", 1002)]) # Department nesnesi oluşturulurken Employee nesneleri de oluşturulur
dept.display_employees()
