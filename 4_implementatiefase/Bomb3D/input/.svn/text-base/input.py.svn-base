# -*- coding: utf-8 -*-
# 08/09 OGO 2.3.2
# Coded by: Anson

# Problem: 
# In chat mode, you can't see the text which you're typing until you send it (that is, until you toggle chat off). 
# edit: This is a design flaw, i'm afraid. How much of a problem is it? You, sir, may decide.

# Problem:
# Threading is problematic. Mouse input isn't read. If the threading does work in the output module, i propose to merge this with it.
# edit: ok, so apparently this is a fundamental limitation of pyGame, all pyGame stuff must be run in the main thread.

import pygame
from pygame.locals import *

import Queue
import ConfigParser

import time
import sys, os


class input(object):

  def __init__(self, screen, optionsfile, outqueue, player_id, debug_mode_on): 
    
    # Input conversion
    self.outqueue = outqueue
    self.id = player_id  
    self.screen = screen
    self.debug = debug_mode_on
    self.mid_x = self.screen.get_size()[0] / 2
    self.mid_y = self.screen.get_size()[1] / 2
    
    # get options
    self.config = ConfigParser.RawConfigParser()
    self.config.read(optionsfile)
    self.keyDict = {}
    self.buttonDict = {}
    self.chat_toggler = self.config.get('Input', 'ChatTogg')[1:]
    listOfSlots = ['AcceForw', 'AcceBack', 'StepLeft', 'StepRght', 'DropBomb', 'Powerup1', 'Powerup2', 'Powerup3', 'MinimapT']
    
    # put the options into dictionaries for fast retrieval
    for self.slot in listOfSlots:
      self.key = self.config.get('Input', self.slot)[1:]
      if (self.config.get('Input', self.slot)[0] == 'K'):
        self.keyDict[self.key] = self.slot
        if self.debug:
          print 'K'
          print self.key
          print self.slot
      else: 
        self.buttonDict[self.key] = self.slot
        if self.debug:
          print 'B'
          print self.key
          print self.slot
    
    # status variables + chat  
    self.done = False
    self.chatting = False
    self.newchat = True
    self.chatmessage = '' 
    self.last_pos = (self.mid_x, self.mid_y)
  
  # messages sent have this format:
  # (UUID), message type, data 
  def run(self): 
    #while self.done == False:
      for event in pygame.event.get():
      
        # mouse moved
        if (event.type == MOUSEMOTION): 
        
          # output
          if self.debug:
            print event.rel, self.id
          if not ((event.pos == (self.mid_x, self.mid_y)) or 
          ((self.last_pos[0] < event.pos[0]) and (event.pos[0] < self.mid_x)) or 
          ((self.last_pos[0] > event.pos[0]) and (event.pos[0] > self.mid_x))):
            
            # mouse action!
            self.outqueue.put('m' + ' ' + str(event.rel[0]) + 'x' + str(event.rel[1]))
            pygame.mouse.set_visible(0)
            pygame.mouse.set_pos(self.mid_x, self.mid_y)
            
          self.last_pos = event.pos
        
        # mouse button pressed  
        elif (event.type == MOUSEBUTTONDOWN):
          
          if not self.chatting:
            
            # output
            if str(event.button) in self.buttonDict:
              if self.debug:
                print self.buttonDict[str(event.button)]
              self.outqueue.put('b' + ' ' + self.buttonDict[str(event.button)] + 'On')
              
            # enter chat
            if (str(event.button) == self.chat_toggler):
              if self.debug:
                print 'chat toggled on'
              self.chatting = True   
            
          else:
            
            # exit chat
            if (str(event.button) == self.chat_toggler):
              if self.debug:
                print 'chat toggled off'
              self.chatting = False 
              self.outqueue.put('c' + ' ' + self.chatmessage)
              if self.debug:
                print self.chatmessage
              self.chatmessage = ''  
              self.newchat = True  
        
        # mouse button released
        elif (event.type == MOUSEBUTTONUP):
          # output
          if str(event.button) in self.buttonDict:
            if self.debug:
              print self.buttonDict[str(event.button)]
            self.outqueue.put('b' + ' ' + self.buttonDict[str(event.button)] + 'Off')
        
        # keyboard key lifted
        elif (event.type == KEYUP):
          
          # in action mode
          if not self.chatting:
            
            # action
            if str(event.key) in self.keyDict:
              if self.debug:
                print self.keyDict[str(event.key)]
              self.outqueue.put('b' + ' ' + self.keyDict[str(event.key)] + 'Off')
        
        # keyboard key pressed
        elif (event.type == KEYDOWN):
          
          if not self.chatting:
            
            # action
            if str(event.key) in self.keyDict:
              if self.debug:
                print self.keyDict[str(event.key)]
              self.outqueue.put('b' + ' ' + self.keyDict[str(event.key)] + 'On')
            
            # enter chat
            if (str(event.key) == self.chat_toggler):
              if self.debug:
                print 'chat toggled on'
              self.chatting = True
              
          else: 
            
            # exit chat
            if (str(event.key) == self.chat_toggler):
              if self.debug:
                print 'chat toggled off'
              self.chatting = False 
              self.outqueue.put('c' + ' ' + self.chatmessage)
              if self.debug:
                print self.chatmessage
              self.chatmessage = ''
              self.newchat = True
            
            # typing
            else: 
              
              # legal chat input
              if (event.key < 256): 
                
                # new chat message
                if self.newchat:
                  self.chatmessage = chr(event.key)
                  self.newchat = False
                
                # cont'd chat message
                else:
                  self.chatmessage = self.chatmessage + chr(event.key)

        #if self.debug:

        if (event.type == KEYDOWN) and (event.key == K_ESCAPE):     
        #self.done = True
          self.outqueue.put('q escape')
