# -*- coding: utf-8 -*-

from engine import placeable

class bomb(placeable.placeable):
  
  ### available properties:
  # range
  # owner
  # kind
  
  def __init__(self, engine, owner, range, type, kind, coordinate, timeleft):
    super(bomb, self).__init__(engine)
    self.type  = "bomb"
    self.kind  = kind
    self.owner = owner
    self.range = range
    self.coordinate = dict(coordinate)
    self.direction  = dict(x=1, y=0)
    self.velocity   = dict(x=0, y=0)
    self.timeleft(timeleft)
    self.boundingbox = dict(x=25, y=25, w=30, h=30)
	
    engine.loadModel(self, "bomb_" + owner.color)
  