from Shapes import Shapes

class Circle(Shapes):
    
    import math
    pi = math.pi

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.area = None
        self.circumference = None
  
    def is_unit_circle(self):

        unit_circle = self.x == 0 and self.y == 0 and self.radius == 1

        return unit_circle


    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius}, area={self._area}, circumference={self._circumference})"


    def __str__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius}, area={self._area}, circumference={self._circumference})"
