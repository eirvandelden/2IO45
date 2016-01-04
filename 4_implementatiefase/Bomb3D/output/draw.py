# -*- coding: utf-8 -*-

__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

import vector
import math3D
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import acos, pi

# constants
SQUARE_SIZE = 80 # size of a square on the board

def boardToLevelCoord(width, length, coordinate):
  coord = vector.tVector3(0.0, 0.0, 0.0) # create a new vector
  xzero = -0.5*width + 0.5*SQUARE_SIZE # 3D x-coordinate for 2D coordinate x = 0
  zzero = (0.5*length - 0.5*SQUARE_SIZE) # 3D z-coordinate for 2D coordinate y = 0
  toAdd = vector.tVector3(xzero + (coordinate['x'] ), 0.0, zzero - (coordinate['y'] ))
  coord = coord + toAdd
  return coord
  
def setCamera(graph, coordinate, direction):
  pos = vector.tVector3(0.0, 0.0, 0.0)
  view = vector.tVector3(0.0, 0.0, 0.0)
  up = vector.tVector3(0.0, 1.0, 0.0)
  
  pos.x = coordinate.x - 25*direction['x']
  pos.y = 4.0
  pos.z = coordinate.z - 25*direction['y']
  
  view.x = coordinate.x + direction['x']
  view.y = 4.0
  view.z = coordinate.z + direction['y']
  
  graph.camera.Position_Camera(pos.x, pos.y, pos.z, view.x, view.y, view.z, up.x, up.y, up.z)
  
def drawFloor(gamestate, texture):
  # calculate the actual width and length, and the number of texture repetitions
  x = 0.5 * gamestate.level.size['x']
  xtexrep = (2*x) / SQUARE_SIZE
  y = 0.5 * gamestate.level.size['y']
  ytexrep = (2*y) / SQUARE_SIZE
  
  glBindTexture(GL_TEXTURE_2D,texture)
  glBegin(GL_QUADS)
  glTexCoord2f(0.0,0.0); glVertex3f(-x,0.0,y) # left front
  glTexCoord2f(ytexrep,0.0); glVertex3f(x,0.0,y) # right front
  glTexCoord2f(ytexrep,xtexrep); glVertex3f(x,0.0,-y) # right back
  glTexCoord2f(0.0,xtexrep); glVertex3f(-x,0.0,-y) # left back
  glEnd()
  
def drawWalls(gamestate, texture):
  xwidth = 0.5 * gamestate.level.size['x']
  xtexrep = (2*xwidth) / SQUARE_SIZE
  height = 0.5*SQUARE_SIZE
  ywidth = 0.5 * gamestate.level.size['y']
  ytexrep = (2*ywidth) / SQUARE_SIZE
  
  glTranslatef(0.0, height, -ywidth)
  glBindTexture(GL_TEXTURE_2D,texture)
	
  # draw the back wall
  glBegin(GL_QUADS)
  glTexCoord2f(0.0,0.0); glVertex3f(-xwidth, -height,  0.0) # left bottom
  glTexCoord2f(xtexrep,0.0); glVertex3f( xwidth, -height,  0.0) # right bottom
  glTexCoord2f(xtexrep,1.0); glVertex3f( xwidth,  height,  0.0) # right top
  glTexCoord2f(0.0,1.0); glVertex3f(-xwidth,  height,  0.0) # left top
  glEnd()
		
  # draw the right wall
  glTranslatef(xwidth, 0.0, ywidth)
  glBegin(GL_QUADS)
  glTexCoord2f(0.0,0.0); glVertex3f(0.0, -height,  -ywidth) # left bottom
  glTexCoord2f(ytexrep,0.0); glVertex3f(0.0, -height,  ywidth) # right bottom
  glTexCoord2f(ytexrep,1.0); glVertex3f(0.0,  height,  ywidth) # right top
  glTexCoord2f(0.0,1.0); glVertex3f(0.0,  height,  -ywidth) # left top
  glEnd()
		
  # draw the front wall
  glTranslatef(-xwidth, 0.0, ywidth)
  glBegin(GL_QUADS)
  glTexCoord2f(0.0,0.0); glVertex3f(xwidth, -height,  0.0) # left bottom
  glTexCoord2f(xtexrep,0.0); glVertex3f(-xwidth, -height,  0.0) # right bottom
  glTexCoord2f(xtexrep,1.0); glVertex3f(-xwidth,  height,  0.0) # right top
  glTexCoord2f(0.0,1.0); glVertex3f(xwidth,  height,  0.0) # left top
  glEnd()
		
  # draw the left wall
  glTranslatef(-xwidth, 0.0, -ywidth)
  glBegin(GL_QUADS)
  glTexCoord2f(0.0,0.0); glVertex3f(0.0, -height,  ywidth) # left bottom
  glTexCoord2f(ytexrep,0.0); glVertex3f(0.0, -height,  -ywidth) # right bottom
  glTexCoord2f(ytexrep,1.0); glVertex3f(0.0,  height,  -ywidth) # right top
  glTexCoord2f(0.0,1.0); glVertex3f(0.0,  height,  ywidth) # left top
  glEnd()

