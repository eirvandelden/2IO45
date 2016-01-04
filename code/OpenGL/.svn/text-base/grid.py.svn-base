from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math

positionz = []
positionx = []
xpos, ypos, zpos = 0,0,0
xrot, yrot, angle = 0,0,0.0
lastx,lasty = 0,0

def init():
    cubepositions()

def cubepositions():
    for i in range(0,10):
        positionz.append(random.randint(0, 4) + 5)
        positionx.append(random.randint(0, 4) + 5)
	
def drawgrid():
    for i in range(-500,501,5):
        glBegin(GL_LINES)
        glColor3ub(150, 190, 150)
        glVertex3f(-500, 0, i)
        glVertex3f(500, 0, i)
        glVertex3f(i, 0,-500)
        glVertex3f(i, 0, 500)
        glEnd()
	
def drawscene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# Clear Screen And Depth Buffer
    glLoadIdentity()									# Reset The Current Modelview Matrix
    gluLookAt(0,0,1,  0,0,0,   0,1,0)
    drawgrid()
    glTranslatef(0,1.0,0)
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glColor3f(1.0,0.5,0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glColor3f(1.0,0.0,0.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glColor3f(1.0,1.0,0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glColor3f(1.0,0.0,1.0)
    glVertex3f( 1.0, 1.0,-1.0)
    glVertex3f( 1.0, 1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glEnd()
	
def enable():
    glEnable (GL_DEPTH_TEST) #enable the depth testing
    glEnable (GL_LIGHTING) #enable the lighting
    glEnable (GL_LIGHT0) #enable LIGHT0, our Diffuse Light
    glShadeModel (GL_SMOOTH) #set the shader to smooth shader
	
def camera():
    glRotatef(xrot,1.0,0.0,0.0)  #rotate our camera on teh x-axis (left and right)
    glRotatef(yrot,0.0,1.0,0.0)  #rotate our camera on the y-axis (up and down)
    glTranslated(-xpos,-ypos,-zpos) #translate the screen to the position of our camera
	
def cube():
    for i in range (0,9):
        glPushMatrix()
        glTranslated(-positionx[i + 1] * 10, 0, -positionz[i + 1] * 10) #translate the cube
        glutSolidCube(2) #draw the cube
        glPopMatrix()
	
def display(): # to refresh the display
    global angle
    glClearColor (0.0,0.0,0.0,1.0)
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #drawscene()
    camera()
    enable()
    cube()
    glutSwapBuffers()
    angle = angle + 1
	
def reshape(w, h):
    glViewport(0, 0, w, h) #set the viewport to the current window specifications
    glMatrixMode(GL_PROJECTION) #set the matrix to projection
    glLoadIdentity()
    gluPerspective(60, w / h, 1.0, 1000.0) #set the perspective (angle of sight, width, height, , depth)
    glMatrixMode(GL_MODELVIEW) #set the matrix back to model

def mousemovement(x, y):
    global lastx, lasty, xrot, yrot
    diffx = x - lastx #check the difference between the current x and the last x position
    diffy = y - lasty #check the difference between the current y and the last y position
    lastx = x #set lastx to the current x position
    lasty = y #set lasty to the current y position
    xrot = xrot + diffy #set the xrot to xrot with the addition of the difference in the y position
    yrot = yrot + diffx	#set the xrot to yrot with the addition of the difference in the x position

def keyboard(key, x, y):
    global xrot, yrot, xpos, ypos, zpos
    if (key == 'q'):
        xrot = xrot + 1
		
    if (xrot > 360):
        xrot = xrot - 360

    if (key == 'z'):
        xrot = xrot - 1
		
    if (xrot < -360):
        xrot = xrot + 360;

    if (key == 'a'):
        yrotrad = (yrot / 180 * 3.141592654)
        xrotrad = (xrot / 180 * 3.141592654)
        xpos = xpos + math.sin(yrotrad)
        zpos = zpos - math.cos(yrotrad)
        ypos = ypos - math.sin(xrotrad)

    if (key == 'd'):
        yrotrad = (yrot / 180 * 3.141592654)
        xrotrad = (xrot / 180 * 3.141592654)
        xpos = xpos - math.sin(yrotrad)
        zpos = zpos + math.cos(yrotrad)
        ypos = ypos + math.sin(xrotrad)

    if (key == 'w'):
        yrotrad = (yrot / 180 * 3.141592654)
        xpos = xpos + math.cos(yrotrad) * 0.2
        zpos = zpos + math.sin(yrotrad) * 0.2

    if (key == 's'):
        yrotrad = (yrot / 180 * 3.141592654)
        xpos = xpos - math.cos(yrotrad) * 0.2
        zpos = zpos - math.sin(yrotrad) * 0.2

    if (key == 27):
        exit(0);
		 
# init		 
glutInit()
init()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)
glutInitWindowSize (500, 500); 
glutInitWindowPosition (100, 100);
glutCreateWindow("Grid") # create a window
glShadeModel(GL_SMOOTH) # Enable Smooth Shading
glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
glClearDepth(1.0) # Depth Buffer Setup
glEnable(GL_DEPTH_TEST) # Enables Depth Testing
glDepthFunc(GL_LEQUAL) # The Type Of Depth Testing To Do
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutPassiveMotionFunc(mousemovement)
glutKeyboardFunc(keyboard)
glutMainLoop()