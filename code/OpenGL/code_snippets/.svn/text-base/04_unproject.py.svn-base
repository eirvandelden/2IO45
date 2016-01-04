from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glFlush()

def reshape(w, h):
	glViewport (0, 0,  w,  h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective (45.0, w/ h, 1.0, 100.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def mouse(button, state, x, y):
	#GLint viewport[4]
	viewport = []
	#GLdouble mvmatrix[16], projmatrix[16]
	#GLint realy /* OpenGL y coordinate position */
	#GLdouble wx, wy, wz /* returned world x, y, z coords */
	wx = 0
	wy = 0
	wz = 0
	if button == GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN):
			viewport = glGetIntegerv (GL_VIEWPORT)
			mvmatrix = glGetDoublev (GL_MODELVIEW_MATRIX)
			projmatrix = glGetDoublev (GL_PROJECTION_MATRIX)
			#/* note viewport[3] is height of window in pixels */
			realy = viewport[3] - y - 1
			#printf ("Coordinates at cursor are (%4d, %4d)\n", x, realy)
			#gluUnProject (x, realy, 0.0, mvmatrix, projmatrix, viewport, wx, wy, wz)
			gluUnProject (wx, wy, wz, mvmatrix, projmatrix, viewport)
			#print "World coords at z=0.0 are (%f, %f, %f)\n", wx, wy, wz)
			#gluUnProject (x, realy, 1.0, mvmatrix, projmatrix, viewport, wx, wy, wz)
			#printf ("World coords at z=1.0 are (%f, %f, %f)\n", wx, wy, wz)

		elif button == GLUT_RIGHT_BUTTON:
			if (state == GLUT_DOWN):
				sys.exit()

glutInit()
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ("")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutMainLoop()