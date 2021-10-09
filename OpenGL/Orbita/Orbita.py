from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Sphere import Sphere, rotate, angle
import math

sun = Sphere(0,0,0,1, color = (160, 100,  -300))
earth = Sphere(4,0,0,0.3, color = (0, 0, 200))
moon = Sphere(4.8,0,0,0.1, color = (200, 200, 200))

def draw():

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	sun.draw(rotation = (angle['sun']['translation'],1,1,1))
	rotate('sun')
	
	earth.draw(rotation = (angle['earth']['translation'],1,1,1))
	moon.draw(rotation = (angle['moon']['translation'],1,1,1))

	pos_earth = earth.get_orbit_position(sun, 3, angle['earth']['rotation'])
	earth.move_to(*pos_earth)
	rotate('earth')

	pos_moon = moon.get_orbit_position(earth, 0.5, angle['moon']['rotation'])
	moon.move_to(*pos_moon)
	rotate('moon')

	glutSwapBuffers()

def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1000,800)
glutCreateWindow('Solar System')
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


