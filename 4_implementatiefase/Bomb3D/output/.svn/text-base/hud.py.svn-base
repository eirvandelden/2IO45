__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import floor, pi

import math3D
import vector
import pygame
pygame.init()

SCREEN_SIZE = (640,480) # screen size when not fullscreen
SQUARE_SIZE = 80
MAP_SCREEN_RATIO = 3;
INIT_DIRECTION = vector.tVector3(0.0, 1.0, 0.0) # inital bomberman direction

# global variables
bdirection = vector.tVector3(0.0, 0.0, 0.0) # direction of bomberman
angle = 0.0

class HUD(): # The HUD
  def __init__(self, textures):
    self.visuals = textures
    
  def Draw_Mini_Map(self, gamestate):
    self.HudMode(True)
    # map size           
    real_map_width = float(gamestate.level.size['x'])
    real_map_height = float(gamestate.level.size['y'])
    relative_map_width = gamestate.level.size['x'] / SQUARE_SIZE
    relative_map_height = gamestate.level.size['y'] / SQUARE_SIZE
    
    map_height = float(SCREEN_SIZE[1] / MAP_SCREEN_RATIO)
    map_width = map_height / relative_map_height * relative_map_width
    
    # tile size
    tile_size = map_height / relative_map_height
    player_size = tile_size * 0.6
    
    # map position on the screen
    map_x = (SCREEN_SIZE[0] - map_width) / 2.0
            
    # floor
    glBindTexture(GL_TEXTURE_2D, self.visuals["map_floor"])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(map_x, 0)
    glTexCoord2d(relative_map_width,0)
    glVertex2d(map_x + map_width, 0)
    glTexCoord2d(relative_map_width,relative_map_height)
    glVertex2d(map_x + map_width, map_height)
    glTexCoord2d(0,relative_map_height)
    glVertex2d(map_x, map_height)
    glEnd()
    
    for placeable in gamestate.placeables:
      item_x = placeable.coordinate['x'] / SQUARE_SIZE * tile_size
      item_y = placeable.coordinate['y'] / SQUARE_SIZE * tile_size
      
      if placeable.type == "hardwall":
        # wall texture
        glBindTexture(GL_TEXTURE_2D,self.visuals["map_wall"])
      elif placeable.type == "softwall":
        # wall texture
        glBindTexture(GL_TEXTURE_2D,self.visuals["map_soft_wall"])
      elif placeable.type == "explosion":
        glBindTexture(GL_TEXTURE_2D,self.visuals["map_explosion"])
        
      if placeable.type == "hardwall" or placeable.type == "softwall" or placeable.type == "explosion":
        # draw tile
        glBegin(GL_QUADS)
        glTexCoord2d(0,0)
        glVertex2d(map_x + item_x, item_y)
        glTexCoord2d(1,0)
        glVertex2d(map_x + (item_x + tile_size), item_y)
        glTexCoord2d(1,1)
        glVertex2d(map_x + (item_x + tile_size), item_y + tile_size)
        glTexCoord2d(0,1)
        glVertex2d(map_x + item_x, item_y + tile_size)
        glEnd()
      
      if placeable.type == "bomberman":
        # draw player
        texture = "map_player_icon_" + placeable.owner.color
        glBindTexture(GL_TEXTURE_2D,self.visuals[texture])
        glPushMatrix();
        glTranslatef(map_x + item_x + tile_size / 2.0, item_y + tile_size / 2.0, 0)
        bdirection.x = placeable.direction['x']
        bdirection.y = placeable.direction['y']
        angle = math3D.AngleBetweenVectors(INIT_DIRECTION, bdirection) # angle in radians
        angle = angle * (360.0 / (2*pi)) # angle in degrees
        if bdirection.x < 0:
          angle = - angle
        angle = angle + 180
        glRotatef(angle, 0, 0, 1.0) # rotate around z-axis
        glBegin(GL_QUADS)
        glTexCoord2d(0,0)
        glVertex2d(-1 * player_size / 2, -1 * player_size / 2)
        glTexCoord2d(1,0)
        glVertex2d(player_size / 2, -1 * player_size / 2)
        glTexCoord2d(1,1)
        glVertex2d(player_size / 2, player_size / 2)
        glTexCoord2d(0,1)
        glVertex2d(-1 * player_size / 2, player_size / 2)
        glEnd()
        glPopMatrix();

    self.HudMode(False)
        
  def Draw_Stats(self, player):
    self.HudMode(True)
    score = player.kills - player.deaths
    bombs = min(player.bomberman.totalbombs, 9)
    range = min(player.bomberman.range, 9)
    
    # score
    glBindTexture(GL_TEXTURE_2D,self.visuals["icon_score"])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(10,(SCREEN_SIZE[1]-74))
    glTexCoord2d(1,0)
    glVertex2d(74,(SCREEN_SIZE[1]-74))
    glTexCoord2d(1,1)
    glVertex2d(74,(SCREEN_SIZE[1]-10))
    glTexCoord2d(0,1)
    glVertex2d(10,(SCREEN_SIZE[1]-10))
    glEnd()
    
    # score value    
    if abs(score) > 9:
      glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_" + str(int(abs(score)/10))])
      glBegin(GL_QUADS)
      glTexCoord2d(0,0)
      glVertex2d(19,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,0)
      glVertex2d(51,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,1)
      glVertex2d(51,(SCREEN_SIZE[1]-26))
      glTexCoord2d(0,1)
      glVertex2d(19,(SCREEN_SIZE[1]-26))
      glEnd()
      glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_" + str(abs(score)%10)])
      glBegin(GL_QUADS)
      glTexCoord2d(0,0)
      glVertex2d(33,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,0)
      glVertex2d(65,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,1)
      glVertex2d(65,(SCREEN_SIZE[1]-26))
      glTexCoord2d(0,1)
      glVertex2d(33,(SCREEN_SIZE[1]-26))
      glEnd()
      if player.kills < player.deaths:
        glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_min"])
        glBegin(GL_QUADS)
        glTexCoord2d(0,0)
        glVertex2d(8,(SCREEN_SIZE[1]-58))
        glTexCoord2d(1,0)
        glVertex2d(40,(SCREEN_SIZE[1]-58))
        glTexCoord2d(1,1)
        glVertex2d(40,(SCREEN_SIZE[1]-26))
        glTexCoord2d(0,1)
        glVertex2d(8,(SCREEN_SIZE[1]-26))
        glEnd()
    else:
      glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_" + str(abs(score))])
      glBegin(GL_QUADS)
      glTexCoord2d(0,0)
      glVertex2d(26,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,0)
      glVertex2d(58,(SCREEN_SIZE[1]-58))
      glTexCoord2d(1,1)
      glVertex2d(58,(SCREEN_SIZE[1]-26))
      glTexCoord2d(0,1)
      glVertex2d(26,(SCREEN_SIZE[1]-26))
      glEnd()
      if player.kills < player.deaths:
        glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_min"])
        glBegin(GL_QUADS)
        glTexCoord2d(0,0)
        glVertex2d(14,(SCREEN_SIZE[1]-58))
        glTexCoord2d(1,0)
        glVertex2d(46,(SCREEN_SIZE[1]-58))
        glTexCoord2d(1,1)
        glVertex2d(46,(SCREEN_SIZE[1]-26))
        glTexCoord2d(0,1)
        glVertex2d(14,(SCREEN_SIZE[1]-26))
        glEnd()
      
    
    # bombs
    glBindTexture(GL_TEXTURE_2D,self.visuals["icon_bomb"])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(10,(SCREEN_SIZE[1]-138))
    glTexCoord2d(1,0)
    glVertex2d(74,(SCREEN_SIZE[1]-138))
    glTexCoord2d(1,1)
    glVertex2d(74,(SCREEN_SIZE[1]-74))
    glTexCoord2d(0,1)
    glVertex2d(10,(SCREEN_SIZE[1]-74))
    glEnd()
    
    # bombs value
    glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_" + str(bombs)])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(26,(SCREEN_SIZE[1]-122))
    glTexCoord2d(1,0)
    glVertex2d(58,(SCREEN_SIZE[1]-122))
    glTexCoord2d(1,1)
    glVertex2d(58,(SCREEN_SIZE[1]-90))
    glTexCoord2d(0,1)
    glVertex2d(26,(SCREEN_SIZE[1]-90))
    glEnd()
    
    if player.bomberman.totalbombs > 9:
      glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_plus"])
      glBegin(GL_QUADS)
      glTexCoord2d(0,0)
      glVertex2d(46,(SCREEN_SIZE[1]-122))
      glTexCoord2d(1,0)
      glVertex2d(78,(SCREEN_SIZE[1]-122))
      glTexCoord2d(1,1)
      glVertex2d(78,(SCREEN_SIZE[1]-90))
      glTexCoord2d(0,1)
      glVertex2d(46,(SCREEN_SIZE[1]-90))
      glEnd()
    
    # range
    glBindTexture(GL_TEXTURE_2D,self.visuals["icon_range"])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(10,(SCREEN_SIZE[1]-202))
    glTexCoord2d(1,0)
    glVertex2d(74,(SCREEN_SIZE[1]-202))
    glTexCoord2d(1,1)
    glVertex2d(74,(SCREEN_SIZE[1]-138))
    glTexCoord2d(0,1)
    glVertex2d(10,(SCREEN_SIZE[1]-138))
    glEnd()
    
    # range value
    glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_" + str(range)])
    glBegin(GL_QUADS)
    glTexCoord2d(0,0)
    glVertex2d(26,(SCREEN_SIZE[1]-186))
    glTexCoord2d(1,0)
    glVertex2d(58,(SCREEN_SIZE[1]-186))
    glTexCoord2d(1,1)
    glVertex2d(58,(SCREEN_SIZE[1]-154))
    glTexCoord2d(0,1)
    glVertex2d(26,(SCREEN_SIZE[1]-154))
    glEnd()
    
    if player.bomberman.range > 9:
      glBindTexture(GL_TEXTURE_2D,self.visuals["icon_label_plus"])
      glBegin(GL_QUADS)
      glTexCoord2d(0,0)
      glVertex2d(41,(SCREEN_SIZE[1]-186))
      glTexCoord2d(1,0)
      glVertex2d(73,(SCREEN_SIZE[1]-186))
      glTexCoord2d(1,1)
      glVertex2d(73,(SCREEN_SIZE[1]-154))
      glTexCoord2d(0,1)
      glVertex2d(41,(SCREEN_SIZE[1]-154))
      glEnd()
    self.HudMode(False)
    
  def Draw_Power_Ups(self, player):
    self.HudMode(True)
    #i = 0
    #for powerup in powerups:
    #  # power-up
    #  glBindTexture(GL_TEXTURE_2D,self.visuals[powerup])
    #  glBegin(GL_QUADS)
    #  glTexCoord2d(0,0)
    #  glVertex2d((SCREEN_SIZE[0]-74),(SCREEN_SIZE[1]-74-(64*i)))
    #  glTexCoord2d(1,0)
    #  glVertex2d((SCREEN_SIZE[0]-10),(SCREEN_SIZE[1]-74-(64*i)))
    #  glTexCoord2d(1,1)
    #  glVertex2d((SCREEN_SIZE[0]-10),(SCREEN_SIZE[1]-10-(64*i)))
    #  glTexCoord2d(0,1)
    #  glVertex2d((SCREEN_SIZE[0]-74),(SCREEN_SIZE[1]-10-(64*i)))
    #  glEnd()
    #  i = i + 1
    self.HudMode(False) 
      
  def HudMode(self, flag):
    if flag:
      # 2d projection
      glMatrixMode(GL_PROJECTION)
      glPushMatrix()
      glLoadIdentity()

      gluOrtho2D(0, SCREEN_SIZE[0], 0, SCREEN_SIZE[1])
      glMatrixMode(GL_MODELVIEW)
      glPushMatrix()
      glLoadIdentity()
      glDisable(GL_DEPTH_TEST)
    else:
      # 3d projection
      glMatrixMode(GL_PROJECTION)
      glPopMatrix()
      glMatrixMode(GL_MODELVIEW)
      glPopMatrix()
      glEnable(GL_DEPTH_TEST)