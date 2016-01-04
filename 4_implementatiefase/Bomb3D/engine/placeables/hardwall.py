# -*- coding: utf-8 -*-

from engine import placeable

class hardwall(placeable.placeable):
  
  ### available properties:
  # none
  
  def __init__(self, engine, coordinate):
    super(hardwall, self).__init__(engine)
    self.type = "hardwall"
    self.coordinate = dict(coordinate)
    self.direction  = dict(x=1, y=0)
    self.velocity   = dict(x=0, y=0)
    self.timelefttimer   = float("infinity")
    self.owner      = None
    self.boundingbox = dict(x=0, y=0, w=80, h=80)
	
    engine.loadModel(self, "hardwall");
