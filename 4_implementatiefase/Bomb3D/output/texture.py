# -*- coding: utf-8 -*-
__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

# import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# import PyGame
import pygame
from pygame.locals import *
pygame.init()

def loadTextures(textures):
  images = os.listdir("output/textures") # get all files from the folder
  for image in images: # try to load each file
    try:
      loadTexture(image,image[:-4],textures)
    except:
      print "The filename '"+image+"' couldn't be loaded." 
	  
def loadTexture(filename, name, textures):
  filename = os.path.join("output/textures",filename) # get the file
  texture = pygame.image.load(filename) # load the image
  textures[name] = len(textures) # A texture number.
  texture_data = pygame.image.tostring(texture, "RGBX", 1 )
  glBindTexture(GL_TEXTURE_2D,len(textures)-1)
  if filename[-4:] == '.png':
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)

    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    glEnable(GL_BLEND)
    glEnable(GL_CULL_FACE)    
  else:
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    # texture settings
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    #glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
    #glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )