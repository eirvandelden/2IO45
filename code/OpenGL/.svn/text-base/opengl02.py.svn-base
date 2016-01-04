import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

spin = 0.0

def init():
   glClearColor(0.0, 0.0, 0.0, 0.0)
   glShadeModel(GL_FLAT)

def display():
   glClear(GL_COLOR_BUFFER_BIT)
   glPushMatrix()
   glRotatef(spin, 0.0, 0.0, 1.0)
   glColor3f(1.0, 1.0, 1.0)
   glRectf(-25.0, -25.0, 25.0, 25.0)
   glPopMatrix()
   glutSwapBuffers()

def spinDisplay():
   global spin
   spin = (spin + 2.0) % 360.0
   time.sleep(0.01)
   glutPostRedisplay()

def spinDisplay2():
   global spin
   spin = (spin - 2.0) % 360.0
   time.sleep(0.01)
   glutPostRedisplay()
   
def reshape(width, height):
   glViewport(0, 0, width, height)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-50.0, 50.0, -50.0, 50.0, -1.0, 1.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()

def mouse(button, state, x, y):
   if button == GLUT_LEFT_BUTTON:
       if state == GLUT_DOWN:
           glutIdleFunc(spinDisplay)
   elif button == GLUT_MIDDLE_BUTTON:
       if state == GLUT_DOWN:
           glutIdleFunc(spinDisplay2)

if __name__ == "__main__":
   glutInit()
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
   glutCreateWindow("")
   glutInitWindowSize(250, 250)
   glutInitWindowPosition(100, 100)
   init()
   glutDisplayFunc(display)
   glutReshapeFunc(reshape)
   glutMouseFunc(mouse)
   glutMainLoop()