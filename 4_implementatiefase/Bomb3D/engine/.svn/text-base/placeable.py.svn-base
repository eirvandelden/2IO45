# -*- coding: utf-8 -*-

import math

class placeable(object):

  ### available properties:
  # type
  # coordinate
  # nextcoordinate
  # direction: een vector met lengte 1 (dict(x=1, y=0))
  # model
  # timeleft
  # velocity: een vector
  # owner
  # boundingbox
  
  def __init__(self, engine):
    self.nextCoordinate = None;
    self.engine = engine
  
  def timeleft(self, sec):
    self.timelefttimer = math.floor(sec * self.engine.gamestate.framerate)
