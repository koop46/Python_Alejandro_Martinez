from Rectangle import *
from Circle import *
from Sphere import *
from Cube import *


class Shapes:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):        

        if isinstance(self, Rectangle):
            area = self.side * self.side2
            self._area = area if area > 0 else 404

        elif isinstance(self, Circle):
            area = (self.pi * pow(self.radius, 2))
            self._area = area


    @property
    def circumference(self):
        return self._circumference


    @circumference.setter
    def circumference(self, circumference):
        
        if isinstance(self, Rectangle):
            circumference = 2 * (self.side + self.side2)
            self._circumference = circumference if self.side > 0 and self.side2 > 0 else 404


        elif isinstance(self, Circle):
            circumference =  (2 * self.pi * self.radius)
            self._circumference = circumference if circumference > 0 else 404


    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, volume):

        if isinstance(self, Cube):
    
            volume = pow(self.side,3)
            self._volume = volume

        elif isinstance(self, Sphere):

            volume = (4/3) * self.pi * pow(self.radius, 3)
            self._volume = volume if self.radius > 0 else 404

    def draw_figure(self):
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches

        fig, axes = plt.subplots()

        if isinstance(self, Circle):
            circle = plt.Circle( (self.x, self.y), self.radius, fill = False, color='blue' )

            axes.set_aspect( 1 )
            axes.add_artist( circle )

        elif isinstance(self, Rectangle):
            rectangle = patches.Rectangle((self.x - self.side2/2, self.y - self.side/2), self.side2, self.side, fill=False, color='blue')
            axes.add_patch(rectangle)

        plt.xlim( 0, 10 )
        plt.ylim( 0, 10 )

        plt.show()
        #ChatGPT automatic reponse när jag googlade "plot rectangle matplotlib"

    def is_inside_edge(self, x, y, z=None):

        figure_x = self.x
        figure_y = self.y
        side = self.side/2

        coord_y1 = figure_y - side
        coord_y2 = figure_y + side

        if z is not None: # z=0 tolkas som z=None
            figure_z = self.z

            coord_x1 = figure_x - side 
            coord_x2 = figure_x + side
            coord_z1 = figure_z - side 
            coord_z2 = figure_z + side 

            return coord_x1 < x < coord_x2 and coord_y1 < y < coord_y2 and coord_z1 < z < coord_z2

        else:

            side2 = self.side2/2 
    
            coord_x1 = figure_x - side2
            coord_x2 = figure_x + side2
            

            return coord_x1 < x < coord_x2 and coord_y1 < y < coord_y2

    def is_inside_curve(self, x, y, z=None):

        figure_x = self.x
        figure_y = self.y

        if z is not None:
            figure_z = self.z
            distance = ((x - figure_x) ** 2 + (y - figure_y) ** 2 + (z - figure_z) ** 2) ** 0.5

        else:
            distance = ((x - figure_x) ** 2 + (y - figure_y) ** 2) ** 0.5

        return distance < self.radius
    
    #Chat GPT query:
    # This is my code to check if a point (x,y) falls wihtin area of a rectangle
    # how can I rewrite the code to check if point falls within a circle? 
    # How would this function look to check if point falls within a sphere?

    def translate(self, x, y, z=None):
        try:
            x = float(x)
            y = float(y)
            z = float(z) if z is not None else None
            
        except ValueError:
            print("Sorry, you can only input numbers.")
        
        else:
            self.x = x
            self.y = y
            self.z = z if z is not None else None


    def __repr__(self):
        return f"Shapes(x={self.x}, y={self.y})"


    def __str__(self):
        return f"Shapes(x={self.x}, y={self.y})"


    def __eq__(self, obj):
        return self.area  == obj.area


    def __le__(self, object):
        if isinstance(self, Sphere) or isinstance(self, Cube):
            return self.volume <= object.volume
        else:
            return self.area <= object.area, self.circumference <= object.circumference        


    def __ge__(self, object):
        if isinstance(self, Sphere) or isinstance(self, Cube):
            return self.volume >= object.volume
        else:
            return self.area >= object.area, self.circumference >= object.circumference


    def __lt__(self, object):
        
        if isinstance(self, Sphere) or isinstance(self, Cube):
            return self.volume < object.volume
        else:
            return self.area < object.area, self.circumference < object.circumference


    def __gt__(self, object):
        if isinstance(self, Sphere) or isinstance(self, Cube):
            return self.volume > object.volume
        else:
            return self.area > object.area, self.circumference > object.circumference
