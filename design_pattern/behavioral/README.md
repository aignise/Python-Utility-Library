# Behavioral Design Patterns

Behavioral patterns describe communication between objects and how responsibilities are distributed. They focus on simplifying communication while keeping components loosely coupled.

## Observer

The Observer pattern allows an object (subject) to publish updates to subscriber objects (observers) that are monitoring it.

**observer.py** defines a NewsPublisher subject that maintains a list of NewsSubscriber observers. The publisher notifies observers when news is available by calling their update() method.

**Uses:**

- Building event or notification systems that propagate new data to interested parties.
- Implementing subscription model where objects subscribe to updates from other objects.
- Replacing tight coupling between objects with a loosely coupled publish-subscribe model.

## Strategy

The Strategy pattern defines a family of interchangeable algorithms and allows switching between them dynamically.

**strategy.py** shows shipping strategies that encapsulate different shipping cost calculation algorithms. The ShippingCalculator context uses the strategy interface to delegate calculation to strategies interchangeably.

**Uses:**

- Implementing different variants of an algorithm within a system and making them interchangeable.
- Isolating implementation details behind a common interface to keep client code decoupled. 
- Ability to switch strategies at runtime based on application state or user input.

Behavioral patterns like Observer and Strategy promote flexibility in carrying out communication and distribution of responsibilities between objects. This makes it easy to extend systems by adding new behaviors without affecting existing code.