# Prototype base class
class VehiclePrototype:

  def clone(self):
    pass

# Concrete classes
class CarPrototype(VehiclePrototype):

  def __init__(self):
    # Initialize with default values
  def clone(self):
    # Return cloned instance with same values
    return CarPrototype() 

class MotorcyclePrototype(VehiclePrototype):
  
  # Motorcycle clone method

  def clone(self):
    # Return cloned instance
    return MotorcyclePrototype()    

# Example usage 
car = CarPrototype()
car_clone = car.clone()

motorcycle = MotorcyclePrototype()
motorcycle_clone = motorcycle.clone()