from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Texture import Texture
from Sphere import Sphere, rotate, set_angle, angle
import numpy

textures_files = {
    'earth': 'images/terra.png',
    'sun': 'images/sol.png',
    'moon': 'images/lua.png'
}
tx = Texture(textures_files, 'solar system', 640, 480)

sun = Sphere(0,0,0,1.2, tx = tx)
earth = Sphere(5,0,0,0.7, tx = tx)
moon = Sphere(6,0,0,0.2, tx = tx)

stars = []
total_stars = 1000
starts_range = 50

def draw_stars():
    
    glPushMatrix()

    glTranslatef(0,0,-30)

    glBegin(GL_POINTS)
    for i in range(total_stars):
        x = stars[0][i]*starts_range
        y = stars[1][i]*starts_range
        glVertex3fv((x, y, 0))
        glVertex3fv((-y, -x, 0))
        glVertex3fv((-x, y, 0))
        glVertex3fv((y, -x, 0))
    glEnd()
    
    glPopMatrix()	

def load_random_stars():

    x  = list(numpy.random.rand(1, total_stars)[0])
    y  = list(numpy.random.rand(1, total_stars)[0])
    stars.append(x)
    stars.append(y)

def draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    

    draw_stars()

    glLoadIdentity()  

    glTranslatef(0.0,0.0,-20.0)

    sun.draw(rotation = (angle['sun']['translation'],1,1,1), texture_index = 'sun')
    rotate('sun')

    earth.draw(rotation = (angle['earth']['translation'],1,1,1), texture_index = 'earth')
    moon.draw(rotation = (angle['moon']['translation'],1,1,1), texture_index = 'moon')

    pos_earth = earth.get_orbit_position(sun, 4.5, angle['earth']['rotation'])
    earth.move_to(*pos_earth)
    rotate('earth')

    pos_moon = moon.get_orbit_position(earth, .5, angle['moon']['rotation'])
    moon.move_to(*pos_moon)
    rotate('moon')

    glutSwapBuffers()


if __name__ == '__main__':
    
    load_random_stars()
    set_angle('sun', rotation = (0,0.1), translation = (0,0.9))
    set_angle('earth', rotation = (0,0.02), translation = (0,0.9))
    set_angle('moon', rotation = (0,0.1), translation = (0,0.2))
    tx.main(draw)

