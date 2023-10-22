# Subject interface
class NewsPublisher:

  def __init__(self):
    self.observers = []
  
  def subscribe(self, observer):
    # Add observer
    self.observers.append(observer)
  
  def unsubscribe(self, observer):
    # Remove observer 
    self.observers.remove(observer)
  
  def notify(self, news):
    # Notify all observers
    for observer in self.observers:
      observer.update(news)

# Observer interface
class NewsSubscriber:

  def __init__(self, name):
    self.name = name
  
  def update(self, news):
    print(f"{self.name} received {news}")

# Usage:
pub = NewsPublisher()

sub1 = NewsSubscriber("Alice")
sub2 = NewsSubscriber("Bob")

pub.subscribe(sub1)
pub.subscribe(sub2)

pub.notify("Hello World!")
# Alice received Hello World! 
# Bob received Hello World!

pub.unsubscribe(sub1)
pub.notify("Breaking News!") 
# Bob received Breaking News!