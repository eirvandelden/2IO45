# -*- coding: utf-8 -*-

#Import the classes we need
import engine.placeables.explosion 

#Placing a bomb
def placebomb(gamestate, player): # these arguments are still open for discussion
  bomberman = player.bomberman
  
  #Check if a bomb can be set down
  if bomberman.bombsinplay >= bomberman.totalbombs:
    return
  
  #Increase the number of bombs in play
  bomberman.bombsinplay = bomberman.bombsinplay + 1
  coordinate = dict(x=int((bomberman.coordinate['x']+40)/80)*80, y=int((bomberman.coordinate['y']+40)/80)*80)
  
  bomb = engine.placeables.bomb.bomb(gamestate.engine, bomberman.owner, bomberman.range, "normal", bomberman.bombtype, coordinate, 5)
  
  gamestate.placeables.append(bomb)

#Exploding a bomb.
def explode(gamestate, bomb):
  #Check correct call
  if bomb.type != "bomb":
    return
  
  bomb.owner.bomberman.bombsinplay = bomb.owner.bomberman.bombsinplay - 1
  
  #Create an explosion on the spot of this bomb
  explosion = engine.placeables.explosion.explosion(gamestate.engine, bomb.owner, bomb.coordinate, dict(x=0, y=0), bomb.range, 0.5)
  gamestate.placeables.append(explosion)
  
  gamestate.events.bombexplode.emit(bomb.coordinate, bomb.range)
  
  #Remove the bomb that has just exploded
  gamestate.placeables.remove(bomb)


#When a bomberman tries to walk into a bomb
def bombermanVSbomb(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "bomberman":
    bomberman = obj1
    if obj2.type == "bomb":
      bomb = obj2
    else:
      return
  elif obj2.type == "bomberman":
    bomberman = obj2
    if obj1.type == "bomb":
      bomb = obj1
    else:
      return
  else:
    return
  
  bomberman.velocity = dict(x=0, y=0)
  bomberman.nextCoordinate = correctedPosition

def init(events):
  events.timeout.register(explode)
  events.collision.register(bombermanVSbomb)
  events.eDropBombOn.register(placebomb)
