from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Sphere import Sphere
import math

sun = Sphere(0,0,0,1, color = (160, 100,  -300), angle_speed = 5)
earth = Sphere(1,0,0,0.3, color = (0, 0, 200), angle_speed = 0.1)
moon = Sphere(1,0,0,0.1, color = (200, 200, 200), angle_speed = 0.1)

orbit_angle = 0
orbit_speed = 10

def draw():
	global orbit_angle

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	sun.draw()
	earth.orbit(sun, 3, orbit_angle, rotate = 50)   
	earth.draw()
	moon.orbit(earth, 0.3, orbit_angle + .01, rotate = 50)   
	moon.draw()

	glutSwapBuffers()

	orbit_angle += (2*math.pi)/(150 - orbit_speed)
 
def timer(i):
	glutPostRedisplay()
	glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1000,800)
glutCreateWindow("Sphere")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


