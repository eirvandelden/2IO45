# -*- coding: utf-8 -*-

__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

# import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# import additional modules
import os
import camera
import vector
import draw
import texture
import hud
import sound
import pygame
import math3D
import time

from math import pi
from pygame.locals import *

def initGraphics():
  pygame.init()

  # constants
  global SCREEN_SIZE
  SCREEN_SIZE = (1024,600) # screen size when not fullscreen
  global DISPLAY_FLAGS
  DISPLAY_FLAGS = OPENGL|DOUBLEBUF #|FULLSCREEN # display settings
  global INIT_DIRECTION
  INIT_DIRECTION = vector.tVector3(1.0, 0.0, 0.0) # inital bomberman direction

  # global variables
  global pos
  pos = vector.tVector3(0, 0, 0) # Position Vector Camera
  global view
  view = vector.tVector3(0, 0, 0) # View Vector Camera
  global up
  up = vector.tVector3(0, 0, 0) # Up Vector Camera
  global bdirection
  bdirection = vector.tVector3(0.0, 0.0, 0.0) # direction of bomberman
  global angle
  angle = 0.0 # angle for rotating the bomberman

  # dispplay settings
  os.environ["SDL_VIDEO_CENTERED"] = "1" # Center the graphics window.
  global screen
  screen = pygame.display.set_mode(SCREEN_SIZE,DISPLAY_FLAGS)
  pygame.display.set_caption("Bomb3D v"+__version__)

def glInit():
  glutInit()  # initialize the GLUT library.
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) # initial display mode
  glShadeModel(GL_SMOOTH) # Enable Smooth Shading
  glClearColor(0.0, 0.0, 0.0, 0.5) # Black Background
	
  glClearDepth(1.0) # Depth Buffer Setup
  glEnable(GL_DEPTH_TEST) # Enables Depth Testing
  glDepthFunc(GL_LEQUAL) # The Type Of Depth Testing To Do
  glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST) # Really Nice Perspective Calculations
	
  glViewport(0,0,SCREEN_SIZE[0],SCREEN_SIZE[1]) # Reset The Current Viewport
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
	
  # Calculate The Aspect Ratio Of The Window
  gluPerspective(45.0, SCREEN_SIZE[0]/SCREEN_SIZE[1], 0.1, 3000.0)
  glMatrixMode(GL_MODELVIEW)
	
  glCullFace(GL_BACK) # Don't draw the back sides of polygons
  glEnable(GL_CULL_FACE) # Turn on culling
  glEnable(GL_TEXTURE_2D) # Enable textures
  
