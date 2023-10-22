# Creational Design Patterns

Creational patterns provide object creation mechanisms that increase flexibility and reuse of existing code.

## Singleton

The Singleton pattern ensures only one instance of a class is created. This is useful when exactly one object is needed to coordinate actions across the system. 

**singleton.py** creates a Singleton class that prevents additional instantiations after the first instance is created. The static `get_instance()` method returns the singleton instance.

**Use cases:**

- Managing a shared resource that needs global access like a database object.
- Coordinating processes like logging.
- Managing application settings and configurations.

## Factory Method 

The Factory Method pattern defines an interface for creating objects, but lets subclasses decide which classes to instantiate. This allows deferring instantiation to subclasses.

**factory.py** creates a `VehicleFactory` class with a factory method that returns different vehicle subclasses based on input parameters. This decouples client code from the specific implementation classes.

**Use cases:**

- When the creation logic needs to be dynamically chosen based on configuration, environment, etc.
- To avoid tight coupling between the client code and concrete classes. 
- When you need to manage or manipulate the instantiated objects in subclasses.

## Builder

The Builder pattern constructs complex objects step-by-step. It allows producing different object representations using the same construction process.

**builder.py** has a `VehicleBuilder` abstract class for building vehicle objects part-by-part through its construction methods. The `VehicleDirector` uses the builder interface to construct a vehicle.

**Use cases:** 

- When object creation requires multiple steps or complex logic. 
- When you want to reuse the construction process but create different object representations.
- To encapsulate and abstract away complex construction details from the client code.

## Prototype

The Prototype pattern creates new objects by copying existing ones. It allows dynamically creating objects based on a template rather than recreating them from scratch.

**prototype.py** shows a `VehiclePrototype` base class with a `clone()` method to copy prototypes. Concrete prototypes like `CarPrototype` override this to clone themselves.

**Use cases**:

- When object creation is expensive, but new instances can be quickly cloned. This optimizes performance.
- Dynamically creating copies of existing parameterized objects at runtime.
- Reducing subclass proliferation when many variants of an object are required.