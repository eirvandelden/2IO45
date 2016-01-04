# -*- coding: utf-8 -*-

from engine import placeable

class bomberman(placeable.placeable):
  
  ### available properties:
  # range
  # totalbombs
  # bombsinplay
  # bombtype
  # move
  # Functions 
  
  def __init__ (self, engine, owner, coordinate):
    super(bomberman, self).__init__(engine)
    self.type = "bomberman"
    self.coordinate = dict(coordinate)
    self.direction  = dict(x=1, y=0)
    self.begincoordinate = dict(coordinate)
    self.begindirection  = dict(x=1, y=0)
    self.timelefttimer   = float("inf")
    self.owner      = owner
    self.velocity   = dict(x=0, y=0)
    self.range      = 1
    self.totalbombs = 1
    self.bombsinplay = 0
    self.bombtype = "normal"
    self.boundingbox = dict(x=25, y=25, w=30, h=30)
    self.move = []
    self.invincible = False
    engine.loadModel(self, "bomberman")
  
  def increase_range(self):
    """Increase the range of the bombs of this player"""
    self.range = self.range + 1
  
  def decrease_range(self):
    """Decrease the range of the bombs of this player, but not lower than 1 """
    if range > 1:
      self.range = self.range - 1
    else:
      pass
    
  def increase_totalbomb(self):
    """Increase the total number of bombs of this player"""
    self.totalbombs = self.totalbombs + 1
    
  def decrease_totalbomb(self):
    """Decrease the total number of bombs of this player"""
    if self.totalbombs > 1:
      self.totalbombs = self.totalbombs - 1
    else:
      pass
  
