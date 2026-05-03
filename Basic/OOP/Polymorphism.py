class Shape:
    def area(self):
        pass



class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size**2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius**2

sq = Square(10)
print(sq.area())

cir = Circle(2)
print(cir.area())