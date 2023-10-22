# Structural Design Patterns

Structural patterns describe how classes and objects can be combined to form larger structures. They focus on simplifying interfaces and the relationships between components.

## Adapter

The Adapter pattern converts one interface into another so that incompatible classes can work together. It wraps an existing class with a new interface.

**adapter.py** defines a Target US socket interface. The Adapter takes a European socket and adapts its interface to match the target interface expected by client code. This allows incompatible power systems to work together through the adapter.

**Uses:**

- Making existing classes with incompatible interfaces work together.
- Allowing APIs designed for different purposes to communicate through an adapter layer.
- Simplifying and normalizing different interface structures into one common API.

## Bridge 

The Bridge pattern separates an abstraction from its implementation so they can vary independently. 

**bridge.py** has an Abstraction (Vehicle) that defines the interface. The Implementor (Production) defines the implementation interface. Concrete implementations (CarProduction, MotorcycleProduction) implement the production classes.

This allows decoupling the abstraction from specific implementations.

**Uses:**

- Avoiding a highly coupled abstraction and implementation.
- Improving extensibility by separating the abstraction code from implementation details.
- Allowing the implementation to evolve independently from the abstraction interface.
- Switching implementations at runtime if business rules change.

Structural patterns like Adapter and Bridge are useful when you need to use incompatible pre-existing systems together or want to change implementations transparently. They help make components more reusable, maintainable and extensible.