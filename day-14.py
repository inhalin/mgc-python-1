import math

class Shape:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def getArea(self):
        area=self.width*self.height
        return area

    def description(self):
        return "This is a Shape."

class Rectangle(Shape):
    def description(self):
        return "This is a rectangle."

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def getArea(self):
        area=round(math.pi*(self.radius**2),4)
        return area

    def description(self):
        return "This is a circle."

shape=Shape(2,5)
print(shape.description())
print(f"The area of this shape is {shape.getArea()}.\n")

rectangle=Rectangle(3,4)
print(rectangle.description())
print(f"The area of this shape is {rectangle.getArea()}.\n")

circle=Circle(4)
print(circle.description())
print(f"The area of this shape is {circle.getArea()}.")