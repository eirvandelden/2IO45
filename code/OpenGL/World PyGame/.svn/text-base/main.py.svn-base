from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import os
import sys # system routines
import data # Module For The Camera
import pygame
from pygame.locals import *

__author__ = "Leroy Bakker"

pygame.init()

# contants
SCREEN_SIZE = (640,480)
DISPLAY_FLAGS = OPENGL|DOUBLEBUF|FULLSCREEN

# global variables
objCamera = data.CCamera() # Our Camera
pos = data.tVector3(0, 0, 0) # Vector Camera Position
view = data.tVector3(0, 0, 0) # View Vector Camera
up = data.tVector3(0, 0, 0) # Up Vector Camera
lastx = 0 # To Remember The Last Mouse Position

def glInit():
    glutInit()  # initialize the GLUT library.
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH) # initial display mode
    glShadeModel(GL_SMOOTH) # Enable Smooth Shading
    glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
    glClearDepth(1.0) # Depth Buffer Setup
    glEnable(GL_DEPTH_TEST) # Enables Depth Testing
    glDepthFunc(GL_LEQUAL) # The Type Of Depth Testing To Do
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations
    objCamera.Position_Camera(0, 1.5, 4.0, 0, 1.5, 0, 0, 1.0, 0) # Set Camera Position
    glViewport(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]) # Reset The Current Viewport
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, SCREEN_SIZE[0]/SCREEN_SIZE[1], 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
	
class MyWorld():
    #mousepos = (0,0)
    lastx = 0
	
    def __init__(self):
        global screen
        self.screen = screen
        self.done = False
		
    def Draw_Character(self): # This object will symbolize our character
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

    def Draw_Grid(self):
        for i in range(-500, 501, 5):
            glBegin(GL_LINES)
            glColor3ub(150, 190, 150)
            glVertex3f(-500, 0, i)
            glVertex3f(500, 0, i)
            glVertex3f(i, 0, -500)
            glVertex3f(i, 0, 500)
            glEnd()
		
    def DrawScreen(self):
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
        self.Draw_Character()
        glPopMatrix()

        #glRotatef(yrot,0.0,1.0,0.0)  #rotate our camera on the y-axis (up and down)

        self.Draw_Grid()

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
		
    def Go(self):
        global lastx
        pygame.mouse.set_visible(0)
        pygame.mouse.set_pos(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        while not self.done:
            self.DrawScreen() # draw the world
            for event in pygame.event.get(): # watch for events
                if event.type == QUIT: 
                    self.done = True
                elif event.type == KEYDOWN: # if a key is pressed
                    if event.key == K_ESCAPE: # escape key
                        self.done = True
                elif event.type == MOUSEMOTION:
                        objCamera.Mouse_Move(SCREEN_SIZE[0],SCREEN_SIZE[1])
						
            keystate = pygame.key.get_pressed() # get the pressed key
            # moving forward
            if keystate[K_UP]: objCamera.Move_Camera(data.CAMERASPEED)
            if keystate[K_w]: objCamera.Move_Camera(data.CAMERASPEED)
            # moving backward
            if keystate[K_DOWN]: objCamera.Move_Camera(-data.CAMERASPEED)
            if keystate[K_s]: objCamera.Move_Camera(-data.CAMERASPEED)
            # moving left
            if keystate[K_LEFT]: objCamera.Strafe_Camera(-data.CAMERASPEED)
            if keystate[K_a]: objCamera.Strafe_Camera(-data.CAMERASPEED)
            # moving right
            if keystate[K_RIGHT]: objCamera.Strafe_Camera(data.CAMERASPEED)
            if keystate[K_d]: objCamera.Strafe_Camera(data.CAMERASPEED)
            pygame.display.flip()
		
if __name__ == '__main__':
    # init screen
    os.environ["SDL_VIDEO_CENTERED"] = "1" # Center the graphics window.
    screen = pygame.display.set_mode(SCREEN_SIZE,DISPLAY_FLAGS)
    pygame.display.set_caption("World PyGame")
    
    # init GL
    glInit()  # initialize the GLUT library.
    glEnable(GL_TEXTURE_2D)
    
    mw = MyWorld()
    mw.Go()