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
from math import pi, cos, sin, floor

pygame.init() # Initialize PyGame

# contants
SCREEN_SIZE = (1024,768)
MAP_SIZE = (5,5)
MAP_SCREEN_RATIO = 3;
DISPLAY_FLAGS = PyGLoc.OPENGL|PyGLoc.DOUBLEBUF
FILE_NAME = "World.raw"

MAP = []
MAP.append((1,1,1,1,1))
MAP.append((1,2,2,0,1))
MAP.append((1,2,1,0,1))
MAP.append((1,0,0,0,0))
MAP.append((1,1,1,1,1))

# player location: x,y,angle,color
PLAYERS = [(1.5,1.5,50,(255,0,0)),(6.5,7.5,280,(0,255,0))]

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
  OGL.glClearColor(0.0, 0.0, 0.0, 0.0) # Black Background
	
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

    # Auto-load all images in the graphics directory.
    self.textures = {}
    images = os.listdir(os.path.join("graphics","hud"))
    for image in images:
        try:
            self.LoadTexture(image,image[:-4])
        except:
            print "The filename '"+image+"' couldn't be loaded."
      
  def LoadTexture(self,filename,name):
    filename = os.path.join("graphics","hud",filename)
    texture = pygame.image.load(filename)
    self.textures[name] = len(self.textures) # A texture number.
    texture_data = pygame.image.tostring(texture, "RGBA", 1 )
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,len(self.textures)-1)
    OGL.glPixelStorei(OGL.GL_UNPACK_ALIGNMENT,1)

    OGL.glTexParameterf( OGL.GL_TEXTURE_2D, OGL.GL_TEXTURE_MIN_FILTER, OGL.GL_LINEAR )
    OGL.glTexParameterf( OGL.GL_TEXTURE_2D, OGL.GL_TEXTURE_MAG_FILTER, OGL.GL_LINEAR )
    OGL.glTexEnvf(OGL.GL_TEXTURE_ENV, OGL.GL_TEXTURE_ENV_MODE, OGL.GL_MODULATE)
    OGL.glBlendFunc(OGL.GL_SRC_ALPHA, OGL.GL_ONE_MINUS_SRC_ALPHA)
    OGL.glTexImage2D(OGL.GL_TEXTURE_2D, 0, OGL.GL_RGBA, texture.get_width(), texture.get_height(), 0, OGL.GL_RGBA, OGL.GL_UNSIGNED_BYTE, texture_data)
    
    OGL.glTexImage2D(OGL.GL_TEXTURE_2D, 0, OGL.GL_RGBA, texture.get_width(), texture.get_height(), 0, OGL.GL_RGBA, OGL.GL_UNSIGNED_BYTE, texture_data)

    OGL.glEnable(OGL.GL_BLEND)
    OGL.glEnable(OGL.GL_CULL_FACE)    
    
		
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
    
  def HudMode(self, flag):
    if flag:
      # 2d projection
      OGL.glMatrixMode(OGL.GL_PROJECTION)
      OGL.glPushMatrix()
      OGL.glLoadIdentity()

      OGLU.gluOrtho2D(0, SCREEN_SIZE[0], 0, SCREEN_SIZE[1])
      OGL.glMatrixMode(OGL.GL_MODELVIEW)
      OGL.glPushMatrix()
      OGL.glLoadIdentity()
      OGL.glDisable(OGL.GL_DEPTH_TEST)
    else:
      # 3d projection
      OGL.glMatrixMode(OGL.GL_PROJECTION)
      OGL.glPopMatrix()
      OGL.glMatrixMode(OGL.GL_MODELVIEW)
      OGL.glPopMatrix()
      OGL.glEnable(OGL.GL_DEPTH_TEST)
        
  def Draw_Mini_Map(self):
    # map size           
    map_height = floor(SCREEN_SIZE[1] / MAP_SCREEN_RATIO)
    map_width = floor(map_height / MAP_SIZE[1] * MAP_SIZE[0])
    
    # tile size
    tile_size = floor(map_height / MAP_SIZE[1])
    
    # map position on the screen
    map_x = floor((SCREEN_SIZE[0] - map_width) / 2) + (MAP_SIZE[0]*0.5*tile_size*0.04)
    
    OGL.glColor3ub(255,255,255)
            
    # draw all tiles
    for i in range(MAP_SIZE[0]):
      for j in range(MAP_SIZE[1]):
        if MAP[j][i] == 0:
          # soft wall texture
          OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["soft_wall"])
        elif MAP[j][i] == 1:
          # wall texture
          OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["wall"])
        else:
          # no wall texture
          OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["floor"])
        
        # draw tile
        OGL.glBegin(OGL.GL_QUADS)
        OGL.glTexCoord2d(0,0)
        OGL.glVertex2d(((map_x-(i*tile_size*0.04))+(i*tile_size)), map_height-((j+1)*tile_size)+(j*tile_size*0.04))
        OGL.glTexCoord2d(1,0)
        OGL.glVertex2d(((map_x-(i*tile_size*0.04))+((i+1)*tile_size)), map_height-((j+1)*tile_size)+(j*tile_size*0.04))
        OGL.glTexCoord2d(1,1)
        OGL.glVertex2d(((map_x-(i*tile_size*0.04))+((i+1)*tile_size)), map_height-(j*tile_size)+(j*tile_size*0.04))
        OGL.glTexCoord2d(0,1)
        OGL.glVertex2d(((map_x-(i*tile_size*0.04))+(i*tile_size)), map_height-(j*tile_size)+(j*tile_size*0.04))
        OGL.glEnd()
        
    # draw players
    player_size = 18;
    for player in PLAYERS:
      OGL.glColor3ub(player[3][0],player[3][1],player[3][2])
      OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["player"])
      OGL.glPushMatrix();
      OGL.glTranslatef(map_x+(player[0]*tile_size),map_height-(player[1]*tile_size),0)
      OGL.glRotatef(player[2], 0, 0, 1.0)
      OGL.glBegin(OGL.GL_QUADS)
      OGL.glTexCoord2d(0,0)
      OGL.glVertex2d(-(player_size/2),-(player_size/2))
      OGL.glTexCoord2d(1,0)
      OGL.glVertex2d((player_size/2),-(player_size/2))
      OGL.glTexCoord2d(1,1)
      OGL.glVertex2d((player_size/2),(player_size/2))
      OGL.glTexCoord2d(0,1)
      OGL.glVertex2d(-(player_size/2),(player_size/2))
      OGL.glEnd()
      OGL.glPopMatrix();
      
    OGL.glColor3ub(255,255,255)
      
  def Draw_Stats(self):    
    # score
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_score"])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-74))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-74))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-10))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-10))
    OGL.glEnd()
    # score value
    score = 5
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str(score)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-58))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-58))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-26))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-26))
    OGL.glEnd()
    
    # bombs
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_bomb"])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-138))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-138))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-74))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-74))
    OGL.glEnd()
    # bombs value
    bombs = 8
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str(bombs)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-122))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-122))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-90))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-90))
    OGL.glEnd()
    
    # range
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_range"])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-202))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-202))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(74,(SCREEN_SIZE[1]-138))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(10,(SCREEN_SIZE[1]-138))
    OGL.glEnd()
    # range value
    range = 0
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str(range)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-186))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-186))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(58,(SCREEN_SIZE[1]-154))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(26,(SCREEN_SIZE[1]-154))
    OGL.glEnd()
    
  def Draw_Time(self, seconds):
    time_x = (SCREEN_SIZE[0] / 2) - 40
    
    # floor ( (seconds / 60) / 10 )
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str(seconds/600)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(time_x,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(time_x+32,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(time_x+32,SCREEN_SIZE[1])
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(time_x,SCREEN_SIZE[1])
    OGL.glEnd()
    
    # (seconds / 60) mod 10
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str((seconds/60) % 10)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(time_x+14,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(time_x+46,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(time_x+46,SCREEN_SIZE[1])
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(time_x+14,SCREEN_SIZE[1])
    OGL.glEnd()
    
    # time colon
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_colon"])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(time_x+24,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(time_x+56,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(time_x+56,SCREEN_SIZE[1])
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(time_x+24,SCREEN_SIZE[1])
    OGL.glEnd()
    
    # floor ( (seconds % 60) / 10 )
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str((seconds % 60)/10)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(time_x+35,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(time_x+67,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(time_x+67,SCREEN_SIZE[1])
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(time_x+35,SCREEN_SIZE[1])
    OGL.glEnd()
    
    # seconds mod 10
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures["icon_label_" + str(seconds % 10)])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d(time_x+49,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d(time_x+81,SCREEN_SIZE[1]-32)
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d(time_x+81,SCREEN_SIZE[1])
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d(time_x+49,SCREEN_SIZE[1])
    OGL.glEnd()
    
  def Draw_Power_Ups(self,powerups):
    i = 0
    for powerup in powerups:
      # power-up
      OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures[powerup])
      OGL.glBegin(OGL.GL_QUADS)
      OGL.glTexCoord2d(0,0)
      OGL.glVertex2d((SCREEN_SIZE[0]-74),(SCREEN_SIZE[1]-74-(64*i)))
      OGL.glTexCoord2d(1,0)
      OGL.glVertex2d((SCREEN_SIZE[0]-10),(SCREEN_SIZE[1]-74-(64*i)))
      OGL.glTexCoord2d(1,1)
      OGL.glVertex2d((SCREEN_SIZE[0]-10),(SCREEN_SIZE[1]-10-(64*i)))
      OGL.glTexCoord2d(0,1)
      OGL.glVertex2d((SCREEN_SIZE[0]-74),(SCREEN_SIZE[1]-10-(64*i)))
      OGL.glEnd()
      i = i + 1
      
  def Draw_Menu(self):
    OGL.glBindTexture(OGL.GL_TEXTURE_2D,self.textures['icon_mine'])
    OGL.glBegin(OGL.GL_QUADS)
    OGL.glTexCoord2d(0,0)
    OGL.glVertex2d((10),(10))
    OGL.glTexCoord2d(1,0)
    OGL.glVertex2d((SCREEN_SIZE[0]-10),(10))
    OGL.glTexCoord2d(1,1)
    OGL.glVertex2d((SCREEN_SIZE[0]-10),(SCREEN_SIZE[1]-10))
    OGL.glTexCoord2d(0,1)
    OGL.glVertex2d((10),(SCREEN_SIZE[1]-10))
    OGL.glEnd()
    
  def GUI(self):
    self.HudMode(True)
    
    OGL.glEnable(OGL.GL_TEXTURE_2D)
    self.Draw_Mini_Map()
    self.Draw_Stats()
    self.Draw_Power_Ups(("icon_mine","icon_new_crate"))
    self.Draw_Time(300)
    self.Draw_Menu()
    OGL.glDisable(OGL.GL_TEXTURE_2D)
    
    self.HudMode(False)
		
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
      self.GUI()
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