# In Python, the super() function is used to access methods and properties of a superclass within a subclass. Here's a simple example demonstrating inheritance with the super() function:
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} wags tail happily")


# Create an instance of the Dog class
my_dog = Dog("Buddy", "Woof", "Labrador")

# Accessing methods from superclass (Animal)
my_dog.make_sound()  # Output: Buddy says Woof

# Accessing method from subclass (Dog)
my_dog.wag_tail()  # Output: Buddy wags tail happily
