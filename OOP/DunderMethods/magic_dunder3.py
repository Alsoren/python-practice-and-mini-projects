class Person:
    def __init__ (self, name):
        self.name = name

    def __getattr__(self, attr): # Magic method to get an attribute
        return f"'{attr}' attribute is not defined in class"
     
    def __setattr__(self, attr, value): # Magic method to set an attribute
        if attr == "age" and value < 0:
            raise ValueError("Age cannot be negative")
        else :
            super ().__setattr__(attr, value) # ** Magic method to set an attribute

    def __delattr__(self, attr): # Magic method to delete an attribute
        if attr == "name":
            raise AttributeError("Cannot delete 'name' attribute")
        else:
            super().__delattr__(attr)

p1 = Person("Alice")
print(p1.name)  # Accessing an existing attribute
print(p1.age)   # Accessing a non-existing attribute, triggers __getattr__

p1.age = 30  # Setting an existing attribute
print(p1.age)  # Accessing the newly set attribute

del p1.age  # Deleting an existing attribute
print(p1.age)  # Accessing the deleted attribute, triggers __getattr__
