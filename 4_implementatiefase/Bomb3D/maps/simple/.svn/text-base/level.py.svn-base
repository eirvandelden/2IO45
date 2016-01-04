# -*- coding: utf-8 -*-

import engine.placeables.hardwall as hardwall
import engine.placeables.softwall as softwall
import engine.placeables.bomb as bomb
import engine.placeables.explosion as explosion
import engine.placeables.bomberman as bomberman
import engine.placeables.powerup as powerup

import engine.scripts.bomberman as bombermanScript
import engine.scripts.bomb as bombScript
import engine.scripts.explosion as explosionScript
import engine.scripts.powerup as powerupScript
import engine.scripts.special as specialScript
import engine.scripts.quit as quitScript

class simple(object):
  
  def __init__(self):
    self.objectsUsed = ["hardwall", "softwall", "bomb", "explosion", "bomberman", "powerup"]
    self.size = dict(x=9*80,y=9*80) # 9 bij 9 vakjes van 80x80
  
  def createLevel(self, engine, players):   
    
    #Zet hardwalls neer rond het level
    self.initialState = []
    for x in range(9):
      self.initialState.append(hardwall.hardwall(engine, dict(x=(x * 80),y=(0)))) #Teken links 
      self.initialState.append(hardwall.hardwall(engine, dict(x=(x * 80),y=(8 * 80)))) #Teken boven
      if x != 0 and x != 8:
        self.initialState.append(hardwall.hardwall(engine, dict(x=(0), y=(x * 80)))) #Teken rechts
        self.initialState.append(hardwall.hardwall(engine, dict(x=(8 * 80), y=(x * 80)))) #Teken onder
    
    # Zet hardwalls ertussen
    for x in [2,4,6]:
      for y in [2,4,6]:
        self.initialState.append(hardwall.hardwall(engine, dict(x=(x * 80), y=(y * 80))))
    
    #lege blokjes1
    for x in [1,4,7]:
      for y in [3,5]:
        self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), ""))
        
    #lege blokjes1
    for x in [3,5]:
      for y in [1,4,7]:
        self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), ""))        
    
    #range upgrades
    x = 2
    y = 3
    self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), "range"))
    x = 5
    y = 4
    self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), "range"))
    
    #bomb upgrades
    x = 3
    y = 5
    self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), "bombs"))    
    x = 4
    y = 2    
    self.initialState.append(softwall.softwall(engine, dict(x=(x * 80), y=(y * 80)), "bombs"))
    
    # add bombermans
    bombermanspots = [dict(x=4*80, y=7*80), dict(x=7*80, y=4*80), dict(x=1*80, y=4*80), dict(x=4*80, y=1*80), dict(x=1*80, y=7*80), dict(x=7*80, y=1*80), dict(x=7*80, y=7*80), dict(x=1*80, y=1*80)]
    for player in players:
      player.addBomberman(engine, bombermanspots.pop())
      self.initialState.append(player.bomberman)

  def loadScripts(self, events):
    bombermanScript.init(events)
    bombScript.init(events)
    explosionScript.init(events)
    powerupScript.init(events)
    specialScript.init(events)
    quitScript.init(events)

