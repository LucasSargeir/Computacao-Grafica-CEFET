from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *



class Sphere:

    half_pi = pi/2

    def __init__(self, x, y, z, radius, angle = 0, angle_speed = 0,color = (0,0,0), density = 50):
        self.position = (x, y, z)
        self.radius = radius
        self.angle = angle
        self.angle_speed = angle_speed
        self.color =  color
        self.density = density + x

    def draw(self, rotation = (1,1,1)):
        self._draw_filled_sphere(rotation)
        
    def rotate(self, times = 1):
        self.angle += self.angle_speed * times

    def move(self, x, y, z):
        self.position = (self.position[0] + x, self.position[1] + y, self.position[2] + z)

    def move_to(self, x, y, z):
        self.position = (x, y, z)

    def orbit(self, sphere, distance, angle, rotate = None):	
        total_distance = distance + sphere.radius + self.radius

        x, y, z = sphere.position

        x2 = (total_distance) * cos(angle) + x
        y2 = 0 + y
        z2 = (total_distance) * sin(angle) + z
        
        self.move_to(x2, y2, z2)
        
        if rotate:
            self.rotate(rotate)

    def _sphere(self, u, v):
        theta = (u * pi / (self.density - 1)) - self.half_pi
        phi = (v * 2 * pi) / (self.density - 1)

        x = self.radius * cos(theta) * cos(phi)
        y = self.radius * sin(theta)
        z = self.radius * cos(theta) * sin(phi)

        return x, y, z

    def _draw_filled_sphere(self, rotation):
        glPushMatrix()
        
        glTranslatef(*self.position)
        glRotatef(self.angle,*rotation)

        for i in range(0, self.density):
            glBegin(GL_TRIANGLE_STRIP)
            for j in range(0, self.density):
                self._setColor(i, j)
                glVertex3fv(self._sphere(i,j))
                glVertex3fv(self._sphere(i - 1,j))
            glEnd()

        glPopMatrix()

    def _setColor(self, i, j): 
        if i < self.density//2: 
            r = (i) / (self.density /2 - 1)
            g = (i) / (self.density /2 - 1)
            b = (i) / (self.density /2 - 1)
        else:
            r = ((self.density - i) / (self.density /2 - 1)) - 0.08
            g = ((self.density - i) / (self.density /2 - 1)) - 0.08
            b = ((self.density - i) / (self.density /2 - 1)) - 0.08
        
        glColor3f(r + (self.color[0] / 255), g + (self.color[1] / 255), b + (self.color[2] / 255))


