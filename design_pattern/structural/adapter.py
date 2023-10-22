# The Adaptee contains the existing interface we want to adapt
class EuropeanSocketInterface:
  
  def voltage(self): 
    return 230 # Returns 230V 
    
  def live(self):
    return 1 # European live wire
    
  def neutral(self):
    return -1 # European neutral wire

# The Target defines the desired interface  
class USSocketInterface:
   
   def voltage(self):
     return 120 # US voltage
   
   def live(self):
     return 1 # US live wire
     
   def neutral(self):
     return 0 # US neutral 

# The Adapter makes the Adaptee's interface match Target    
class Adapter(USSocketInterface):
  
  # Constructor takes Adaptee object
  def __init__(self, socket):  
    self.socket = socket
  
  # Adapts the voltage
  def voltage(self):    
    return 110  
  
  # Returns Adaptee's live wire  
  def live(self):     
    return self.socket.live()
  
  # Returns Adaptee's neutral  
  def neutral(self):
    return self.socket.neutral()
          
# Client code uses Target interface through Adapter  
socket = EuropeanSocketInterface()
adapter = Adapter(socket) 

print(adapter.voltage()) # 110V
print(adapter.live()) # 1 
print(adapter.neutral()) # -1