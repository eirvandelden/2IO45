# -*- coding: utf-8 -*-

class gamestate():
  
  ### available properties:
  # players: the players in the game (not the bombermans)
  # level: the level object
  # placeables: array of all objects currently in the game
  # time: the ingame time
  # events: all the events that can be registered and emitted
  # framerate
  # engine: the game engine
  
  def __init__(self, engine, level, players, events, framerate, time):
    self.engine = engine
    self.level = level
    self.placeables = level.initialState
    self.players = players
    self.events = events
    self.framerate = framerate
    self.time = time

