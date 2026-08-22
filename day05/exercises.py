from abc import ABC, abstractmethod
# Exercise 1:
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def describe(self):
        print(f"{self.make} {self.model}")
    @abstractmethod
    def wheels(self):
        """Return the number of wheels."""
        pass
class Car(Vehicle):
    def wheels(self):
        return 4

# Exercise 2 & 3
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)   
        self.capacity = capacity        
    def describe(self):               
        print(f"{self.make} {self.model}, capacity: {self.capacity} tons")
    def wheels(self):
        return 6

# Exercise 4: 
print("--- Vehicles ---")
vehicles = [
    Car("Toyota", "Camry"),
    Truck("Volvo", "FH16", 25),
    Car("Honda", "Civic"),
    Truck("Mercedes", "Actros", 30),
]
for v in vehicles:
    v.describe()  
# Exercise 5: 
print("\nWheel counts")
for v in vehicles:
    print(f"{v.make} {v.model}: {v.wheels()} wheels")