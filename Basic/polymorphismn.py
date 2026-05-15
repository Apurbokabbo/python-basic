class Shape:
     def area(self):
         pass

class Square(Shape):
     def __init__(self,size):
         self.size = size

     def area(self):
         return self.size * self.size


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.1416* self.radius **2


sq=Square(5)
print(sq.area())

circle=Circle(10)
print(circle.area())

rec=Rectangle(10,20)
print(rec.area())


