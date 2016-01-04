# -*- coding: utf-8 -*-

from engine import placeable

class powerup(placeable.placeable):
  
  ### available properties:
  # kind
  
  def __init__(self, engine, coordinate, kind, explosion):
    super(powerup, self).__init__(engine)
    self.type = "powerup"
    self.kind = kind
    self.coordinate = dict(coordinate)
    self.direction = dict(x=1, y=0)
    self.velocity = dict(x=0, y=0)
    self.timelefttimer = float("infinity")
    self.boundingbox = dict(x=15, y=15, w=50, h=50)
    self.owner = None
    self.explosion = explosion
    
    engine.loadModel(self, "powerup");
