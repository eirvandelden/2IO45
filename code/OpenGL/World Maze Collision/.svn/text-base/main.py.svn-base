# OpenGL
import OpenGL.GL as OGL
import OpenGL.GLU as OGLU
import OpenGL.GLUT as OGLUT

import os # Needed to set the screen in the middle when not in fullscreen
import sys # system routines
import camera # Module For The Camera
import vector # For the 3D vector
import pygame # For mouse, keyboard and screen
import pygame.locals as PyGLoc
from math import pi, cos, sin

pygame.init() # Initialize PyGame

# contants
SCREEN_SIZE = (640,480)
DISPLAY_FLAGS = PyGLoc.OPENGL|PyGLoc.DOUBLEBUF|PyGLoc.FULLSCREEN
FILE_NAME = "World.raw"

# global variables
objCamera = camera.CCamera() # Our Camera
pos = vector.tVector3(0, 0, 0) # Vector Camera Position
view = vector.tVector3(0, 0, 0) # View Vector Camera
up = vector.tVector3(0, 0, 0) # Up Vector Camera
g_vWorld = [] # Array containing all the triangles our world consists of
g_NumberOfVerts = 0 # Number of vertices used in our world

# Load the vertices specified in our world file
def LoadVertices():
  global g_NumberOfVerts
  # This function reads in the vertices from an ASCII text file (World.raw).
  # First, we read in the vertices with a temp CVector3 to get the number of them.
  # Next, we rewind the file pointer and then actually read in the vertices into
  # our allocated CVector3 array g_vWorld[].

  # Create a file and load the model from a file of vertices
  fp = open(FILE_NAME, "r")

  # Read in the vertices that are stored in the file
  arr = []
  for line in fp.readlines(): # Read line after line
    arr.append(map(float, line.split())) # Map the vertices into a 2-dim array
    new = vector.tVector3(arr[g_NumberOfVerts][0], arr[g_NumberOfVerts][1], arr[g_NumberOfVerts][2])
    g_vWorld.append(new)
    g_NumberOfVerts = g_NumberOfVerts + 1									 
  # Close our file because we are done
  fp.close()

def glInit():
  OGLUT.glutInit()  # initialize the GLUT library.
  OGLUT.glutInitDisplayMode(OGLUT.GLUT_DOUBLE | OGLUT.GLUT_RGB |OGLUT.GLUT_DEPTH) # initial display mode
  OGL.glShadeModel(OGL.GL_SMOOTH) # Enable Smooth Shading
  OGL.glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
	
  OGL.glClearDepth(1.0) # Depth Buffer Setup
  OGL.glEnable(OGL.GL_DEPTH_TEST) # Enables Depth Testing
  OGL.glDepthFunc(OGL.GL_LEQUAL) # The Type Of Depth Testing To Do
  OGL.glHint(OGL.GL_PERSPECTIVE_CORRECTION_HINT, OGL.GL_NICEST) # Really Nice Perspective Calculations
	
  objCamera.Position_Camera(10, 4, 12,   9, 4, 12,   0, 1, 0) # Set Camera Position
	
  LoadVertices()
	
  OGL.glViewport(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]) # Reset The Current Viewport
  OGL.glMatrixMode(OGL.GL_PROJECTION)
  OGL.glLoadIdentity()
	
  # Calculate The Aspect Ratio Of The Window
  OGLU.gluPerspective(45.0, SCREEN_SIZE[0]/SCREEN_SIZE[1], 0.1, 100.0)
  OGL.glMatrixMode(OGL.GL_MODELVIEW)
	
  OGL.glCullFace(OGL.GL_BACK) # Don't draw the back sides of polygons
  OGL.glEnable(OGL.GL_CULL_FACE) # Turn on culling

  #OGL.glFogi(OGL.GL_FOG_MODE, OGL.GL_EXP2) # Set The Fog Mode
  #OGL.glFogfv(OGL.GL_FOG_COLOR, [0.0, 0.0, 0.0, 1.0]) # Set The Fog Color
  #OGL.glFogf(OGL.GL_FOG_DENSITY, 0.011) # Set How Dense Will The Fog Be
  #OGL.glHint(OGL.GL_FOG_HINT, OGL.GL_DONT_CARE) # Set The Fog's calculation accuracy
  #OGL.glFogf(OGL.GL_FOG_START, 0) # Set The Fog's Start Depth
  #OGL.glFogf(OGL.GL_FOG_END, 50.0) # Set The Fog's End Depth
  #OGL.glEnable(OGL.GL_FOG) # Enable fog (turn it on)
	
