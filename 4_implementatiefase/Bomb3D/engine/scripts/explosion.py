# -*- coding: utf-8 -*-

import engine.placeables.bomb

#Removing an explosion
def removeExplode(gamestate, explosion):
  if explosion.type != "explosion":
    return
  
  if explosion.phase == 1:
    if explosion.range != 0:

      map = []
      
      for i in range(gamestate.level.size['y'] / 80):
        map.append([])
        for j in range(gamestate.level.size['x'] / 80): 
        # all nodes are ready initially
          map[i].append(0)
      
      for placeable in gamestate.placeables:
        if placeable.type == "softwall":
          map[int(placeable.coordinate['y'] / 80)][int(placeable.coordinate['x'] / 80)] = 1
        elif placeable.type == "hardwall":
          map[int(placeable.coordinate['y'] / 80)][int(placeable.coordinate['x'] / 80)] = 2
      
      explosion_x = int(explosion.coordinate['x'] / 80)
      explosion_y = int(explosion.coordinate['y'] / 80)
      
      if explosion.direction == dict(x=0, y=0):
        for direction in [dict(x=1, y=0), dict(x=-1, y=0), dict(x=0, y=1), dict(x=0, y=-1)]:
          x = direction['x']
          y = direction['y']
          if map[explosion_x+x][explosion_y+y] == 1:
            expl_range = 0
          else:
            expl_range = explosion.range - 1
            
          if map[explosion_x+x][explosion_y+y] != 2:
            newCoordinate = dict(x=explosion.coordinate['x'] + x * 80, y=explosion.coordinate['y'] + y * 80)
            newExplosion = engine.placeables.explosion.explosion(gamestate.engine, explosion.owner, newCoordinate, dict(x=x, y=y), expl_range, 0.5)
            gamestate.placeables.append(newExplosion)
      else:
        x = explosion.direction['x']
        y = explosion.direction['y']
        if map[explosion_x+x][explosion_y+y] == 1:
          expl_range = 0
        else:
          expl_range = explosion.range - 1
          
        if map[explosion_x+x][explosion_y+y] != 2:
          newCoordinate = dict(x=explosion.coordinate['x'] + x * 80, y=explosion.coordinate['y'] + y * 80)
          newExplosion = engine.placeables.explosion.explosion(gamestate.engine, explosion.owner, newCoordinate, dict(x=x, y=y), explosion.range - 1, 0.5)
          gamestate.placeables.append(newExplosion)
    explosion.phase = 2
    explosion.timeleft(1)
  else:
    gamestate.placeables.remove(explosion)

#When a explosion hits a bomberman
def explosionVSbomberman(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "explosion":
    explosion = obj1
    if obj2.type == "bomberman":
      bomberman = obj2
    else:
      return
  elif obj2.type == "explosion":
    explosion = obj2
    if obj1.type == "bomberman":
      bomberman = obj1
    else:
      return
  else:
    return
    
  gamestate.events.playerkilled.emit(gamestate, bomberman, explosion)

#When an explosion and a bomb collide
def explosionVSbomb(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "explosion":
    explosion = obj1
    if obj2.type == "bomb":
      bomb = obj2
    else:
      return
  elif obj2.type == "explosion":
    explosion = obj2
    if obj1.type == "bomb":
      bomb = obj1
    else:
      return
  else:
    return
  
  bomb.owner = explosion.owner
  bomb.timelefttimer = 1

#When an explosion and a powerup collide
def explosionVSpowerup(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "explosion":
    explosion = obj1
    if obj2.type == "powerup":
      powerup = obj2
    else:
      return
  elif obj2.type == "explosion":
    explosion = obj2
    if obj1.type == "powerup":
      powerup = obj1
    else:
      return
  else:
    return
  
  if explosion != powerup.explosion:
    gamestate.placeables.remove(powerup)

#When an explosion and a powerup collide
def explosionVSsoftwall(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "explosion":
    explosion = obj1
    if obj2.type == "softwall":
      softwall = obj2
    else:
      return
  elif obj2.type == "explosion":
    explosion = obj2
    if obj1.type == "softwall":
      softwall = obj1
    else:
      return
  else:
    return
  
  if (softwall.powerup != ''):
    powerup = engine.placeables.powerup.powerup(gamestate.engine, softwall.coordinate, softwall.powerup, explosion)
    gamestate.placeables.append(powerup)
  gamestate.placeables.remove(softwall)

def init(events):
  events.collision.register(explosionVSbomb)
  events.collision.register(explosionVSbomberman)
  events.collision.register(explosionVSpowerup)
  events.collision.register(explosionVSsoftwall)
  events.timeout.register(removeExplode)
