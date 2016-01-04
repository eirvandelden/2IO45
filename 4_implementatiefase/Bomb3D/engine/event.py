# -*- coding: utf-8 -*-

### available properties:
# none?
# 

class event(object):
  def __init__(self, name):
    self.name = name
    self.callbacks = []
  
  def register(self, func):
    self.callbacks.append(func)
  
  def unregister(self, func):
    self.callbacks.remove(func)
  
  def emit(self, *args):
    #if self.name != "eMouseEvent":
      #print "DEBUG: " + self.name + " emitted"
    #TODO: mogelijk copy maken van callback
    for callback in self.callbacks:
      callback(*args)

class events():
  pass
