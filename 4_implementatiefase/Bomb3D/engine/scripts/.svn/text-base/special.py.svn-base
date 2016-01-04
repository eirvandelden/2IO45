# -*- coding: utf-8 -*-

# Staying empty until we have time to add special tiles

import engine.placeables.softwall

def init(events):
  events.ePowerup1On.register(placeSoftwall)

def placeSoftwall(gamestate, player):
  bomberman = player.bomberman
  
  coordinate = dict(x=int((bomberman.coordinate['x']+40)/80)*80, y=int((bomberman.coordinate['y']+40)/80)*80)
  softwall = engine.placeables.softwall.softwall(gamestate.engine, coordinate, None)
  
  gamestate.placeables.append(softwall)