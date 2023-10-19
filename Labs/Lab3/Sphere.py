from Circle import *


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