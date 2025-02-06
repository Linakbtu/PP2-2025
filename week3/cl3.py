class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    square = Square(4)
    print("Square area:", square.area())
    
    rectangle = Rectangle(4, 5)
    print("Rectangle area:", rectangle.area())
    
    shape = Shape()
    print("Shape area:", shape.area())
