# -*- coding: utf-8 -*-

#Import the classes we need
import engine.placeables.bomb
import engine.placeables.hardwall
import engine.placeables.softwall

import output.math3D as math3D
import math
import output.vector

# movement
movementSpeed = 4

class vector(object):
  def __init__(self, vector):
    self.x = vector['x']
    self.y = vector['y']
    self.z = 0
    
def recalcVelocity(MoveDirection, MoveSpeed, lookAtDirection):
  # correction
  standard_angle = math.asin(1)

  # hoek waarop we bewegen ten opzichte van de kijkrichting
  move_angle = math.acos(MoveDirection['x'])
  angle_determinant = math.asin(MoveDirection['y'])
  if (angle_determinant < 0):
    move_angle = - move_angle
  
  # hoek waarin we kijken
  cur_angle = math.acos(lookAtDirection['x'])
  angle_determinant = math.asin(lookAtDirection['y'])
  if (angle_determinant < 0):
    cur_angle = - cur_angle

  # totale hoek
  new_angle = -(move_angle + cur_angle + standard_angle)
    
  return dict(
    x=(math.cos(new_angle) * MoveSpeed), 
    y=(math.sin(new_angle) * MoveSpeed)
  )

# def move(gamestate, player, movementDirection):
def move(gamestate, player):
  way = {
    'f': dict(x=0, y=-1),
    'b': dict(x=0, y=1),
    'l': dict(x=-1, y=0),
    'r': dict(x=1, y=0),
  }
  
  if len(player.bomberman.move):
    player.bomberman.velocity = recalcVelocity(way[player.bomberman.move[-1]], movementSpeed, player.bomberman.direction)
  else:
    player.bomberman.velocity = dict(x=0, y=0)

def moveForward(gamestate, player):
  player.bomberman.move.append('f')
  move(gamestate, player)
  # move(gamestate, player, dict(x=0, y=-1))
  
def moveBack(gamestate, player):
  player.bomberman.move.append('b')
  move(gamestate, player)
  # move(gamestate, player, dict(x=0, y=1))
  
def moveLeft(gamestate, player):
  player.bomberman.move.append('l')
  move(gamestate, player)
  # move(gamestate, player, dict(x=-1, y=0))
  
def moveRight(gamestate, player):
  player.bomberman.move.append('r')
  move(gamestate, player)
  # move(gamestate, player, dict(x=1, y=0))
  
# def moveStop(gamestate, player):
#   player.bomberman.velocity = dict(x=0, y=0)

def moveForwardStop(gamestate, player):
  player.bomberman.move.remove('f')
  move(gamestate, player)

def moveBackStop(gamestate, player):
  player.bomberman.move.remove('b')
  move(gamestate, player)

def moveLeftStop(gamestate, player):
  player.bomberman.move.remove('l')
  move(gamestate, player)

def moveRightStop(gamestate, player):
  player.bomberman.move.remove('r')
  move(gamestate, player)

def mouseMove(gamestate, m, input_y, player):
  # hoek waarover we draaien
  rotate_angle = math.atan2(m, 100)
  
  # hoek waarnaar we kijken
  cur_angle = math.acos(player.bomberman.direction['x'])
  angle_determinant = math.asin(player.bomberman.direction['y'])
  if (angle_determinant < 0):
    cur_angle = - cur_angle
  
  # totale hoek
  new_angle = rotate_angle + cur_angle
  
  # update info
  player.bomberman.direction['x'] = math.cos(new_angle)
  player.bomberman.direction['y'] = math.sin(new_angle)
  
  move(gamestate, player)

#When a bomberman gets killed
def playerkilled(gamestate, bomberman, source):
  if bomberman.invincible:
    return
  
  #Update the killboard
  bomberman.owner.deaths = bomberman.owner.deaths + 1
  bomberman.owner.lives = bomberman.owner.lives - 1
  killer = source.owner
  if bomberman.owner != killer:
    killer.kills = killer.kills + 1
  
  #Remove the player from the playing field
  if bomberman.owner.lives < 1:
    bomberman.bombsinplay = float("inf") #TODO: mogelijk fixen als we gaan respawnen
    gamestate.placeables.remove(bomberman)
  else:
    bomberman.coordinate = bomberman.begincoordinate
    bomberman.direction = bomberman.begindirection
    gamestate.events.playerspawned.emit(bomberman)
    bomberman.invincible = True
    bomberman.timeleft(3)

#When a bomberman tries to walk into a hardwall
def bombermanVShardwall(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "bomberman":
    bomberman = obj1
    if obj2.type == "hardwall":
      bomb = obj2
    else:
      return
  elif obj1.type == "hardwall":
    bomb = obj1
    if obj2.type == "bomberman":
      bomberman = obj2
    else:
      return
  else:
    return
  
  bomberman.velocity = dict(x=0, y=0)
  bomberman.nextCoordinate = correctedPosition

#When a bomberman tries to walk into a softwall
def bombermanVSsoftwall(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "bomberman":
    bomberman = obj1
    if obj2.type == "softwall":
      bomb = obj2
    else:
      return
  elif obj1.type == "softwall":
    bomb = obj1
    if obj2.type == "bomberman":
      bomberman = obj2
    else:
      return
  else:
    return
  
  bomberman.velocity = dict(x=0, y=0)
  bomberman.nextCoordinate = correctedPosition

def invincibleTimeout(gamestate, bomberman):
  if bomberman.type != "bomberman":
    return
  bomberman.timelefttimer = float("inf")
  bomberman.invincible = False

def init(events):
  # movement
  events.eAcceForwOn.register(moveForward)
  events.eAcceBackOn.register(moveBack)
  events.eStepLeftOn.register(moveLeft)
  events.eStepRghtOn.register(moveRight)
  
  events.eAcceForwOff.register(moveForwardStop)
  events.eAcceBackOff.register(moveBackStop)
  events.eStepLeftOff.register(moveLeftStop)
  events.eStepRghtOff.register(moveRightStop)
  
  events.eMouseEvent.register(mouseMove)
  
  events.playerkilled.register(playerkilled)
  events.collision.register(bombermanVShardwall)
  events.collision.register(bombermanVSsoftwall)
  
  events.timeout.register(invincibleTimeout)
