# Builder interface
class VehicleBuilder:
  def build_frame(self): pass
  def build_engine(self): pass
  def build_wheels(self): pass
  def build_doors(self): pass
  def get_vehicle(self): pass

# Car builder concrete class  
class CarBuilder(VehicleBuilder):

  def __init__(self):
    self.car = Car()

  def build_frame(self):
    # Car frame construction

  def build_engine(self):
    # Car engine construction  

  def build_wheels(self):
    # Car wheel construction

  def build_doors(self):
    # Car door construction

  def get_vehicle(self):
    return self.car

# Motorcycle builder concrete class
class MotorcycleBuilder(VehicleBuilder):
  
  # Motorcycle builder methods...

  def get_vehicle(self):
    return self.motorcycle

# Director class handles construction
class VehicleDirector:

  def __init__(self, builder):
    self.builder = builder

  def construct(self):
    self.builder.build_frame()
    self.builder.build_engine()
    self.builder.build_wheels()
    # etc...

  def get_vehicle(self):
    return self.builder.get_vehicle()

# Example usage:
car_builder = CarBuilder()
director = VehicleDirector(car_builder)
director.construct()
car = director.get_vehicle()

bike_builder = MotorcycleBuilder()
director = VehicleDirector(bike_builder)
director.construct()
motorcycle = director.get_vehicle()