class Animal:
    def make_sound(self):
        print('Animal Can Make Sound')

class Cat(Animal):
    # using overide concept
    def make_sound(self):
        print('Meow Meow')

class Dog(Animal):
    pass


cat1 = Cat()
cat1.make_sound() # Meow Meow

dog1 = Dog()
dog1.make_sound() # Animal can make sound 



