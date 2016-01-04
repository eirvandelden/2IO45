import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

leftFirst = GL_TRUE
ESCAPE = '\033'

def init():
	# Initialize alpha blending function.
	glEnable (GL_BLEND)
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glShadeModel (GL_FLAT)
	glClearColor (0.0, 0.0, 0.0, 0.0)

def drawLeftTriangle():
	# draw yellow triangle on LHS of screen
	glBegin (GL_TRIANGLES)
	glColor4f(1.0, 1.0, 0.0, 0.75)
	glVertex3f(0.1, 0.9, 0.0)
	glVertex3f(0.1, 0.1, 0.0)
	glVertex3f(0.7, 0.5, 0.0)
	glEnd()

def drawRightTriangle():
	# draw cyan triangle on RHS of screen
	glBegin (GL_TRIANGLES)
	glColor4f(0.0, 1.0, 1.0, 0.75)
	glVertex3f(0.9, 0.9, 0.0)
	glVertex3f(0.3, 0.5, 0.0)
	glVertex3f(0.9, 0.1, 0.0)
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	if (leftFirst):
		drawLeftTriangle()
		drawRightTriangle()
	else:
		drawRightTriangle()
		drawLeftTriangle()
	glFlush()

def reshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if (w <= h):
		gluOrtho2D (0.0, 1.0, 0.0, 1.0*h/w)
	else:
		gluOrtho2D (0.0, 1.0*w/h, 0.0, 1.0)

def keyboard(key, x, y):
	global leftFirst 
	if key == "t":
		leftFirst = not leftFirst
		glutPostRedisplay()
	elif key == ESCAPE:
		sys.exit()
		
if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize (200, 200)
	glutCreateWindow("")
	init()
	glutReshapeFunc (reshape)
	glutKeyboardFunc (keyboard)
	glutDisplayFunc (display)
	glutMainLoop()