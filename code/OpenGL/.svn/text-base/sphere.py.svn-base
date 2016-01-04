# Draw a sphere with light effect

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init_display_list():
    glNewList(1,GL_COMPILE)
    glPushMatrix()
    glTranslatef(0,0,0) # move to where we want to put object
    glutSolidSphere(1,25,25) # make radius 1 sphere of res 15x15
    glEndList()

def display(): # to refresh the display
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # sets the bitplane area of the window to values previously selected by glClearColor
    glCallList(1)
    init_display_list() # yeeey draw!	
    glutSwapBuffers() # swaps the buffers of the current window if double buffered

glutInit()  # initialize the GLUT library.
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH) # initial display mode
    # GLUT_DOUBLE:  Bit mask to select a double buffered window.
	# GLUT_RGB: Bit mask to select an RGBA mode window.
	# GLUT_DEPTH: Bit mask to select a window with a depth buffer.
glutInitWindowSize(400,400) # initial window size of course
glutCreateWindow("MyWindowName") # create a window
glClearColor(0.,0.,0.,1.) # initial background color RGBA 
glutDisplayFunc(display) # called when GLUT determines that the normal plane for the window needs to be redisplayed

# --------------------- some properties ----------------------------
glEnable(GL_CULL_FACE) # enable backface culling
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING) # enable lights
# -------------------------- a light -----------------------------------
lightZeroPosition0 = [10,10,10,1] # position of light
lightZeroColor0 = [0.9,0.3,0.2,1.0] # reddish :P
glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition0) # position
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor0) # color
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1) # something with brightness
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.005) # something with brightness
glEnable(GL_LIGHT0)
#--- ------------------------------------------------------------------

# -------------------------- a 2nd light -----------------------------------
lightZeroPosition1 = [-10,-10,-10,1] # position of light
lightZeroColor1 = [0.2,0.7,0.2,1.0] # greenish :P
glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition1) # position
glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor1) # color
glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1) # something with brightness
glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05) # something with brightness
glEnable(GL_LIGHT1)
#--- ---------------------------------------------------------------------------

glutMainLoop() # enters the GLUT event processing loop.