class graphicalLevel():
  
  def __init__(self, player):
    global screen
    self.time = time.time()
    self.screen = screen # our screen
    self.textures = {} # for saving the textures
    self.camera = camera.CCamera()
    self.list = glGenLists(7) # display lists
    self.rotation = 0.0 # set rotation variable for rotation objects
    glInit() # initialize OpenGL and window
    texture.loadTextures(self.textures) # load all textures
    self.HUD = hud.HUD(self.textures) # The HUD
    self.player = player
    
  def initEvents(self, events):
    self.Sound = sound.Sound(events, self.player)

  def buildLists(self, gamestate):
    # build the display list for the floor and sky
    glNewList(self.list, GL_COMPILE)
    glPushMatrix()
    draw.drawFloor(gamestate, self.textures["floor"])
    #draw.drawSky(scale,self.textures["gal5"], self.textures["gal3"])
    glPopMatrix()
    glEndList()
  
    # build the display list for hard walls
    glNewList(self.list+1, GL_COMPILE)
    draw.drawCube(40, 1, self.textures["metal"])
    glEndList()
  
    # build the display list for the soft walls
    glNewList(self.list+2, GL_COMPILE) 
    draw.drawCube(40, 1, self.textures["crate"])
    glEndList()
	
    # build the display list for the powerups 	
    glNewList(self.list+3, GL_COMPILE) 
    draw.drawCube(12, 1, self.textures["powerup"])
    glEndList()

    # build the display list for the bombs 	
    glNewList(self.list+4, GL_COMPILE) 
    draw.drawBomb(12)
    glEndList()
	
    # build the display list for the bombermans
    glNewList(self.list+5, GL_COMPILE) 
    draw.drawBM(24)
    glEndList()
	
    # build the display list for the explosions
    glNewList(self.list+6, GL_COMPILE) 
    draw.drawExplosion(40)
    glEndList()
	
  def load(self, models):
    # models is een array met alle models die in dit level geladen worden.
    pass # doe niks
  
  def loadModel(self, placeable, model):
    # placeable is een object in het spel die als model "model" moet krijgen. Deze moet daar aan gekoppeld worden en placeable.model mag helemaal gebruikt worden hiervoor.
    pass # doe niks
  
  def draw(self, gamestate):
    curTime = time.time()
    self.frameTime = curTime - self.time
    self.time = curTime
    if self.frameTime != 0.0:
      print 1.0 / self.frameTime, " fps"
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# Clear The Screen And The Depth Buffer
    glLoadIdentity() # Reset The matrix
    # Assign Values to Local Variables to Prevent Long Lines Of Code
    pos.x, pos.y, pos.z = self.camera.mPos.x, self.camera.mPos.y, self.camera.mPos.z
    view.x, view.y, view.z = self.camera.mView.x, self.camera.mView.y, self.camera.mView.z
    up.x, up.y, up.z = self.camera.mUp.x, self.camera.mUp.y, self.camera.mUp.z

    # use this function for opengl target camera
    gluLookAt(pos.x, pos.y, pos.z, view.x, view.y, view.z, up.x, up.y, up.z)
	
    glTranslatef(0.0, -40.0, 0.0) # translate down
	
    glCallList(self.list) # draw the floor, walls, sky

    for placeable in gamestate.placeables: # draw all the placeables
      x = gamestate.level.size['x']
      y = gamestate.level.size['y']
      coord = draw.boardToLevelCoord(x, y, placeable.coordinate)
      if placeable.type == "powerup":
        glPushMatrix()
        glTranslate(coord.x, 40, coord.z)
        glRotatef(self.rotation, 0.0, 1.0, 0.0)
        glCallList(self.list+3)
        glPopMatrix()
		
      elif placeable.type == "hardwall":
        glPushMatrix()
        glTranslate(coord.x, 40, coord.z)
        glCallList(self.list+1)
        glPopMatrix()
	
      elif placeable.type == "softwall":
        glPushMatrix()
        glTranslate(coord.x, 40, coord.z)
        glCallList(self.list+2)
        glPopMatrix()
	
      elif placeable.type == "bomb":
        texture = "bomb_" + placeable.owner.color
        glPushMatrix()
        glTranslatef(coord.x, 32, coord.z)
        glBindTexture(GL_TEXTURE_2D, self.textures[texture])
        glCallList(self.list+4)
        glPopMatrix()
	  
      elif placeable.type == "explosion":
        texture = "bomb_" + placeable.owner.color
        glPushMatrix()
        glTranslatef(coord.x, 32, coord.z)
        glBindTexture(GL_TEXTURE_2D, self.textures[texture])
        glCallList(self.list+6)
        glPopMatrix()
		
      elif placeable.type == "bomberman":
        if placeable.owner == self.player: # set camera instead of bomberman model
          draw.setCamera(self, coord, placeable.direction)
        else: # draw bomberman model
          texture = "bm_" + placeable.owner.color
	      # calculate the angle for rotation: cos(angle) = ( u 'dot' v ) / ( ||u|| ||v|| )
          bdirection.x = placeable.direction['x']
          bdirection.z = placeable.direction['y']
          angle = math3D.AngleBetweenVectors(INIT_DIRECTION, bdirection) # angle in radians
          angle = angle * (360 / (2*pi)) # angle in degrees
          if bdirection.z < 0:
            angle = -angle
          glPushMatrix()
          glTranslatef(coord.x, 24, coord.z)
          glRotatef(angle, 0.0, 1.0, 0.0)
          glBindTexture(GL_TEXTURE_2D, self.textures[texture])
          glCallList(self.list+5)
          glPopMatrix()
      else:
        pass
 
    self.rotation = self.rotation + 0.8 # rotate
    glTranslatef(0.0, 40.0, 0.0) # translate up
        
    self.HUD.Draw_Mini_Map(gamestate)
    self.HUD.Draw_Power_Ups(self.player) # TODO: actual available powerups
    self.HUD.Draw_Stats(self.player)
    
    self.Sound.PlaySound(gamestate, self.player)
        
    pygame.display.flip()
