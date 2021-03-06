from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 15
rotation_speed = 2

def setColor(i, j): 
    
    if j < density//2: 
        r = (j) / (density/2 - 1)
        g = (j) / (density/2 - 1)
        b = (j) / (density/2 - 1)
    else:
        r = ((density - j) / (density/2 - 1)) - 0.08
        g = ((density - j) / (density/2 - 1)) - 0.08
        b = ((density - j) / (density/2 - 1)) - 0.08
    
    glColor3f(r, g, b)

def second_degree_function(u, v):
    theta = (v * 2 * pi) / (density - 1)
    w = (u * 2 / (density - 1))

    x = w * cos(theta)
    y = w ** 2
    z = w * sin(theta)

    return x, y, z

def third_degree_function(u, v):
    theta = (v * 2 * pi) / (density - 1)
    w = ((u * 4) / (density - 1)) - 2

    x = w * cos(theta)
    y = w ** 3
    z = w * sin(theta)

    return x, y, z

def draw_second_degree_function_points():
    glTranslatef(-6,-1,0)
    glRotatef(angle,0,1,0)
    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)
    for i in range(density):
        for j in range(density):
            x, y, z = second_degree_function(i,j)
            glVertex3f(x, -y, z)
    glEnd()

def draw_third_degree_function_points():
    glTranslatef(6,0,0)
    glRotatef(angle,0,1,0)
    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)
    for i in range(density):
        for j in range(density):
            glVertex3fv(third_degree_function(i,j))
    glEnd()

def draw_filled_second_degree_function():
    glTranslatef(-6,1,0)
    glRotatef(angle,0,1,0)

    for i in range(density):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(i, j)
            glVertex3fv(second_degree_function(i,j))
            glVertex3fv(second_degree_function(i - 1,j))
        glEnd()

def draw_filled_third_degree_function():
    glTranslatef(0,0,0)
    glRotatef(angle,0,1,0)

    for i in range(1,density):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(density):
            setColor(i, j)
            glVertex3fv(third_degree_function(i,j))
            glVertex3fv(third_degree_function(i - 1,j))
        glEnd()

angle = 0

def draw():
    global angle
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    draw_filled_second_degree_function()    
    glPopMatrix()
   
    glPushMatrix()
    draw_filled_third_degree_function()    
    glPopMatrix()
    
    glPushMatrix()
    draw_third_degree_function_points()    
    glPopMatrix()
    
    glPushMatrix()
    draw_second_degree_function_points()    
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
glutCreateWindow("2/3 Degrees Functions")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-25)
glutTimerFunc(50,timer,1)
glutMainLoop()


