# Meta Programing

def newMethod(self):
    print("New method added")

class Person:
    pass

Person.newMethod = newMethod  # Dynamically adding a new method to the Person class
p1 = Person()
p1.newMethod()