def drawSky(scale, texture1, texture2):
  glDisable(GL_CULL_FACE) # Turn off culling

  glScalef(scale*3000,scale*3000,scale*3000) # large size
  
  # right
  glBindTexture(GL_TEXTURE_2D, texture1)
  glBegin(GL_QUADS)
  glTexCoord2f(1,1); glVertex3f(1,1,1) 
  glTexCoord2f(0,1); glVertex3f(1,1,-1) 
  glTexCoord2f(0,0); glVertex3f(1,-1,-1) 
  glTexCoord2f(1,0); glVertex3f(1,-1,1) 
              
  # left	
  glTexCoord2f(0,0); glVertex3f(-1,-1,1) 
  glTexCoord2f(1,0); glVertex3f(-1,-1,-1) 
  glTexCoord2f(1,1); glVertex3f(-1,1,-1) 
  glTexCoord2f(0,1); glVertex3f(-1,1,1) 
  
  # front
  glTexCoord2f(0,0); glVertex3f(1,-1,1) 
  glTexCoord2f(1,0); glVertex3f(-1,-1,1) 
  glTexCoord2f(1,1); glVertex3f(-1,1,1) 
  glTexCoord2f(0,1); glVertex3f(1,1,1) 
  glEnd()

  # back
  glBindTexture(GL_TEXTURE_2D, texture2)
  glBegin(GL_QUADS)
  glTexCoord2f(1,1); glVertex3f(1,1,-1) 
  glTexCoord2f(0,1); glVertex3f(-1,1,-1) 
  glTexCoord2f(0,0); glVertex3f(-1,-1,-1) 
  glTexCoord2f(1,0); glVertex3f(1,-1,-1) 
  glEnd()  

  glEnable(GL_CULL_FACE) # Turn on culling
  
def drawExplosion(radius):
  glDisable(GL_CULL_FACE) # Turn off culling

  q = gluNewQuadric() # Create A New Quadratic
 
  gluQuadricNormals(q, GL_SMOOTH) # Generate Smooth Normals For The Quad
  gluQuadricTexture(q, GL_TRUE) # Enable Texture Coords For The Quad

  glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
  glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
		
  glEnable(GL_BLEND) # Enable Blending
  glBlendFunc(GL_SRC_ALPHA, GL_ONE) # Set Blending Mode To Mix Based On SRC Alpha
  glEnable(GL_TEXTURE_GEN_S) # Enable Sphere Mapping
  glEnable(GL_TEXTURE_GEN_T) # Enable Sphere Mapping

  gluSphere(q, radius, 32, 32) # Draw Sphere

  glDisable(GL_TEXTURE_GEN_S) # Disable Sphere Mapping
  glDisable(GL_TEXTURE_GEN_T) # Disable Sphere Mapping

  glEnable(GL_CULL_FACE) # Turn on culling
  
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  
def drawBomb(radius):
  q = gluNewQuadric() # Create A New Quadratic
 
  gluQuadricNormals(q, GL_SMOOTH) # Generate Smooth Normals For The Quad
  gluQuadricTexture(q, GL_TRUE) # Enable Texture Coords For The Quad
  glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
  glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP) # Set Up Sphere Mapping
		
  glEnable(GL_TEXTURE_GEN_S) # Enable Sphere Mapping
  glEnable(GL_TEXTURE_GEN_T) # Enable Sphere Mapping

  gluSphere(q, radius, 32, 32) # Draw Sphere

  glDisable(GL_TEXTURE_GEN_S) # Disable Sphere Mapping
  glDisable(GL_TEXTURE_GEN_T) # Disable Sphere Mapping
  
