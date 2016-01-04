# -*- coding: utf-8 -*-

import gamestate
import event
import tournament
import testqhandlers
import math

class engine():
  
  ### available properties:
  # gamestate
  # graphics
  
  def __init__(self, graphics, level, players, inputqueue, options):

    self.graphics = graphics
    self.inputqueue = inputqueue
    graphics.load(level.objectsUsed)
    # initialize events
    events = event.events()
    events.token = event.event("token") #arguments: none
    events.timeout = event.event("timeout") # arguments: gamestate, object that timed out
    events.collision = event.event("collision") # arguments: gamestate, object1, object2
    events.playerkilled = event.event("playerkilled") # arguments: gamestate, bomberman, explosion
    events.playerspawned = event.event("playerspawned") # arguments: bomberman
    events.bombexplode = event.event("bombexplode") # arguments: bombcoordinate, bombrange
    events.poweruppickup = event.event("poweruppickup") # arguments: bombcoordinate, bombrange
    
    events.eMouseEvent = event.event("eMouseEvent")
    
    # emits as data: the message as a string, player_id as an integer.
    events.eChtMessage = event.event("eChtMessage")
    
    # these all emit as data: player_id as an integer.
    events.eAcceForwOn = event.event("eAcceForwOn")
    events.eAcceBackOn = event.event("eAcceBackOn")
    events.eStepLeftOn = event.event("eStepLeftOn")
    events.eStepRghtOn = event.event("eStepRghtOn")
    events.eDropBombOn = event.event("eDropBombOn")
    events.ePowerup1On = event.event("ePowerup1On")
    events.ePowerup2On = event.event("ePowerup2On")
    events.ePowerup3On = event.event("ePowerup3On")
    events.eMinimapTOn = event.event("eMinimapTOn")
    
    events.eAcceForwOff = event.event("eAcceForwOff")
    events.eAcceBackOff = event.event("eAcceBackOff")
    events.eStepLeftOff = event.event("eStepLeftOff")
    events.eStepRghtOff = event.event("eStepRghtOff")
    events.eDropBombOff = event.event("eDropBombOff")
    events.ePowerup1Off = event.event("ePowerup1Off")
    events.ePowerup2Off = event.event("ePowerup2Off")
    events.ePowerup3Off = event.event("ePowerup3Off")
    events.eMinimapTOff = event.event("eMinimapTOff")
    
    events.eNeatQuit = event.event("eNeatQuit")
    
    events.token.register(engine.play)
    
    time = options.get("time", 120) #TODO: tijd (timeleft in dit geval dacht ik) goed regelen
    
    level.createLevel(self, players)
    level.loadScripts(events)
    self.graphics.initEvents(events)
    
    self.gamestate = gamestate.gamestate(self, level, players, events, 10, time) #TODO: framerate fixen
    graphics.buildLists(self.gamestate)
    
    self.inputqueuehandler = testqhandlers.QReaderEventWriter(inputqueue, self.gamestate)
    
    # start the mainloop
    #self.play()
  
  def play(self): #TODO: input is tijdelijk om te testen
    self.updategamestate()
    self.graphics.draw(self.gamestate)
  
  def updategamestate(self):
    # decrease timers
    for placeable in self.gamestate.placeables:
      placeable.timelefttimer = placeable.timelefttimer - 1
      if placeable.timelefttimer <= 0:
        self.gamestate.events.timeout.emit(self.gamestate, placeable)
    
    # check for collisions
    self.collisions()
    
    # move objects
    for placeable in self.gamestate.placeables:
      if placeable.velocity == dict(x=0, y=0):
        continue
      #TODO: aanzetten als corrected position berekenen weer werkt!
      #if placeable.nextCoordinate != None:
        #placeable.coordinate = placeable.nextCoordinate
        #placeable.nextCoordinate = None
      else:
        placeable.coordinate['x'] = placeable.coordinate['x'] + placeable.velocity['x']
        placeable.coordinate['y'] = placeable.coordinate['y'] + placeable.velocity['y']

  
  
  def loadModel(self, object, model):
    self.graphics.loadModel(object, model)
  
  
  def collisions(self):
    for placeable in self.gamestate.placeables:
      if (placeable.type == "bomberman" or
          placeable.type == "explosion"):
        self.collisionOneObject(placeable)
  
  def collisionOneObject(self, movingObject):
    for placeable in self.gamestate.placeables:
      if placeable == movingObject:
        continue
      self.collisionTwoObjects(movingObject, placeable)
  
  
  def collisionTwoObjects(self, movingObject, otherObject):
    x1 = movingObject.coordinate['x'] + movingObject.boundingbox['x']
    y1 = movingObject.coordinate['y'] + movingObject.boundingbox['y']
    w1 = movingObject.boundingbox['w']
    l1 = movingObject.boundingbox['h']
    vx = movingObject.velocity['x']
    vy = movingObject.velocity['y']
    
    x2 = otherObject.coordinate['x']
    y2 = otherObject.coordinate['y']
    w2 = otherObject.boundingbox['w']
    l2 = otherObject.boundingbox['h']
    
    collision = 0
    
    # if we have intersection of x-coordinates 1
    if x1 + vx <= x2 and x1 + vx + w1 > x2:
      # if we have intersection of y-coordinates 1
      if y1 + vy <= y2 and y1 + vy + l1 > y2:
        collision = 1
      # if we have intersection of y-coordinates 2
      elif y1 + vy > y2 and y2 + l2 > y1 + vy:
        collision = 1
    
    # if we have intersection of x-coordinates 2
    elif x1 + vx > x2 and x2 + w2 > x1 + vx:
      # if we have intersection of y-coordinates 1
      if y2 <= y1 + vy and y2 + l2 > y1 + vy:
        collision = 1
      # if we have intersection of y-coordinates 2
      elif y2 > y1 + vy and y1 + vy + l1 > y2:
        collision = 1
    
    if (collision == 1 and movingObject.type == "bomberman"):
      # if we already where in a collision state, don't count it as one
      # if we have intersection of x-coordinates 1
      if x1 <= x2 and x1 + w1 > x2:
        # if we have intersection of y-coordinates 1
        if y1 <= y2 and y1 + l1 > y2:
          collision = 0
        # if we have intersection of y-coordinates 2
        elif y1 > y2 and y2 + l2 > y1:
          collision = 0
      
      # if we have intersection of x-coordinates 2
      elif x1 > x2 and x2 + w2 > x1:
        # if we have intersection of y-coordinates 1
        if y2 <= y1 and y2 + l2 > y1:
          collision = 0
        # if we have intersection of y-coordinates 2
        elif y2 > y1 and y1 + l1 > y2:
          collision = 0
    
    # correction
    #TODO: dit is nog stuk!!!
    correctionx, correctiony = 0, 0
    if collision == 1:
      if vx != 0:
        c = vy / vx	 
      
      if vx == 0: # moving up or down
        if vy > 0: # moving up, correction down
          correctionx = 0
          correctiony = -((y1 + l1) - y2)
        else: # moving down, correction up
          correctionx = 0
          correctiony = (y2 + l2) - y1
        
      elif vy == 0: # moving left or right
        if vx > 0: # moving right, correction to left
          correctionx = -((x1 + w1) - x2)
          correctiony = 0
        else: # moving left, correction to right
          correctionx = (x2 + w2) - x1
          correctiony = 0
        
      else: # moving diagonally
        if vx > 0 and vy > 0: # moving to the right up
          g = x2
          x = x1 + w1
          y = y1 + l1
          f = y2
        elif vx > 0 and vy < 0: # moving right down
          g = x2
          x = x1 + w1
          y = y1
          f = y2 + l2
        elif vx < 0 and vy > 0: # moving to the left up
          g = x2 + w2
          x = x1
          y = y1 + l1
          f = y2
        else: # moving left down
          g = x2 + w2
          x = x1
          y = y1
          f = y2 + l2
        
        # calculate the intersection point with the object in the direction of -velocity
        a1 = ( c*g + (y - c*x) ) # intersection with point (g, a), y-axis of object
        distance1 = math.sqrt( pow(x - g, 2) + pow(y - a1, 2) )
        a2 = ( f - (y - c*x) ) / c # intersection with point (a,f), x-axis of object
        distance2 = math.sqrt( pow(x - a2, 2) + pow(y - f, 2) )
        
        # correct to the closest intersection point 
        if distance1 < distance2: # y-axis intersection
          correctionx = g - x
          correctiony = a1 - y
        else: # x-axis intersection
          correctionx = a2 - x
          correctiony = f - y
        
    x1 = x1 + correctionx
    y1 = y1 + correctiony
    correctedPosition = dict(x=x1, y=y1)
    
    if collision:
      self.gamestate.events.collision.emit(self.gamestate, movingObject, otherObject, correctedPosition)