class World():	
  def __init__(self):
    global screen
    self.screen = screen
    self.done = False
		
  def Draw_Grid(self):
    for i in range(-500, 501, 5):
      OGL.glBegin(OGL.GL_LINES)
      OGL.glColor3ub(150, 190, 150)
      OGL.glVertex3f(-500, 0, i)
      OGL.glVertex3f(500, 0, i)
      OGL.glVertex3f(i, 0, -500)
      OGL.glVertex3f(i, 0, 500)
      OGL.glEnd()
		
  def DrawScreen(self):
    OGL.glClear(OGL.GL_COLOR_BUFFER_BIT | OGL.GL_DEPTH_BUFFER_BIT)	# Clear The Screen And The Depth Buffer
    OGL.glLoadIdentity() # Reset The matrix

    # To calculate our collision detection with the camera, it just takes one function
    # call from the client side.  We just pass in the vertices in the world that we
    # want to check, and then the vertex count.  
    objCamera.CheckCameraCollision(g_vWorld, g_NumberOfVerts)

    # Assign Values to Local Variables to Prevent Long Lines Of Code	
    pos.x, pos.y, pos.z = objCamera.mPos.x, objCamera.mPos.y, objCamera.mPos.z
    view.x, view.y, view.z = objCamera.mView.x, objCamera.mView.y, objCamera.mView.z
    up.x, up.y, up.z = objCamera.mUp.x, objCamera.mUp.y, objCamera.mUp.z

    # use this function for opengl target camera
    OGLU.gluLookAt(pos.x, pos.y, pos.z, view.x, view.y, view.z, up.x, up.y, up.z)

    # Since we have the vertices for the world in the correct order, let's create
    # a loop that goes through all of the vertices and passes them in to be rendered.

    OGL.glBegin(OGL.GL_TRIANGLES)
    # Go through all the vertices and draw them
    for i in range(0,g_NumberOfVerts,3):
      OGL.glColor3ub(i, 2*i, 3*i) # All different colors to see the structure while playing
      OGL.glVertex3f(g_vWorld[i].x, g_vWorld[i].y, g_vWorld[i].z)
      OGL.glVertex3f(g_vWorld[i+1].x, g_vWorld[i+1].y, g_vWorld[i+1].z)
      OGL.glVertex3f(g_vWorld[i+2].x, g_vWorld[i+2].y, g_vWorld[i+2].z)
				
    OGL.glEnd()
    #OGL.glPopMatrix() 
		
  def Go(self):
    pygame.mouse.set_visible(0)
    pygame.mouse.set_pos(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
    while not self.done:
      for event in pygame.event.get(): # watch for events
        if event.type == PyGLoc.QUIT: 
          self.done = True
        elif event.type == PyGLoc.KEYDOWN: # if a key is pressed
          if event.key == PyGLoc.K_ESCAPE: # escape key
            self.done = True
        elif event.type == PyGLoc.MOUSEMOTION:
          objCamera.Mouse_Move(SCREEN_SIZE[0],SCREEN_SIZE[1])
						
      keystate = pygame.key.get_pressed() # get the pressed key
	  
      if keystate[PyGLoc.K_w] and keystate[PyGLoc.K_d]:
        objCamera.Move_Camera(sin(0.33*pi)*camera.CAMERASPEED)
        objCamera.Strafe_Camera(cos(0.33*pi)*camera.CAMERASPEED)
		
      elif keystate[PyGLoc.K_w] and keystate[PyGLoc.K_a]:
        objCamera.Move_Camera(sin(0.66*pi)*camera.CAMERASPEED)
        objCamera.Strafe_Camera(cos(0.66*pi)*camera.CAMERASPEED)
		
      elif keystate[PyGLoc.K_s] and keystate[PyGLoc.K_d]:
        objCamera.Move_Camera(sin(-0.33*pi)*camera.CAMERASPEED)
        objCamera.Strafe_Camera(cos(-0.33*pi)*camera.CAMERASPEED)
		
      elif keystate[PyGLoc.K_s] and keystate[PyGLoc.K_a]:
        objCamera.Move_Camera(sin(-0.66*pi)*camera.CAMERASPEED)
        objCamera.Strafe_Camera(cos(-0.66*pi)*camera.CAMERASPEED)
      # moving forward
      elif keystate[PyGLoc.K_UP]: objCamera.Move_Camera(camera.CAMERASPEED)
      elif keystate[PyGLoc.K_w]: objCamera.Move_Camera(camera.CAMERASPEED)
      # moving backward
      elif keystate[PyGLoc.K_DOWN]: objCamera.Move_Camera(-camera.CAMERASPEED)
      elif keystate[PyGLoc.K_s]: objCamera.Move_Camera(-camera.CAMERASPEED)
      # moving left
      elif keystate[PyGLoc.K_LEFT]: objCamera.Strafe_Camera(-camera.CAMERASPEED)
      elif keystate[PyGLoc.K_a]: objCamera.Strafe_Camera(-camera.CAMERASPEED)
      # moving right
      elif keystate[PyGLoc.K_RIGHT]: objCamera.Strafe_Camera(camera.CAMERASPEED)
      elif keystate[PyGLoc.K_d]: objCamera.Strafe_Camera(camera.CAMERASPEED)
	  
      self.DrawScreen() # draw the world
      pygame.display.flip()
		
if __name__ == '__main__':
  # init screen
  os.environ["SDL_VIDEO_CENTERED"] = "1" # Center the graphics window.
  screen = pygame.display.set_mode(SCREEN_SIZE,DISPLAY_FLAGS) # Setup screen
  pygame.display.set_caption("World PyGame") # Screen title
    
  # init GL
  glInit()  # Initialize all OpenGL settings
    
  mw = World()
  mw.Go() # Launch our world