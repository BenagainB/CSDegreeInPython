# Programming Principles II

[<< Go back up a level](/Year_One/Year_One.md)

## Section Description

This course continues coverage of concepts introduced in Programming Principles I. Topics include composition, recursion, data abstraction, polymorphism, inheritance, interfaces, inner classes, abstract classes, object cloning, array lists, linked lists and exception handling. Programming projects are required.

## Prerequisites

Programming Principles I and a fair understanding of basic Algebra

## Suggested book

> *Starting Out with Python* (4th Edition) by Tony Gaddis • ISBN-10:0134444329 • ISBN-13:9780134444321

## Topics Covered 

*   Review:  
    *	Classes, methods, and references
    *	Interfaces
*   Compostion:
    *	Has-a relationship, 
    *	References to other classes
    *	Encapsulation vs alias
*   ArrayLists:
    *	Abstract Data Type
    *	ArrayList class
*   Inheritance:
    *	Inheritance
        *	Sub classes
        *	Method override
        *	Polymorphism
        *	Class hierarchies
    *	Object as base of all classes
    *	Protected visibility vs. private visibility
    *	Calling base class constructor
    *	Calling base class methods via super
    *	Abstract base class
    *	Interfaces
*   Exceptions: 
    *	Basic exception handling hierarchy
    *	Checked vs unchecked
    *	Handled versus unhandled exceptions
    *	Try/catch 
    *	Creating own exception class
*   Recursion: 
    *	Recursion in math
    *	Recursion vs. iteration
    *	Cost/benefit analysis
    *	Base and recursive cases
    *	Stack frames
    *	Algorithms that utilize recursion 
*   Linked Lists: 
    *	List as an ADT 
    *	Node class
    *	Basic list operations
    *	Basic linked list class
    *	Linked lists versus array 
    *	Searching and sorting
*   Java API tools: 
    *	Container classes
    *	Collection classes


## Key Concepts:

### Code Smells: (Kent Beck)
1.  A smell by definition is something that catches your attention
2.  Smells indicate a potential problem
3.  Smells are not inherently bad on their own, but they are an indicator of a problem

### WET/DRY
*   Write Every Time / Write Everything Twice
*   Don't Repeat Yourself

|SOLID Principles||
|:---|:---|
|Single-responsibility principle|"There should never be more than one reason for a class to change." In other words, every class should have only one responsibility.|
|Open-closed principle|"Software entities ... should be open for extension, but closed for modification."|
|Liskov substitution principle|"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."|
|Interface segregation principle|"Many client-specific interfaces are better than one general-purpose interface."|
|Dependency inversion principle|"Depend upon abstractions, **not** concretions."|


|Four Pillars of Object-Oriented Programming||
|:---|:---|
|Abstraction | Finding things that are similar in your code and providing a generic function or object to serve multiple places/with multiple concerns.|
|Encapsulation | Binding your data to something, whether it's a class, object, module or function, and doing your best to keep it as private as you reasonably can.|
|Inheritance | Inheritance chain is the term used to describe the flow of inheritance from the base object's prototype (the one that everything else inherits from) to the "end" of the inheritance chain (the last type that is inheriting).|
|Polymorphism | The real power of polymorphism is sharing behaviors, and allowing custom overrides.|

### Original Design Patterns

#### **Creational**
>Creational patterns are ones that create objects, rather than having to instantiate objects directly. This gives the program more flexibility in deciding which objects need to be created for a given case.
*   Creational:
*   Abstract Factory (object)
*   Builder (object)
*   Prototype (object)
*   Singleton (object)
*   Factory Method (class)

#### **Structural**
> These concern class and object composition. They use inheritance to compose interfaces and define ways to compose objects to obtain new functionality.
*   Adapter (object)
*   Bridge (object)
*   Composite (object)
*   Decorator (object)
*   Facade (object)
*   Flyweight (object)
*   Proxy (object)
*   Adapter (class)

#### **Behavioral**
> Most of these design patterns are specifically concerned with communication between objects.
*   Chain of Responsibility (object)
*   Command (object)
*   Iterator (object)
*   Mediator (object)
*   Memento (object)
*   Observer (object)
*   State (object)
*   Strategy (object)
*   Visitor (object)
*   Interpreter (class)
*   Template Method (class)

## Learning Outcomes 

*   insert and/or remove a node from a singly-linked list
*   write, compile and execute a complete program that will simulate a “has-a” relationship
*   design a program implementing inheritance and polymorphism
*   understand and implement a program that uses recursion to solve a problem
*   understand exception processing/handling

### **Special Notes on Singleton and Factory Patterns**

#### Singleton
The singleton design pattern solves problems by allowing it to:
*   Ensure that a class only has one instance
*   Easily access the sole instance of a class
*   Control its instantiation
*   Restrict the number of instances
*   Access a global variable

The singleton design pattern describes how to solve such problems:
*   Hide the constructors of the class.
*   Define a public static operation (getInstance()) that returns the sole instance of the class.

In essence, the singleton pattern forces it to be responsible for ensuring that it is only instantiated once. A hidden constructor—declared private or protected—ensures that the class can never be instantiated from outside the class. The public static operation can be accessed by using the class name and operation name, e.g., Singleton.getInstance()

Singleton DOES NOT return a new instance every time.

#### Factory
Factories determine the actual concrete type of object to be created, and it is here that the object is actually created. As the factory only returns an abstract interface to the object, the client code does not know – and is not burdened by – the actual concrete type of the object which was just created. However, the type of a concrete object is known by the abstract factory. 

In particular, this means:
*   The client code has no knowledge whatsoever of the concrete type, not needing to include any header files or class declarations relating to the concrete type. The client code deals only with the abstract type. Objects of a concrete type are indeed created by the factory, but the client code accesses such objects only through their abstract interface.
*   Adding new concrete types is done by modifying the client code to use a different factory, a modification which is typically one line in one file. This is significantly easier than modifying the client code to instantiate a new type, which would require changing every location in the code where a new object is created.

Factories can be used when:
*   The creation of an object makes reuse impossible without significant duplication of code.
*   The creation of an object requires access to information or resources that should not be contained within the composing class.
*   The lifetime management of the generated objects must be centralized to ensure a consistent behavior within the application.

Factory method DOES return a new instance every time.

Abstract factory DOES NOT rely on inheritance over composition.

Factory method DOES rely on inheritance over composition.

Factory method DOES allow for multiple methods to create an object.

Abstract Factory DOES use composition over instead of inheritance.

Simple Factory DOES NOT have multiple methods to create objects.

Factory methods to create objects ARE static.

Singleton and Factory are both creational patterns.

If you are not careful with factory/abstract factory your code can violate dependency inversion.

## Assignments


