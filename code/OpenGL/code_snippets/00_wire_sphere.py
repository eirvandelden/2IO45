from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0) # zwarte achtergrond

def display():
	eqn = [0.0, 1.0, 0.0, 0.0]
	eqn2 = [1.0, 0.0, 0.0, 0.0]
		
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0) # witte tekenlijnen
	glPushMatrix()
	glTranslatef(0.0, 0.0, -5.0) # verplaats -5 op z-as
	
	glClipPlane(GL_CLIP_PLANE0, eqn)
	glEnable(GL_CLIP_PLANE0)
	
	glClipPlane(GL_CLIP_PLANE1, eqn2)
	glEnable(GL_CLIP_PLANE1)
	
	glRotatef(90.0, 1.0, 0.0, 0.0) # draaiing 90 graden om punt x,y,z
	glutWireSphere(1.0, 20, 16) # wire sphere
	glPopMatrix()
	glFlush()
	
def reshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60.0, w/h, 1.0, 20.0)
	glMatrixMode(GL_MODELVIEW)
	
if __name__ == "__main__":
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(100, 100)
	glutCreateWindow("")
	init()
	glutDisplayFunc(display)
	glutReshapeFunc(reshape)
	glutMainLoop()