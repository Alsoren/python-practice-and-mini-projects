# Nested (iç içe) classlar // Bir classın içinde başka bir classın tanımlanması durumudur
# Bu, genellikle bir classın başka bir classa ait olduğunu belirtmek için kullanılır

class Car:
    def __init__(self, marka, model, engine_hp, engine_type, engine_fuel):
        self.marka = marka
        self.model = model
        self.engine = Car.Engine(engine_hp, engine_type, engine_fuel)
    def show_details(self):
        print(f"Car: {self.marka} {self.model}")
        self.engine.show_engine()
    class Engine:
        def __init__(self, hp, type, fuel):
            self.hp = hp
            self.type = type
            self.fuel = fuel
        def show_engine(self):
            print(f"Engine Horse Power: {self.hp}\nEngine Type: {self.type}\nEngine Fuel: {self.fuel}")

c1 = Car("Toyota", "Corolla", 130, "V4", "Gasoline")
c1.show_details()  # Car classı içinde Engine classı kullanılır