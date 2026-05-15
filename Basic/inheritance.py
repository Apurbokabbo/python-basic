# Parent class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        return f"Info: {self.brand} {self.model} {self.year}"


# Child class
class Car(Vehicle):
    def __init__(self, brand, model, year,seating):
        super().__init__(brand, model, year)
        self.seating = seating

    def display(self):
        return f" Car Info :{self.brand} {self.model} {self.year} {self.seating}"


# Object creation
c1 = Car("Toyota", "Corolla", 2022,5)

print(c1.display())