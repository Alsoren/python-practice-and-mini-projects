# Aggregation (Toplulaştırma) // Bir clasın başka bir classın nesnesini içermesi durumudur
# Zayıf bir ilişki vardır, yani bir class diğerine bağımlı değildir 

class Employee:
    def __init__(self, name, emp_İd):
        self.name = name
        self.emp_id = emp_İd

class Department:
    def __init__(self, dep_name):
        self.dep_name = dep_name
        self.employees = [] #Aggregation 

    def atama(self, emp): # Method to add an employee to the department
        self.employees.append(emp)


emp1 = Employee("Turgut", 1001)
emp2 =Employee("Selin", 1002)

dept = Department("Software Eng")
dept.atama(emp1)
dept.atama(emp2)

for item in dept.employees:
    print(f"Employee Name:{item.name} İD:{item.emp_id}")