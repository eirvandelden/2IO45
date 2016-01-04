from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

year = 0.0
day = 0.0

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0) # zwarte achtergrond

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	
	glPushMatrix()
	glutWireSphere(1.0, 20, 16) # zon
	glRotatef(year, 0.0, 1.0, 0.0)
	glTranslatef(2.0, 0.0, 0.0)
	glRotatef(day, 0.0, 1.0, 0.0)
	glutWireSphere(0.2, 10, 8) # planeet
	glPopMatrix()
	glutSwapBuffers()
	
def reshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60.0, w/h, 1.0, 20.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	
def keyboard(key, x, y):
	global day, year
	if key == "d":
		day = (day + 10) % 360
		glutPostRedisplay()
	elif key == "D":
		day = (day - 10) % 360
		glutPostRedisplay()
	elif key == "y":
		day = (year + 5) % 360
		glutPostRedisplay()
	elif key == "Y":
		day = (year - 5) % 360
		glutPostRedisplay()

if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(100, 100)
	glutCreateWindow("")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(reshape)
	glutKeyboardFunc(keyboard)
	glutMainLoop()