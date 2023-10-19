from Shapes import Shapes

class Rectangle(Shapes):

    def __init__(self, x, y, side=None, side2=None):
        super().__init__(x, y)

        self.side = side
        self.side2 = side2
        self.area = None
        self.circumference = None
    

    def is_square(self):
        return self.side==self.side2


    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, side={self.side}, side2={self.side2}, area={self.area}, circumference={self.circumference})"


    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, side={self.side}, side2={self.side2}, area={self.area}, circumference={self.circumference})"
