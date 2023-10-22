# The Abstraction defines the abstract interface
class Vehicle:

  # Accepts implementation object 
  def __init__(self, production):
    self.production = production

  # Delegates production to implementation  
  def manufacture(self):
    print(f"Manufacturing {self.production.get_vehicle()}")

# The Implementor defines the interface for implementation classes
class Production:
  
  def get_vehicle(self):
    pass

# Concrete Implementations
class CarProduction(Production):

  def get_vehicle(self):
    return "Car"

class MotorcycleProduction(Production):

  def get_vehicle(self):
    return "Motorcycle"

# Using the Abstraction and Implementations:

car = Vehicle(CarProduction())
car.manufacture() 

bike = Vehicle(MotorcycleProduction())
bike.manufacture()