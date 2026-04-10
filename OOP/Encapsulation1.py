# Erişim Belirleyicileri (Access Modifiers)
#Public, __Private, _Protected Atributes

class Car:
    def __init__(self, marka, model):
        self.marka = marka  # Public attribute
        self._model = model  # Protected attribute
        self.__yil = 2020  # Private attribute
        self._ulke = "Türkiye"  # Protected attribute
    
    def display_info(self):
        print(f"Marka: {self.marka}, Model: {self._model}, Yıl: {self.__yil}")

class Tofas(Car):
    def __init__(self, marka, model): # Constructor
        super().__init__(marka, model)# Call the parent constructor
        self.__yil = 1980

    def display_info(self):
        print(f"Marka: {self.marka}, Model: {self._model}, Yıl: {self.__yil}, Ülke: {self._ulke}")

# Kullanım
araba = Car("Toyota", "Corolla")
araba.display_info()  # Erişim public ve protected özelliklere izin verir 
# print(araba.__yil)  # Bu satır hata verecektir çünkü __yil private bir özelliktir
sahin = Tofas("Tofas", "Sahin")
sahin.display_info()  # Erişim public ve protected özelliklere izin verir