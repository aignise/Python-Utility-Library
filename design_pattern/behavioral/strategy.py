# Strategy interface
class ShippingStrategy:
  def calculate(order):
    pass

# Concrete strategies
class RegularShipping(ShippingStrategy):
  
  def calculate(order):
    # Regular shipping calculation

class ExpressShipping(ShippingStrategy):

  def calculate(order):
    # Express shipping calculation
  
# Context class
class ShippingCalculator:

  def __init__(self, strategy):
    self.strategy = strategy
  
  def calculate(self, order):
    return self.strategy.calculate(order)

# Usage
calculator = ShippingCalculator(RegularShipping())
cost = calculator.calculate(order)

calculator.strategy = ExpressShipping()
cost = calculator.calculate(order)