# -*- coding: utf-8 -*-

from engine import placeable

class special(placeable.placeable):
  
  ### available properties:
  # kind
  
  def __init__ (self, engine, coordinate, kind):
    super(special, self).__init__(engine)
    self.type = "special"
    self.kind = kind
    self.coordinate = dict(coordinate)
    self.direction = dict(x=1, y=0)
    self.velocity = dict(x=0, y=0)
    self.timelefttimer = float("infinity")
    self.boundingbox = dict(x=0, y=0, w=80, h=80)
    self.owner = None
    
    engine.loadModel(self, "special")
