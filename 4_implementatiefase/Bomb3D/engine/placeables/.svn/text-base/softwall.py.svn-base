# -*- coding: utf-8 -*-

from engine import placeable

class softwall(placeable.placeable):
  
  ### available properties:
  # none
  def __init__(self, engine, coordinate, powerup):
    super(softwall, self).__init__(engine)
    self.type = "softwall"
    self.coordinate = dict(coordinate)
    self.direction = dict(x=1, y=0)
    self.velocity = dict(x=0, y=0)
    self.timelefttimer = float("infinity")
    self.owner = None
    self.boundingbox = dict(x=0, y=0, w=80, h=80)
    self.powerup = powerup
    
    engine.loadModel(self, "softwall");
