# -*- coding: utf-8 -*-

import placeables.bomberman

class player(object):
  
  ### available properties:
  # UUID
  # score
  # kills
  # deaths
  # lives
  # bomberman
  # bombtype
  # color
  
  def __init__(self, UUID, color, startingLives):
    self.UUID = UUID
    self.color = color
    self.lives = startingLives
    self.score = 0
    self.kills = 0
    self.deaths = 0
    self.bombtype = "normal"
  
  def addBomberman(self, engine, coordinate):
    self.bomberman = placeables.bomberman.bomberman(engine, self, coordinate)
