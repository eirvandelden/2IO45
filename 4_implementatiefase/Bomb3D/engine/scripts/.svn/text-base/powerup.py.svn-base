# -*- coding: utf-8 -*-

# TODO:
# - Write the pickuphandler
# - Check imports

import engine.placeables.bomberman

#When a player walks over an upgrade
def pickup(gamestate, obj1, obj2, correctedPosition):
  if obj1.type == "bomberman":
    bomberman = obj1
    if obj2.type == "powerup":
      powerup = obj2
    else:
      return
  elif obj2.type == "bomberman":
    bomberman = obj2
    if obj1.type == "powerup":
      powerup = obj1
    else:
      return
  else:
    return
  
  if powerup.kind == "bombs":
    bomberman.totalbombs = bomberman.totalbombs + 1
  elif powerup.kind == "range":
    bomberman.range = bomberman.range + 1
  
  gamestate.placeables.remove(powerup)

  gamestate.events.poweruppickup.emit()

def init(events):
  events.collision.register(pickup)
