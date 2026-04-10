# Getter Setter and Deleter Methods

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property # Başta Property ataması yapılır getter'a
    def name(self):
        return self.__name

    @name.setter # Ardından getter methodla aynı isime sahip bir setter tanımlanır
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @name.deleter # Yine aynı isimle bir deleter tanımlanır
    def name(self):
        del self.__name
        print("Name deleted")

    @age.deleter
    def age(self):
        del self.__age
        print("Age deleted")

#Kullanım

person1 = Person("Alice", 30)
print(person1.name)  # Getter kullanımı
person1.name = "Bob"  # Setter kullanımı
print(person1.name)

del person1.name # Deleter kullanımı
