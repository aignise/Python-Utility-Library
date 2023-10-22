# The Singleton class will have only one instance across the entire program
class Singleton:

  # Class attribute to store the single instance
  __instance = None

  @staticmethod
  # Static method to retrieve the instance
  def get_instance():
    if Singleton.__instance == None:
      # Create the instance if it hasn't been created
      Singleton()
    return Singleton.__instance

  # Constructor is made private to prevent direct instantiation
  def __init__(self):
    if Singleton.__instance != None:
      # Raise error if trying to instantiate more than once
      raise Exception("Singleton can only be instantiated once")
    else:
      # Set the instance to the new object
      Singleton.__instance = self

# Usage:
s1 = Singleton.get_instance()
print(s1)
s2 = Singleton.get_instance() 
print(s2)
# s1 and s2 refer to the same instance