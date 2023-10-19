from Rectangle import *

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
