# 4.Car Rental System:
#  Develop a class for managing car rentals with attributes like car type, rental duration, and rental cost. Implement methods for calculating rental charges and displaying rental details.


class CarRental:
    def __init__(self, car_type, rental_duration):
        self.car_type = car_type
        self.rental_duration = rental_duration
        self.rental_cost_per_day = self._rental_cost()

    def _rental_cost(self):
        if self.car_type == "normal":
            return 50
        elif self.car_type == "midsize":
            return 60
        elif self.car_type == "luxury":
            return 100
        else:
            return None

    def calculate_rental_cost(self):
        if self.car_type is None:
            return "Invalid car type"

        return self.rental_duration * self.rental_cost_per_day

    def displaying_rental_cardetails(self):
        print(f"Car Type: {self.car_type}")
        print(f"Rental Duration : {self.rental_duration}")
        print(f"Retal cost per day: {self.rental_cost_per_day}")
        print(f"Total Rental cost: {self.calculate_rental_cost()}")


maruti = CarRental(car_type="normal", rental_duration=2)
maruti.displaying_rental_cardetails()
