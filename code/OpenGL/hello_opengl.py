# Hello World
# only creates an empty window

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display(): # to refresh the display
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # sets the bitplane area of the window to values previously selected by glClearColor
    glutSwapBuffers() # swaps the buffers of the current window if double buffered
    return

glutInit()  # initialize the GLUT library.
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH) # initial display mode
    # GLUT_DOUBLE:  Bit mask to select a double buffered window.
	# GLUT_RGB: Bit mask to select an RGBA mode window.
	# GLUT_DEPTH: Bit mask to select a window with a depth buffer.
glutInitWindowSize(400,400) # initial window size of course
glutCreateWindow("MyWindowName") # create a window
glClearColor(1.,1.,1.,1.) # initial background color RGBA 
glutDisplayFunc(display) # called when GLUT determines that the normal plane for the window needs to be redisplayed
glutMainLoop() # enters the GLUT event processing loop.