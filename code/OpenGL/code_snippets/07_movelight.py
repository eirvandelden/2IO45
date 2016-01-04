from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

spin = 0

def init():
	glClearColor (0.0, 0.0, 0.0, 0.0)
	glShadeModel (GL_SMOOTH)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)


#/* Here is where the light position is reset after the modeling
#* transformation (glRotated) is called. This places the
#* light at a new position in world coordinates. The cube
#* represents the position of the light.
#*/
def display():
	#=======================================================================================
	# DIFFERENT MATERIAL
	no_mat = [ 0.0, 0.0, 0.0, 1.0 ]
	mat_ambient = [ 0.7, 0.7, 0.7, 1.0 ]
	mat_ambient_color = [ 0.8, 0.8, 0.2, 1.0 ]
	mat_diffuse = [ 0.1, 0.5, 0.8, 1.0 ]
	mat_specular = [ 1.0, 1.0, 1.0, 1.0 ]
	no_shininess = [ 0.0 ]
	low_shininess = [ 5.0 ]
	high_shininess = [ 100.0 ]
	mat_emission = [0.3, 0.2, 0.2, 0.0]
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	#/* draw sphere in first row, first column
	#* diffuse reflection only no ambient or specular
	#*/
	glPushMatrix()
	glTranslatef (-3.75, 3.0, 0.0)
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
	glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
	glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
	glutSolidSphere(1.0, 16, 16)
	glPopMatrix()
	#/* draw sphere in first row, second column
	#* diffuse and specular reflection low shininess no ambient
	#*/
	glPushMatrix()
	glTranslatef (-1.25, 3.0, 0.0)
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, low_shininess)
	glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
	glutSolidSphere(1.0, 16, 16)
	glPopMatrix()
	#/* draw sphere in first row, third column
	#* diffuse and specular reflection high shininess no ambient
	#*/
	glPushMatrix()
	glTranslatef (1.25, 3.0, 0.0)
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)
	glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
	glutSolidSphere(1.0, 16, 16)
	glPopMatrix()
	#/* draw sphere in first row, fourth column
	#* diffuse reflection emission no ambient or specular refl.
	#*/
	glPushMatrix()
	glTranslatef (3.75, 3.0, 0.0)
	glMaterialfv(GL_FRONT, GL_AMBIENT, no_mat)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
	glMaterialfv(GL_FRONT, GL_SHININESS, no_shininess)
	glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
	glutSolidSphere(1.0, 16, 16)
	glPopMatrix()
	#=======================================================================================

	position = [ 0.0, 0.0, 1.5, 1.0 ]
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix ()
	glTranslatef (0.0, 0.0, -5.0)
	glPushMatrix ()
	glRotated (spin, 1.0, 0.0, 0.0)
	glLightfv (GL_LIGHT0, GL_POSITION, position)
	glTranslated (0.0, 0.0, 1.5)
	glDisable (GL_LIGHTING)
	glColor3f (0.0, 1.0, 1.0)
	glutWireCube (0.1)
	glEnable (GL_LIGHTING)
	glPopMatrix ()
	glutSolidTorus (0.275, 0.85, 8, 15)
	glPopMatrix ()
	glFlush ()

def reshape (w, h):
	glViewport (0, 0, w, h)
	glMatrixMode (GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(40.0, w/h, 1.0, 20.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def mouse(button, state, x, y):
	global spin
	if button == GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN):
			spin = (spin + 30) % 360
		glutPostRedisplay()

glutInit()
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ("")
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutMainLoop()