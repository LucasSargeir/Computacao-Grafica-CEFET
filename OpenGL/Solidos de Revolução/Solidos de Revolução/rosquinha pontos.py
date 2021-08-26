from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 50
rotation_speed = 1
global_radius = 5
hole_radius = 2.5
color = 0.001


def donut(u, v):
    theta = ( u * 2 * pi) / (density - 1)
    phi = (v * 2 * pi) / (density - 1)
    x = (global_radius + hole_radius * cos(theta)) * cos(phi)
    y = (global_radius + hole_radius * cos(theta)) * sin(phi)
    z = (hole_radius * sin(theta))

    return x, y, z

def draw_donut_points():
    glBegin(GL_POINTS)
    for i in range(density):
        for j in range(density):
            glVertex3fv(donut(i,j))
    glEnd()

angle = 0

def setColor(i, j): 
    r = (i) / (density - 1)
    g = (i) / (density - 1)
    b = (i) / (density - 1)
    glColor3f(r, g, b)

def draw_filled_donut():
    
    glBegin(GL_TRIANGLE_STRIP)

    for i in range(density):    
        for j in range(density):
            glVertex3fv(donut(i,j))
            glVertex3fv(donut(i - 1,j))
            setColor(i,j)
    glEnd()

angle = 0

def draw():
    global angle
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    
    glRotatef(angle,0,1,0)
    draw_filled_donut()    
    
    glPopMatrix()
    glutSwapBuffers()
    
    angle += rotation_speed
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Donut")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)
glutTimerFunc(50,timer,1)
glutMainLoop()


