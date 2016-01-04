import os
import time
import string
import camera
import vector

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, pi

import pygame
pygame.init()
from pygame.locals import *

__author__ = "Leroy Bakker"
__version__ = "2009-05-15"
__license__ = "Public Domain"

SCREEN_SIZE = (640,480) # screen size when not fullscreen
BOARD_SIZE = 20 # number of squares in the length and width
TEXTURESQUARES = 1 # number of squares on the length of the used texture
FLOOR_SIZE = 80*BOARD_SIZE # size of the floor
FLOOR_TEXREP = BOARD_SIZE / TEXTURESQUARES # number of texture repetitions
SQUARE_SIZE = FLOOR_SIZE / BOARD_SIZE # length and width of a square
DISPLAY_FLAGS = OPENGL|DOUBLEBUF#|FULLSCREEN # display settings

# global variables
objCamera = camera.CCamera() # Our Camera
pos = vector.tVector3(0, 0, 0) # Vector Camera Position
view = vector.tVector3(0, 0, 0) # View Vector Camera
up = vector.tVector3(0, 0, 0) # Up Vector Camera
rotation = 1.0

def glInit():
  glutInit()  # initialize the GLUT library.
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) # initial display mode
  glShadeModel(GL_SMOOTH) # Enable Smooth Shading
  glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
	
  glClearDepth(1.0) # Depth Buffer Setup
  glEnable(GL_DEPTH_TEST) # Enables Depth Testing
  glDepthFunc(GL_LEQUAL) # The Type Of Depth Testing To Do
  glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations
	
  objCamera.Position_Camera(10, 4, 12,   9, 4, 12,   0, 1, 0) # Set Camera Position
	
  glViewport(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]) # Reset The Current Viewport
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
	
  # Calculate The Aspect Ratio Of The Window
  gluPerspective(45.0, SCREEN_SIZE[0]/SCREEN_SIZE[1], 0.1, 5000.0)
  glMatrixMode(GL_MODELVIEW)
	
  glCullFace(GL_BACK) # Don't draw the back sides of polygons
  glEnable(GL_CULL_FACE) # Turn on culling

