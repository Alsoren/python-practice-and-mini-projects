# OOP/Inheritance.py
class Person: # Base class
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
    def myPrint(self):
        print(f"{self.firstname} {self.surname}")

class Student(Person): # Derived class
    def __init__(self, firstname, surname, student_id): # Constructor 
        super().__init__(firstname, surname) # Call the constructor of the base class
        self.student_id = student_id

    def myPrint(self): # Override the method from the base class // Method ezme 
        super().myPrint()
        print(f"Student ID: {self.student_id}")

class Teacher(Person): # Another derived class
    def __init__(self, firstname, surname, subject):
        super().__init__(firstname, surname)
        self.subject = subject

    def myPrint(self):
        super().myPrint()
        print(f"Subject: {self.subject}")

# Example usage
student = Student("John", "Doe", "S12345")
teacher = Teacher("Jane", "Smith", "Mathematics")

student.myPrint()
teacher.myPrint()