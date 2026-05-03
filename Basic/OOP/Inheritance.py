
# Parent Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        return f'Vehicle Information: {self.brand} {self.model} {self.year}'

#Child Class
class Car(Vehicle):
    def __init__(self, brand, model, year, seating_capacity):
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity

    def display(self):
        return  f'Car Information: {self.brand} {self.model} {self.year}, seating capacity: {self.seating_capacity}'

my_car = Car('BMW', 1999, 19, 3)
print(my_car.display())