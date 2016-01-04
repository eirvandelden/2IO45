# -*- coding: utf-8 -*-

import game

class tournament():
  ### available properties:
  # ListOfPlayers: the players in the game
  # TotalPlayerScores: an array with the total scores per player
  
  def __init__(self, players, totalplayerscores):
    self.players = players
    self.totalplayerscores = totalplayerscores