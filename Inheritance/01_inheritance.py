class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass 

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Testing the classes
dog = Dog(species="Canine")
print(f"The {dog.species} says: {dog.make_sound()}")  # Output: The Canine says: Woof!

cat = Cat(species="Feline")
print(f"The {cat.species} says: {cat.make_sound()}")  # Output: The Feline says: Meow!

bird = Bird(species="Avian")
print(f"The {bird.species} says: {bird.make_sound()}")  # Output: The Avian says: Chirp!
