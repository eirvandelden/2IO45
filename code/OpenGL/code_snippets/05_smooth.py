from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor (0.0, 0.0, 0.0, 0.0)
	glShadeModel (GL_SMOOTH)

def triangle():
	glBegin (GL_TRIANGLES)
	glColor3f (1.0, 0.0, 0.0)
	glVertex2f (5.0, 5.0)
	glColor3f (0.0, 1.0, 0.0)
	glVertex2f (25.0, 5.0)
	glColor3f (0.0, 0.0, 1.0)
	glVertex2f (5.0, 25.0)
	glEnd()

def display():
	glClear (GL_COLOR_BUFFER_BIT)
	triangle ()
	glFlush ()

def reshape (w, h):
	glViewport (0, 0, w, h)
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity ()
	if (w <= h):
		gluOrtho2D (0.0, 30.0, 0.0, 30.0*h/w)
	else:
		gluOrtho2D (0.0, 30.0*w/h, 0.0, 30.0)
	glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ("")
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()