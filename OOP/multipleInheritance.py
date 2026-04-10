#Multiple Inheritance Example

class FlyingVehicle: #parent class
    def fly(self):
        print("This vehicle can fly!")

class WaterVehicle: #parent class
    def sail(self):
        print("This vehicle can sail!")

class AmphibiousVehicle(FlyingVehicle, WaterVehicle): #child derived from both parent classes
    def drive(self):
        print("This vehicle can drive on land!")

# Example usage
amphibious_vehicle = AmphibiousVehicle()
amphibious_vehicle.fly()
amphibious_vehicle.sail()
amphibious_vehicle.drive()