# Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). Objects are instances of classes, which serve as blueprints for creating objects. OOP emphasizes the organization of code into manageable, reusable components.

## OOPs concepts in Python

1. Class
2. Object
3. Polymorphism
4. Encapsulation
5. Inheritance
6. Data Abstraction

## 1. Class

Classes are like a blueprints for creating objects. They define the properties(attributes) and behaviours (method) of objects. You can create class using the 'class' keyword followed by the class name.

### Syntax to create class

```python
class ClassName:
    #   Class variables(Properties or attributes)
    #   methods(function) go here

```

### Car Class Example

Below is an example of a `Car` class in Python:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

```

**Explanation**

You've defined a simple Python class named Car. This class represents a blueprint for creating car objects. Let's break down the components of this class:

**Constructor (**init**):** This method is called when a new instance of the Car class is created. It initializes the attributes of the object (make, model, and year) with the values passed as arguments.

**Attributes (make, model, and year):** These are properties of the Car class, representing the make, model, and year of the car, respectively.

**Method (display_info):** This method is defined to display information about the car object. It prints out the make, model, and year of the car using formatted strings.

### self

In Python, `self` represents the instance of the class being used. It allows access to attributes and methods of the class. Using `self` binds attributes with given arguments. Python doesn't use the `@` syntax for instance attributes, so `self` is necessary to refer to them. It's customary to use `self` as the first parameter in instance methods. When calling a method of an object, the object is automatically passed as the first argument using `self`. This enables modification of the object's properties and execution of tasks unique to that instance.

##2. Object

Object is an instance of a class. It is a real world entities. Everything in python is an object, including integers, strings, lists, function and classes themselves.
Object have attributes that represent their state and method that define their behaviour

### Creation of object

To create an object (instance) of the Car class provided earlier, you simply need to call the class name with the required arguments for the **init** method. Here's how you can do it:

```python
# Create an object (instance) of the Car class
car = Car("Toyota", "Camry", 2020)

# Access attributes and call methods of the car object
print(car.make)      # Output: Toyota
print(car.model)     # Output: Camry
print(car.year)      # Output: 2020
car.display_info()   # Output: Make: Toyota, Model: Camry, Year: 2020

```

## Full Code

```python

# Creating class of Car name
# with attribute make, model and year
# display_info(self) method to display information in terminal
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create an object (instance) of the Car class
car = Car("Toyota", "Camry", 2020)

# Access attributes and call methods of the car object
print(car.make)      # Output: Toyota
print(car.model)     # Output: Camry
print(car.year)      # Output: 2020
car.display_info()   # Output: Make: Toyota, Model: Camry, Year: 2020
```
