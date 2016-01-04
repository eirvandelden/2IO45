from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys # system routines
import data # Module For The Camera
#import pygame # for screen, mouse- and keyboardhandling

objCamera = data.CCamera() # Our Camera
pos = data.tVector3(0, 0, 0) # Vector Camera Position
view = data.tVector3(0, 0, 0) # View Vector Camera
up = data.tVector3(0, 0, 0) # Up Vector Camera
lastx = 0 # To Remember The Last Mouse Position

def ReSizeGLScene(width, height): # Resize And Initialize The GL Window
    if (height==0): # Prevent A Divide By Zero By
        height=1

    glViewport(0,0,width,height) # Reset The Current Viewport

    glMatrixMode(GL_PROJECTION) # Select The Projection Matrix
    glLoadIdentity() # Reset The Projection Matrix

    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, width / height, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW) #vSelect The Modelview Matrix
    glLoadIdentity() #vReset The Modelview Matrix

def InitGL(): # All Setup For OpenGL Goes Here
    glutInit()  # initialize the GLUT library.
    #pygame.init()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH) # initial display mode
    #glutInitWindowSize(400,400) # initial window size of course
    #glutCreateWindow("Welcome") # create a window
    glutGameModeString("990x768:32@75") # the settings for fullscreen mode
    glutEnterGameMode() # set glut to fullscreen using the settings in the line above
    glutIdleFunc(display)
    glutDisplayFunc(display) # called when GLUT determines that the normal plane for the window needs to be redisplayed
    glShadeModel(GL_SMOOTH) # Enable Smooth Shading
    glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
    glClearDepth(1.0) # Depth Buffer Setup
    glEnable(GL_DEPTH_TEST) # Enables Depth Testing
    glDepthFunc(GL_LEQUAL) # The Type Of Depth Testing To Do
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations
    objCamera.Position_Camera(0, 1.5, 4.0, 0, 1.5, 0, 0, 1.0, 0) # Set Camera Position
    glutReshapeFunc(reshape)
    glutPassiveMotionFunc(Mouse_Movement)
    glutKeyboardFunc(Keyboard_Input)
    glutMainLoop() # enters the GLUT event processing loop.
	

def Mouse_Movement(x, y):
    global lastx
    if x > lastx:
        angle_y = data.ROTATESPEED
    elif x < lastx:
        angle_y = -data.ROTATESPEED
    else:
        angle_y = 0
    objCamera.Rotate_Position(angle_y)
    lastx = x

def DrawGLScene(): # Here's Where We Do All The Drawing
    global xrot, yrot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Clear Screen And Depth Buffer
    glLoadIdentity() # Reset The Current Modelview Matrix
	
    # Assign Values to Local Variables to Prevent Long Lines Of Code	
    pos.x, pos.y, pos.z = objCamera.mPos.x, objCamera.mPos.y, objCamera.mPos.z
    view.x, view.y, view.z = objCamera.mView.x, objCamera.mView.y, objCamera.mView.z
    up.x, up.y, up.z = objCamera.mUp.x, objCamera.mUp.y, objCamera.mUp.z

    # use this function for opengl target camera
    gluLookAt(pos.x, pos.y, pos.z, view.x, view.y, view.z, up.x, up.y, up.z)

    glPushMatrix();
    # Always keep the character in the view
    glTranslatef(objCamera.mView.x, 0.0, objCamera.mView.z)
    Draw_Character()
    glPopMatrix()

    #glRotatef(yrot,0.0,1.0,0.0)  #rotate our camera on the y-axis (up and down)
	
    Draw_Grid()

    glPushMatrix()
    glScalef(0.5, 0.5, 0.5)
    glTranslatef(0,1.0,0)
	
    glBegin(GL_QUADS)
	
    # front
    glColor3f(0.0, 1.0, 0.0) # Green
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)

	# back
    glColor3f(1.0, 0.0, 1.0) # Magenta
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
	
    # left
    glColor3f(1.0, 0.0, 0.0) # Red
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
	
    # right
    glColor3f(1.0, 1.0, 0.0) # Yellow
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glColor3f(0.0, 0.0, 1.0)
	
    # top
    glColor3f(0.0, 0.0, 1.0) # Blue
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)
	
    # bottom
    glColor3f(0.0, 1.0, 1.0) # Aqua
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
	
    glEnd()
    glPopMatrix()

def Keyboard_Input(key, x, y):
    if (key == 'a') or (key == 'A'):
        objCamera.Strafe_Camera(-data.CAMERASPEED)
		
    if (key == 'w') or (key == 'W'):
        objCamera.Move_Camera(data.CAMERASPEED)
		
    if (key == 'd') or (key == 'D'):
        objCamera.Strafe_Camera(data.CAMERASPEED)
		
    if (key == 's') or (key == 'S'):				
        objCamera.Move_Camera(-data.CAMERASPEED)
		
    if (key == 'q') or (key == 'Q'):
        #glutLeaveGameMode() # set the resolution how it was
        sys.exit()
	
def Draw_Character(): # This object will symbolize our character
    glScalef(0.3, 1.0, 0.3)
    glTranslatef(0, 1.0, 0)
    glBegin(GL_TRIANGLES)				
    glColor3f(1.0, 0.0, 0.0)				
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f( 1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)
    glEnd()
	
def Draw_Grid():
    for i in range(-500, 501, 5):
        glBegin(GL_LINES)
        glColor3ub(150, 190, 150)
        glVertex3f(-500, 0, i)
        glVertex3f(500, 0, i)
        glVertex3f(i, 0, -500)
        glVertex3f(i, 0, 500)
        glEnd()
		
def reshape(w, h):
    glViewport(0, 0, w, h) #set the viewport to the current window specifications
    glMatrixMode(GL_PROJECTION) #set the matrix to projection
    glLoadIdentity()
    gluPerspective(60, w / h, 1.0, 1000.0) #set the perspective (angle of sight, width, height, , depth)
    glMatrixMode(GL_MODELVIEW) #set the matrix back to model
		
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    DrawGLScene()
    glFlush()
    glutSwapBuffers() # swaps the buffers of the current window if double buffered
	
if __name__ == '__main__':
    InitGL()