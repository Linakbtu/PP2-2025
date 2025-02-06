class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

if __name__ == "__main__":
    square = Square(4)
    print("Square area:", square.area())
    shape = Shape()
    print("Shape area:", shape.area())