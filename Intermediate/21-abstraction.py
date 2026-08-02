#=======================
#   Abstraction
#=======================
 # Abstraction hides implementation details and exposes a simple interface.
 # Abstract classes define methods that subclasses must implement.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

vehicles = [Car(), Motorcycle()]
for vehicle in vehicles:
    vehicle.start_engine()
