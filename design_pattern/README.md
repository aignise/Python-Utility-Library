# Design Patterns Utility Library

The `design_patterns` directory is dedicated to the core design patterns used in object-oriented software development. These patterns offer repeatable solutions to commonly occurring software design problems. Understanding and implementing these patterns can lead to more modular, flexible, and maintainable code.

## Table of Contents

1. [Creational Patterns](#creational-patterns)
2. [Structural Patterns](#structural-patterns)
3. [Behavioral Patterns](#behavioral-patterns)

---

### Creational Patterns (`creational.py`)

Creational patterns deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

- **Singleton**: Ensures a class has only one instance and provides a global point to access it.
- **Factory**: Provides an interface for creating instances of a class, with its subclasses deciding which class to instantiate.
- **Builder**: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
- **Prototype**: Creates a fully initialized instance that can be cloned or copied to produce a different instance.

---

### Structural Patterns (`structural.py`)

Structural patterns concern class and object composition. They provide a manner to define relationships between classes or objects.

- **Adapter**: Allows classes with incompatible interfaces to work together by wrapping its own interface around that of an already existing class.
- **Bridge**: Decouples an abstraction from its implementation so that the two can vary independently.

---

### Behavioral Patterns (`behavioral.py`)

Behavioral patterns focus on communication between objects, how they operate, and assign responsibilities.

- **Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Strategy**: Defines a set of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.

---

The `design_patterns` library provides concrete implementations of these classic design patterns. Each pattern is implemented in a modular fashion, with detailed comments and explanations, allowing developers to grasp the underlying concepts and integrate the patterns seamlessly into their projects. Whether you're new to design patterns or need a quick refresher, this library serves as a valuable resource.