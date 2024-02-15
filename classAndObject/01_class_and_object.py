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
