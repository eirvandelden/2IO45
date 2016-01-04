from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

xrot, yrot = 0.0,0.0

def drawBox():
    glBegin(GL_QUADS)

    # front
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)

	# back
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
	
    # left
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
	
    # right
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glColor3f(0.0, 0.0, 1.0)
	
    # top
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
	
    # bottom
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glEnd();

def idle():
    global xrot, yrot
    xrot, yrot = xrot + 0.1,yrot + 0.1
    display()
	
def rotate(x,y):
    glRotatef(x, 1.0, 0.0, 0.0)
    glRotatef(y, 0.0, 1.0, 0.0)
	
# The display function is very simple. It simply places the camera 3 units down the z axis, applies two rotation transformations and renders the cube. 
# void display()
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    rotate(xrot,yrot)
    drawBox()
    glFlush()
    glutSwapBuffers() # swaps the buffers of the current window if double buffered

glutInit()  # initialize the GLUT library.
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH) # initial display mode
glutInitWindowSize(400,400) # initial window size of course
glutCreateWindow("A Box") # create a window
glClearColor(0.93, 0.93, 0.93, 0.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LEQUAL)
glClearDepth(1.0)
glutIdleFunc(idle)
glutDisplayFunc(display) # called when GLUT determines that the normal plane for the window needs to be redisplayed
glutMainLoop() # enters the GLUT event processing loop.
	