class BlocksWorld:
    """A very simple virtual world, inspired by the classic SHRDLU."""
    def __init__(self,**options):
        global screen
        self.screen = screen
        self.done = False

        # Auto-load all images in the graphics directory.
        self.textures = {}
        images = os.listdir(os.path.join("graphics","textures"))
        for image in images:
            try:
                self.LoadTexture(image,image[:-4])
            except:
                print "The filename '"+image+"' couldn't be loaded."

        #pygame.font.init()
        self.board = []
        
    def LoadTexture(self,filename,name):
        filename = os.path.join("graphics","textures",filename)
        texture = pygame.image.load(filename)
        self.textures[name] = len(self.textures) # A texture number.
        texture_data = pygame.image.tostring(texture, "RGBX", 1 )
        glBindTexture(GL_TEXTURE_2D,len(self.textures)-1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
		
    def DrawFloor(self,size,texrep,texture):
        glBindTexture(GL_TEXTURE_2D,texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size,0.0,-size) # left back
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size,0.0,size) # left front
        glTexCoord2f(texrep,texrep)
        glVertex3f(size,0.0,size) # right front
        glTexCoord2f(0.0,texrep)
        glVertex3f(size,0.0,-size) # right back
        glEnd()

    def DrawSky(self, size, texrep, x, y, z):
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		
        glBindTexture(GL_TEXTURE_2D, self.textures["gal5"])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(  size, -size, -size )
        glTexCoord2f(1, 0)
        glVertex3f( -size, -size, -size )
        glTexCoord2f(1, 1)
        glVertex3f( -size,  size, -size )
        glTexCoord2f(0, 1)
        glVertex3f(  size,  size, -size )
        glEnd()

        # Render the left quad
        glBindTexture(GL_TEXTURE_2D, self.textures["gal5"])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f( size, -size,  size )
        glTexCoord2f(1, 0)
        glVertex3f( size, -size, -size )
        glTexCoord2f(1, 1) 
        glVertex3f( size,  size, -size )
        glTexCoord2f(0, 1) 
        glVertex3f( size,  size,  size )
        glEnd()

        # Render the back quad
        glBindTexture(GL_TEXTURE_2D, self.textures["gal5"])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0) 
        glVertex3f( -size, -size,  size )
        glTexCoord2f(1, 0) 
        glVertex3f(  size, -size,  size )
        glTexCoord2f(1, 1) 
        glVertex3f(  size,  size,  size )
        glTexCoord2f(0, 1) 
        glVertex3f( -size,  size,  size )
        glEnd()

        # Render the right quad
        glBindTexture(GL_TEXTURE_2D, self.textures["gal5"])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0) 
        glVertex3f( -size, -size, -size )
        glTexCoord2f(1, 0) 
        glVertex3f( -size, -size,  size )
        glTexCoord2f(1, 1) 
        glVertex3f( -size,  size,  size )
        glTexCoord2f(0, 1) 
        glVertex3f( -size,  size, -size )
        glEnd()

        # Render the top quad
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1) 
        glVertex3f( -size,  size, -size )
        glTexCoord2f(0, 0) 
        glVertex3f( -size,  size,  size )
        glTexCoord2f(1, 0) 
        glVertex3f(  size,  size,  size )
        glTexCoord2f(1, 1) 
        glVertex3f(  size,  size, -size )
        glEnd()

        # Render the bottom quad
        #glBegin(GL_QUADS)
        #glTexCoord2f(0, 0)
        #glVertex3f( -size, -size, -size )
        #glTexCoord2f(0, 1)
        #glVertex3f( -size, -size,  size )
        #glTexCoord2f(1, 1)
        #glVertex3f(  size, -size,  size )
        #glTexCoord2f(1, 0)
        #glVertex3f(  size, -size, -size )
        #glEnd()
		
    def DrawWallsPlanes(self,texture):
        glTranslatef(0.0, 0.5*SQUARE_SIZE, -0.5*FLOOR_SIZE)
        width = 0.5*FLOOR_SIZE
        height = 0.5*SQUARE_SIZE
        texrep = BOARD_SIZE

        glBindTexture(GL_TEXTURE_2D,texture)
		
        # draw the back wall
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex3f(-width, -height,  0.0) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( width, -height,  0.0) # right bottom
        glTexCoord2f(texrep,1.0)
        glVertex3f( width,  height,  0.0) # right top
        glTexCoord2f(0.0,1.0)
        glVertex3f(-width,  height,  0.0) # left top
        glEnd()
		
        # draw the right wall
        glTranslatef(0.5*FLOOR_SIZE, 0.0, 0.5*FLOOR_SIZE)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex3f(0.0, -height,  -width) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f(0.0, -height,  width) # right bottom
        glTexCoord2f(texrep,1.0)
        glVertex3f(0.0,  height,  width) # right top
        glTexCoord2f(0.0,1.0)
        glVertex3f(0.0,  height,  -width) # left top
        glEnd()
		
        # draw the front wall
        glTranslatef(-0.5*FLOOR_SIZE, 0.0, 0.5*FLOOR_SIZE)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex3f(width, -height,  0.0) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f(-width, -height,  0.0) # right bottom
        glTexCoord2f(texrep,1.0)
        glVertex3f(-width,  height,  0.0) # right top
        glTexCoord2f(0.0,1.0)
        glVertex3f(width,  height,  0.0) # left top
        glEnd()
		
        # draw the left wall
        glTranslatef(-0.5*FLOOR_SIZE, 0.0, -0.5*FLOOR_SIZE)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0,0.0)
        glVertex3f(0.0, -height,  width) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f(0.0, -height,  -width) # right bottom
        glTexCoord2f(texrep,1.0)
        glVertex3f(0.0,  height,  -width) # right top
        glTexCoord2f(0.0,1.0)
        glVertex3f(0.0,  height,  width) # left top
        glEnd()
	
    def DrawSphere(self, radius, texture, x, y, z):
        glTranslatef(x,y,z)
        q = gluNewQuadric() # Create A New Quadratic
 
        gluQuadricNormals(q, GL_SMOOTH) # Generate Smooth Normals For The Quad
        gluQuadricTexture(q, GL_TRUE) # Enable Texture Coords For The Quad

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
		
        #glColor4f(1.0, 1.0, 1.0, 0.4)
        
        glBindTexture(GL_TEXTURE_2D, texture) # Select Texture
        #glEnable(GL_BLEND) # Enable Blending
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE) # Set Blending Mode To Mix Based On SRC Alpha
        glEnable(GL_TEXTURE_GEN_S) # Enable Sphere Mapping
        glEnable(GL_TEXTURE_GEN_T) # Enable Sphere Mapping

        gluSphere(q, radius, 32, 32) # Draw Sphere

        glDisable(GL_TEXTURE_GEN_S) # Disable Sphere Mapping
        glDisable(GL_TEXTURE_GEN_T) # Disable Sphere Mapping
        glDisable(GL_BLEND) # Disable Blending
        glTranslatef(-x,-y,-z)
		
    def DrawWallsCubes(self,size,texrep,texture):
        # go to the middle of the left top square of the floor
        x = -(0.5*FLOOR_SIZE) - (0.5*SQUARE_SIZE)
        y = 0.5 * SQUARE_SIZE
        z = -(0.5*FLOOR_SIZE) + (0.5*SQUARE_SIZE)
        
        # draw the back wall
        for i in range(0,BOARD_SIZE):
            glTranslatef(SQUARE_SIZE, 0.0, 0.0) # go to pos to draw
            self.DrawCube(size,texrep,texture,x,y,z) # draw cube
			
        # draw the right wall
        for i in range(0,BOARD_SIZE):
            glTranslatef(0,0,SQUARE_SIZE) # go to pos to draw
            self.DrawCube(size,texrep,texture,x,y,z) # draw cube
			
        # draw the front wall
        for i in range(0,BOARD_SIZE):
            glTranslatef(-SQUARE_SIZE,0,0) # go to pos to draw
            self.DrawCube(size,texrep,texture,x,y,z) # draw cube
			
        # draw the left wall
        for i in range(0,BOARD_SIZE):
            glTranslatef(0,0,-SQUARE_SIZE) # go to pos to draw
            self.DrawCube(size,texrep,texture,x,y,z) # draw cube     
			
    def DrawExplosionMid(self,size,texrep,texture,x,y,z):
        glTranslatef(x,y,z)
        glDisable(GL_CULL_FACE)
        glBindTexture(GL_TEXTURE_2D,texture)
        
        glEnable(GL_BLEND) # Enable Blending
        glBlendFunc(GL_SRC_ALPHA, GL_ONE) # Set Blending Mode To Mix Based On SRC Alpha
        
        glBegin(GL_QUADS)
	
        # front
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -0.5*size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -0.5*size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  0.5*size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  0.5*size,  size) # left top

      	# back
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -0.5*size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  0.5*size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  0.5*size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -0.5*size, -size) # left bottom
	
        # left
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -0.5*size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  0.5*size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  0.5*size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -0.5*size, -size) # left bottom

        # right
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -0.5*size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  0.5*size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  0.5*size,  size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -0.5*size,  size) # left bottom
	
        # top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size,  0.5*size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size,  0.5*size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  0.5*size, -size) # right top 
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  0.5*size, -size) # left top

        # bottom
        #glTexCoord2f(texrep,0.0)
        #glVertex3f(-size, -0.5*size,  size) # right bottom
        #glTexCoord2f(texrep,texrep)
        #glVertex3f(-size, -0.5*size, -size) # right top
        #glTexCoord2f(0.0,texrep)
        #glVertex3f( size, -0.5*size, -size) # left top
        #glTexCoord2f(0.0,0.0)
        #glVertex3f( size, -0.5*size,  size) # left bottom

        glEnd()
        glDisable(GL_BLEND) # Disable Blending
        glEnable(GL_CULL_FACE)
        glTranslatef(-x,-y,-z)
		
    def DrawExplosionEdge(self, radius, texture, x, y, z):
        glTranslatef(x,y,z)
        q = gluNewQuadric() # Create A New Quadratic
 
        gluQuadricNormals(q, GL_SMOOTH) # Generate Smooth Normals For The Quad
        gluQuadricTexture(q, GL_TRUE) # Enable Texture Coords For The Quad

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
		
        #glColor4f(1.0, 1.0, 1.0, 0.4)
        
        glBindTexture(GL_TEXTURE_2D, texture) # Select Texture
        glEnable(GL_BLEND) # Enable Blending
        glBlendFunc(GL_SRC_ALPHA, GL_ONE) # Set Blending Mode To Mix Based On SRC Alpha
        glEnable(GL_TEXTURE_GEN_S) # Enable Sphere Mapping
        glEnable(GL_TEXTURE_GEN_T) # Enable Sphere Mapping

        gluSphere(q, radius, 32, 32) # Draw Sphere

        glDisable(GL_TEXTURE_GEN_S) # Disable Sphere Mapping
        glDisable(GL_TEXTURE_GEN_T) # Disable Sphere Mapping
        glDisable(GL_BLEND) # Disable Blending
        glTranslatef(-x,-y,-z)

    def DrawPowerUp(self, size, texrep, texture, rotation, x, y, z): 
        glTranslatef(x,y,z)
        glRotatef(rotation,0.0,1.0,0.0)
        glBindTexture(GL_TEXTURE_2D,texture)
        glBegin(GL_QUADS)
	
        # front
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size,  size) # left top

      	# back
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -size, -size) # left bottom
	
        # left
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -size, -size) # left bottom

        # right
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  size,  size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -size,  size) # left bottom
	
        # top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size,  size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size,  size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size, -size) # right top 
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size, -size) # left top

        # bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size, -size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size, -size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -size,  size) # left bottom

        glEnd()
        glTranslatef(-x,-y,-z) 			
		
    def DrawCube(self,size,texrep,texture,x,y,z):
        glTranslatef(x,y,z)
        glBindTexture(GL_TEXTURE_2D,texture)
        glBegin(GL_QUADS)
	
        # front
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size,  size) # left top

      	# back
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -size, -size) # left bottom
	
        # left
        glTexCoord2f(texrep,0.0)
        glVertex3f(-size, -size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f(-size,  size,  size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size, -size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size, -size, -size) # left bottom

        # right
        glTexCoord2f(texrep,0.0)
        glVertex3f( size, -size, -size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size, -size) # right top
        glTexCoord2f(0.0,texrep)
        glVertex3f( size,  size,  size) # left top
        glTexCoord2f(0.0,0.0)
        glVertex3f( size, -size,  size) # left bottom
	
        # top
        glTexCoord2f(0.0,0.0)
        glVertex3f(-size,  size,  size) # left bottom
        glTexCoord2f(texrep,0.0)
        glVertex3f( size,  size,  size) # right bottom
        glTexCoord2f(texrep,texrep)
        glVertex3f( size,  size, -size) # right top 
        glTexCoord2f(0.0,texrep)
        glVertex3f(-size,  size, -size) # left top

        # bottom
        #glTexCoord2f(texrep,0.0)
        #glVertex3f(-size, -size,  size) # right bottom
        #glTexCoord2f(texrep,texrep)
        #glVertex3f(-size, -size, -size) # right top
        #glTexCoord2f(0.0,texrep)
        #glVertex3f( size, -size, -size) # left top
        #glTexCoord2f(0.0,0.0)
        #glVertex3f( size, -size,  size) # left bottom

        glEnd()
        glTranslatef(-x,-y,-z)

    def DrawScreen(self):
        global rotation
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# Clear The Screen And The Depth Buffer
        glLoadIdentity() # Reset The matrix

        # To calculate our collision detection with the camera, it just takes one function
        # call from the client side.  We just pass in the vertices in the world that we
        # want to check, and then the vertex count.  
        # objCamera.CheckCameraCollision(g_vWorld, g_NumberOfVerts)

        # Assign Values to Local Variables to Prevent Long Lines Of Code	
        pos.x, pos.y, pos.z = objCamera.mPos.x, objCamera.mPos.y, objCamera.mPos.z
        view.x, view.y, view.z = objCamera.mView.x, objCamera.mView.y, objCamera.mView.z
        up.x, up.y, up.z = objCamera.mUp.x, objCamera.mUp.y, objCamera.mUp.z

        # use this function for opengl target camera
        gluLookAt(pos.x, pos.y, pos.z, view.x, view.y, view.z, up.x, up.y, up.z)
		
        glTranslatef(0.0, -40.0, 0.0)
        #self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor1"])
        #self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor2"])
        #self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor3"])
        #self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor4"])
        #self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor5"])
        self.DrawFloor(0.5*FLOOR_SIZE,FLOOR_TEXREP,self.textures["floor"])
        #self.DrawSky(2000, self.textures["sky"])
        self.DrawWallsPlanes(self.textures["wall"])
        #self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["crate"], 2.5*SQUARE_SIZE, 0.0, 2.5*SQUARE_SIZE)
        #self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["metal"], 2.5*SQUARE_SIZE, 0.0, 0.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_purple"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, -6.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_red"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, -4.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_black"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, -2.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_yellow"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, -0.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_green"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, 2.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_orange"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, 4.5*SQUARE_SIZE)
        self.DrawSphere(0.3*SQUARE_SIZE, self.textures["bm_blue"], 2.5*SQUARE_SIZE, -0.2*SQUARE_SIZE, 6.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_purple"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -7.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_purple"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -6.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_purple"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -5.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_red"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -4.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_blue"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -2.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_yellow"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, -0.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_green"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, 2.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_orange"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, 4.5*SQUARE_SIZE)
        self.DrawExplosionEdge(0.5*SQUARE_SIZE, self.textures["bomb_black"], 1.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, 6.5*SQUARE_SIZE)
        self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["crate"], 6.5*SQUARE_SIZE, 0.0, -2.5*SQUARE_SIZE)
        self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["metal"], 6.5*SQUARE_SIZE, 0.0, -0.5*SQUARE_SIZE)
        self.DrawSky(2000, 1, 0.5*FLOOR_SIZE, 0.0, 0.0)
        self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["metal"], 0.0, 0.0, 0.0)
        #self.DrawCube(0.5*SQUARE_SIZE, 1, self.textures["metal"], 2.5*SQUARE_SIZE, 0.0, 4.5*SQUARE_SIZE)
        self.DrawPowerUp(0.15*SQUARE_SIZE, 1, self.textures["gal5"], rotation, 2.5*SQUARE_SIZE, 0.0, -6.5*SQUARE_SIZE)
        #self.DrawPowerUp(0.15*SQUARE_SIZE, 1, self.textures["hard_box6"], rotation, 2.5*SQUARE_SIZE, 0.0, 6.5*SQUARE_SIZE)

        rotation = rotation + 0.6
        glTranslatef(0.0, 40.0, 0.0)
		
    def Go(self):
        pygame.mouse.set_visible(0)
        pygame.mouse.set_pos(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        while not self.done:
            for event in pygame.event.get(): # watch for events
                if event.type == QUIT: 
                    self.done = True
                elif event.type == KEYDOWN: # if a key is pressed
                    if event.key == K_ESCAPE: # escape key
                        self.done = True
                elif event.type == MOUSEMOTION:
                    objCamera.Mouse_Move(SCREEN_SIZE[0],SCREEN_SIZE[1])
						
            keystate = pygame.key.get_pressed() # get the pressed key
	  
            if keystate[K_w] and keystate[K_d]:
                objCamera.Move_Camera(sin(0.33*pi)*camera.CAMERASPEED)
                objCamera.Strafe_Camera(cos(0.33*pi)*camera.CAMERASPEED)
		
            elif keystate[K_w] and keystate[K_a]:
                objCamera.Move_Camera(sin(0.66*pi)*camera.CAMERASPEED)
                objCamera.Strafe_Camera(cos(0.66*pi)*camera.CAMERASPEED)
		
            elif keystate[K_s] and keystate[K_d]:
                objCamera.Move_Camera(sin(-0.33*pi)*camera.CAMERASPEED)
                objCamera.Strafe_Camera(cos(-0.33*pi)*camera.CAMERASPEED)
		
            elif keystate[K_s] and keystate[K_a]:
                objCamera.Move_Camera(sin(-0.66*pi)*camera.CAMERASPEED)
                objCamera.Strafe_Camera(cos(-0.66*pi)*camera.CAMERASPEED)
            # moving forward
            elif keystate[K_UP]: objCamera.Move_Camera(camera.CAMERASPEED)
            elif keystate[K_w]: objCamera.Move_Camera(camera.CAMERASPEED)
            # moving backward
            elif keystate[K_DOWN]: objCamera.Move_Camera(-camera.CAMERASPEED)
            elif keystate[K_s]: objCamera.Move_Camera(-camera.CAMERASPEED)
            # moving left
            elif keystate[K_LEFT]: objCamera.Strafe_Camera(-camera.CAMERASPEED)
            elif keystate[K_a]: objCamera.Strafe_Camera(-camera.CAMERASPEED)
            # moving right
            elif keystate[K_RIGHT]: objCamera.Strafe_Camera(camera.CAMERASPEED)
            elif keystate[K_d]: objCamera.Strafe_Camera(camera.CAMERASPEED)
	  
            self.DrawScreen() # draw the world
            pygame.display.flip()

    def LoadWorld(self,filename="world.txt"):
        try:
            f = open(filename)
            lines = f.readlines()
            for line in lines:
                self.board.append(line[:BOARD_SIZE])
            f.close()
            print self.board
        except:
            print "Error: Couldn't find test file '"+filename+"'."
            return

os.environ["SDL_VIDEO_CENTERED"] = "1" # Center the graphics window.
screen = pygame.display.set_mode(SCREEN_SIZE,DISPLAY_FLAGS)
pygame.display.set_caption("CubeLand v"+__version__)

glInit()
glEnable(GL_TEXTURE_2D)

bw = BlocksWorld()
bw.Go()
