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


##############################
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


##############################
class Cube(Rectangle):
    
    def __init__(self, x, y, z, side):
        super().__init__(x, y, side, 0) # 0:an ersätter side2 som ärvs från parentklassen

        self.z = z
        self.volume = None

    def draw_figure(self):
        import matplotlib.pyplot as plt

        center = (self.x, self.y, self.z)  
        half_side = self.side / 2

        vertices = [
            [center[0] - half_side, center[1] - half_side, center[2] - half_side],
            [center[0] + half_side, center[1] - half_side, center[2] - half_side],
            [center[0] + half_side, center[1] + half_side, center[2] - half_side],
            [center[0] - half_side, center[1] + half_side, center[2] - half_side],
            [center[0] - half_side, center[1] - half_side, center[2] + half_side],
            [center[0] + half_side, center[1] - half_side, center[2] + half_side],
            [center[0] + half_side, center[1] + half_side, center[2] + half_side],
            [center[0] - half_side, center[1] + half_side, center[2] + half_side]
        ]

        edges = [ [0, 1, 2, 3, 0], [4, 5, 6, 7, 4],
                [0, 4], [1, 5], [2, 6], [3, 7] ]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for edge in edges:
            ax.plot([vertices[i][0] for i in edge],
                    [vertices[i][1] for i in edge],
                    [vertices[i][2] for i in edge], 'blue')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)

        plt.show()
        #Chat GPT: 
        # "show me a code to plot a cube in matplotlib with side 2 and that takes x,y and z coordinates without changing any of the axes"


    def __repr__(self):
        return f"Cube(x={self.x}, y={self.y}, z={self.z}, side={self.side}, volume={self.volume})"


    def __str__(self):
        return f"Cube(x={self.x}, y={self.y}, z={self.z}, side={self.side}, volume={self.volume})"


##############################
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



class Sphere(Circle):

    def __init__(self, x, y, z, radius=None):
        super().__init__(x, y, radius)

        self.z = z
        self.volume = None


    def draw_figure(self):
        import matplotlib.pyplot as plt
        import numpy as np

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        radius = self.radius
        center_x, center_y, center_z = self.x, self.y, self.z

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = center_x + radius * np.outer(np.cos(u), np.sin(v))
        y = center_y + radius * np.outer(np.sin(u), np.sin(v))
        z = center_z + radius * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, color='b')

        ax.set_xlim([0, 7.5])  
        ax.set_ylim([0, 7.5])  
        ax.set_zlim([0, 7.5])  

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')

        ax.set_aspect('equal')

        plt.show()
        # https://www.tutorialspoint.com/plotting-points-on-the-surface-of-a-sphere-in-python-s-matplotlib


    def __repr__(self):
        return f"Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius}, volume={self.volume})"


    def __str__(self):
        return f"Sphere(x={self.x}, y={self.y}, z={self.z}, radius={self.radius}, volume={self.volume})"

#############################################