def drawBM(radius):
  q = gluNewQuadric() # Create A New Quadratic
 
  gluQuadricNormals(q, GL_SMOOTH) # Generate Smooth Normals For The Quad
  gluQuadricTexture(q, GL_TRUE) # Enable Texture Coords For The Quad
  gluQuadricDrawStyle( q, GLU_FILL)
  gluQuadricOrientation( q, GLU_OUTSIDE)

  gluSphere(q, radius, 32, 32) # Draw Sphere
	
def drawPowerUp(size, texrep, texture):
  glBindTexture(GL_TEXTURE_2D,texture)
  glBegin(GL_QUADS)
	
  # front
  glTexCoord2f(0.0,0.0); glVertex3f(-size, -size,  size) # left bottom
  glTexCoord2f(texrep,0.0); glVertex3f( size, -size,  size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f( size,  size,  size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f(-size,  size,  size) # left top

  # back
  glTexCoord2f(texrep,0.0); glVertex3f(-size, -size, -size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f(-size,  size, -size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f( size,  size, -size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f( size, -size, -size) # left bottom

  # left
  glTexCoord2f(texrep,0.0); glVertex3f(-size, -size,  size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f(-size,  size,  size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f(-size,  size, -size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f(-size, -size, -size) # left bottom

  # right
  glTexCoord2f(texrep,0.0); glVertex3f( size, -size, -size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f( size,  size, -size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f( size,  size,  size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f( size, -size,  size) # left bottom

  # top
  #glTexCoord2f(0.0,0.0); glVertex3f(-size,  size,  size) # left bottom
  #glTexCoord2f(texrep,0.0); glVertex3f( size,  size,  size) # right bottom
  #glTexCoord2f(texrep,texrep); glVertex3f( size,  size, -size) # right top 
  #glTexCoord2f(0.0,texrep); glVertex3f(-size,  size, -size) # left top

  # bottom
  #glTexCoord2f(texrep,0.0); glVertex3f(-size, -size,  size) # right bottom
  #glTexCoord2f(texrep,texrep); glVertex3f(-size, -size, -size) # right top
  #glTexCoord2f(0.0,texrep); glVertex3f( size, -size, -size) # left top
  #glTexCoord2f(0.0,0.0); glVertex3f( size, -size,  size) # left bottom

  glEnd()
		
def drawCube(size,texrep,texture):
  glBindTexture(GL_TEXTURE_2D,texture)
  glBegin(GL_QUADS)
	
  # front
  glTexCoord2f(0.0,0.0); glVertex3f(-size, -size,  size) # left bottom
  glTexCoord2f(texrep,0.0); glVertex3f( size, -size,  size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f( size,  size,  size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f(-size,  size,  size) # left top

  # back
  glTexCoord2f(texrep,0.0); glVertex3f(-size, -size, -size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f(-size,  size, -size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f( size,  size, -size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f( size, -size, -size) # left bottom
	
  # left
  glTexCoord2f(texrep,0.0); glVertex3f(-size, -size,  size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f(-size,  size,  size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f(-size,  size, -size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f(-size, -size, -size) # left bottom

  # right
  glTexCoord2f(texrep,0.0); glVertex3f( size, -size, -size) # right bottom
  glTexCoord2f(texrep,texrep); glVertex3f( size,  size, -size) # right top
  glTexCoord2f(0.0,texrep); glVertex3f( size,  size,  size) # left top
  glTexCoord2f(0.0,0.0); glVertex3f( size, -size,  size) # left bottom

  # top
  #glTexCoord2f(0.0,0.0); glVertex3f(-size,  size,  size) # left bottom
  #glTexCoord2f(texrep,0.0); glVertex3f( size,  size,  size) # right bottom
  #glTexCoord2f(texrep,texrep); glVertex3f( size,  size, -size) # right top 
  #glTexCoord2f(0.0,texrep); glVertex3f(-size,  size, -size) # left top

  # bottom
  #glTexCoord2f(texrep,0.0); glVertex3f(-size, -size,  size) # right bottom
  #glTexCoord2f(texrep,texrep); glVertex3f(-size, -size, -size) # right top
  #glTexCoord2f(0.0,texrep); glVertex3f( size, -size, -size) # left top
  #glTexCoord2f(0.0,0.0); glVertex3f( size, -size,  size) # left bottom

  glEnd()