# -*- coding: utf-8 -*-

from engine import placeable

class explosion(placeable.placeable):
  
  ### available properties:
  # owner
  
  def __init__(self, engine, owner, coordinate, direction, range, timeleft):
    super(explosion, self).__init__(engine)
    self.owner  = owner
    self.type   = "explosion"
    self.coordinate = dict(coordinate)
    self.direction  = dict(direction)
    self.range = range
    self.timeleft(timeleft)
    self.channel    = -1 #for sound
    self.velocity = dict(x=0, y=0)
    self.boundingbox = dict(x=5, y=5, w=70, h=70)
    self.phase = 1
    
    engine.loadModel(self, "explosion")
