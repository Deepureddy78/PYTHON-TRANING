'''
7. Shape Hierarchy (Classes + Inheritance)
Task: Implement Shape → Circle, Rectangle.
Input:
circle = Circle(5)
rect = Rectangle(4, 6)
print(circle.area())
print(rect.area())
Expected Output:
78.54
24
'''

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def main():
    circle = Circle(5)
    rect = Rectangle(4, 6)
    
    print(circle.area())
    print(rect.area())

if __name__ == '__main__':
    main()
