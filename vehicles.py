class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        pass  # Base class method to be overridden
    
    def get_info(self):
        return f"{self.name} - Speed: {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self):
        return f"🚗 {self.name} is driving on the road at {self.speed} km/h using {self.fuel_type}"

class Plane(Vehicle):
    def __init__(self, name, speed, altitude):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):
        return f"✈️ {self.name} is flying at {self.speed} km/h at {self.altitude} meters"

class Boat(Vehicle):
    def __init__(self, name, speed, water_type):
        super().__init__(name, speed)
        self.water_type = water_type
    
    def move(self):
        return f"🚢 {self.name} is sailing on {self.water_type} at {self.speed} km/h"

class Bicycle(Vehicle):
    def __init__(self, name, speed, gear_count):
        super().__init__(name, speed)
        self.gear_count = gear_count
    
    def move(self):
        return f"🚲 {self.name} is cycling at {self.speed} km/h with {self.gear_count} gears"

# Example usage
if __name__ == "__main__":
    # Create different vehicles
    car = Car("Tesla Model 3", 120, "electric")
    plane = Plane("Boeing 747", 900, 10000)
    boat = Boat("Speedboat", 50, "sea")
    bicycle = Bicycle("Mountain Bike", 25, 21)
    
    # Demonstrate polymorphism
    vehicles = [car, plane, boat, bicycle]
    
    print("Vehicle Movement Demonstration:")
    print("=" * 50)
    for vehicle in vehicles:
        print(vehicle.move())
        print("-" * 50) 