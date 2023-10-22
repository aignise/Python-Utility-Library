# Parent Vehicle class
class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model
  
  def info(self):
    return f"{self.make} {self.model}"

# Car class derived from Vehicle
class Car(Vehicle):
  def __init__(self, make, model, num_wheels=4):
    super().__init__(make, model)
    self.num_wheels = num_wheels

# Motorcycle class derived from Vehicle
class Motorcycle(Vehicle):
  def __init__(self, make, model, has_sidecart=False):
    super().__init__(make, model)
    self.has_sidecart = has_sidecart

# Factory class to return object instances
class VehicleFactory:

  @staticmethod
  def create_vehicle(vehicle_type, make, model, **kwargs):
    # Return instance based on vehicle type
    if vehicle_type == "car":
      return Car(make, model, **kwargs)
    elif vehicle_type == "motorcycle":
      return Motorcycle(make, model, **kwargs)
    else:
      raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Example usage:
car = VehicleFactory.create_vehicle("car", "Toyota", "Camry")
print(car.info())

bike = VehicleFactory.create_vehicle("motorcycle", "Harley", "Chopper", has_sidecart=True)
print(bike.info())