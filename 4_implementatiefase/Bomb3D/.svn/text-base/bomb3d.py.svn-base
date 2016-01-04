# -*- coding: utf-8 -*-
# 08/09 OGO 2.3.2

# imports
import pygame
import ConfigParser
import time
import math

# from imports
from Queue import Queue

# our code
from network.token import Token, Server
import engine.player as player
import input.input as input
import engine.engine as engine
import maps.simple.level as level
import output.graphics

def splash_get():

  current_menu = 'splash'
  
  # what to read
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      current_menu = 'main' 

  return (current_menu, ())

def main_get():
  
  current_menu = 'main'
  
  lines = (
  "- Main menu -",
  "",  
  "Press 's' to search for a game.",
  "Press 'c' to create a new game.",  
  "Press 'q' to quit.",  
  )
      
  # what to read
  for event in pygame.event.get():
 
    if event.type == pygame.KEYDOWN:
 
      if (31 < event.key) and (event.key < 127):

        if chr(event.key) == 's':
          current_menu = 'search'
          lines = (
          "",
          "",
          "Searching..",
          )

        elif chr(event.key) == 'c':
          current_menu = 'name'
          lines = (
            "",
            "",
            "Starting broadcast..",
            "",
            "Game Name:",
            game_name,
            )
          
        elif chr(event.key) == 'q':
          current_menu = 'quit'        
          
    elif event.type == pygame.QUIT:
      current_menu = 'quit'
      
  return (current_menu, lines)
 
def search_get(found):

  current_menu = 'found'

  lines = (
  "",
  "",
  "Searching..",
  )
  
  found = Token.search()
  
  return (current_menu, lines, found)

def found_get(found, game_picked):

  current_menu = 'found'

  lines = (
  "- Game searching menu -",
  "",  
  )
  
  if not found:
    lines = lines + ("No games were found.",)  
    
  lines = lines + ("Press 'm' to return to the main menu.",)  

  if found:
    ffound = [(x['name'], x['server']) for x in [x for k, x in found.iteritems()]]
  
    lines = lines + ("Press a number to join that game.",
    "Games found:",
    "", 
    )
    i = 0    
    for s in ffound:
      lines = lines + (str(i) + ': ' + s[0],) 
      i = i + 1
      
   # what to read
  for event in pygame.event.get():
  
    if event.type == pygame.KEYDOWN:
  
      if (31 < event.key) and (event.key < 127):
          
        if chr(event.key) == 'm':
          current_menu = 'main'
        
      if (47 < event.key) and (event.key < 58) and (len(found) > event.key - 48):
        print repr(found)
        game_picked = ffound[event.key-48]
        current_menu = 'wait'
        
        lines = (
        "",
        "",
        "Waiting for the server..", 
        "You've joined the game:",
        game_picked[0],
        )
 
  return (current_menu, lines, game_picked) 
 
def wait_get(game_name, in_queue, ne_queue, game_picked):

  current_menu = 'wait'

  lines = (
  "",
  "",
  "Waiting for the server..",
  "",
  "You've joined the game:",
  game_name,
  )
  
  ######################################################
  # TODO: Do funky network stuff. Start the game!
  ######################################################

  start_game(game_name, in_queue, ne_queue, game_picked)
  
  return (current_menu, lines)
  
def start_game(game_name, in_queue, ne_queue, game_picked):  
  
  print repr(game_picked)
  token = Token(game_picked[1], in_queue, ne_queue)  
  in_queue.put(" ".join(["index", str(token.ring.index)]))
  playerlist = [None, None, None, None, None, None, None, None]
  color = ['red', 'blue', 'green', 'purple', 'yellow', 'cyan', 'black', 'orange']
  tokencounter = 0
  while tokencounter < 5:
    got = ne_queue.get(True)
    ident, mesg, index = got.split(" ", 2)
    if (mesg == "token"):
      tokencounter = tokencounter + 1
    else:
      p = player.player(ident, color[int(index)], 3)
      playerlist[int(index)] = p
      if (ident == token.identifier):
        this_player = p
  
  playerlist = [x for x in playerlist if x != None]
  
  output.graphics.initGraphics()
  graphics = output.graphics.graphicalLevel(this_player)
  
  llevel = level.simple()
  options = dict()
  
  iinput = input.input(graphics.screen, 'input/options.ini', in_queue, this_player.UUID, 0)
  
  eengine = engine.engine(graphics, llevel, playerlist, ne_queue, options)
  graphics.buildLists(eengine.gamestate)
  
  eengine.inputqueuehandler.handle(iinput)    
  
  sys.quit()  
  
def name_get(typing, game_name):

  current_menu = 'name'
   
  if typing:
    lines = (
  "- Game Naming Menu -",
  "",  
  "",
  "",
  "Current game name: ",
  game_name,
  "",
  "Press Delete to clear the current name.",
  "Press TAB to finish typing.",
  )     
    
  if not typing:
    lines = (
  "- Game Naming Menu -",
  "",  
  "Press 'm' to return to the main menu.",
  "",
  "Current game name: ",
  game_name,
  "",
  "press TAB to start typing.",
  "Press 'd' when you're done.",)  
 
  # what to read
  for event in pygame.event.get():

    if (event.type == pygame.KEYDOWN):
    
      if not typing:
      
        if (31 < event.key) and (event.key < 127):
      
          if chr(event.key) == 'm':
            current_menu = 'main'
          
          elif chr(event.key) == 'd':
            current_menu = 'serve'
            if debug:
              print 'not typing'
            if not len(game_name): game_name = 'mygame'
            lines = (
            "",
            "",
            "Acting as a server", 
            "",
            "Game Name:",
            game_name,
            )
        
        elif event.key == 9:
          typing = True
          if debug:
            print 'typing'  
    
      else:
        
        if event.key == 9:
          typing = False
          if debug:
            print 'not typing' 
            
        # legal chat input
        if (31 < event.key) and (event.key < 127):
          game_name = game_name + chr(event.key)    

        if event.key == 127:
          game_name = ''
          if debug:
            print 'deleting'        
    
  return (current_menu, typing, game_name, lines)    
  
def serve_get(game_name):
 
  current_menu = 'serve'
 
  lines = (
  "",
  "",
  "Acting as a server", 
  "",
  "Game Name:",
  game_name,
  )
  
  server = Server(game_name)
  time.sleep(15)
  server.stop() 
  
  sys.quit()
  
  ######################################################
  # TODO: Start the game.
  ######################################################  
  
  # what to read
  #for event in pygame.event.get():

    #if event.type == pygame.KEYDOWN and chr(event.key) == 'c':  
    #  current_menu = 'main'
    #  server.stop()
      
    #if event.type == pygame.KEYDOWN and chr(event.key) == 's':
    #  current_menu = 'main'  

  return (current_menu, instructions)

# INITIALIZATION  
  
# debugging mode? 
debug = True

FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

# pygame stuff
pygame.init()
pygame.display.set_caption("Bomb3D")
screen = pygame.display.set_mode((640,480))
pygame.mouse.set_visible(False)
font_size = 25
    
try:
  pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
except pygame.error, exc:
  print >>sys.stderr, "Could not initialize sound system: %s" % exc

pygame.mixer.music.load('output/sounds/bombermantouch.wav')
pygame.mixer.music.play(0)


# enable options for file editing
optionsfile = 'input/options.ini'
config = ConfigParser.RawConfigParser()
config.read(optionsfile)

# enter game with starting status
ingame = True  
current_menu = 'splash'
typing = False

# starting values of visible vars
found = []
game_picked = ''
game_name = 'myGame'

# hardcoded stuff
in_queue = Queue()
ne_queue = Queue()


# MAIN LOOP
while ingame:

  # Pick the correct menu
  
  # general menus
  if current_menu == 'splash':
    (current_menu, instructions) = splash_get()
    
  elif current_menu == 'main':
    (current_menu, instructions) = main_get()
    
  # client menus
  elif current_menu == 'search':
    (current_menu, instructions, found) = search_get(found)
    
  elif current_menu == 'found':
    (current_menu, instructions, game_picked) = found_get(found, game_picked)
    
  elif current_menu == 'wait':
    (current_menu, instructions) = wait_get(game_picked, in_queue, ne_queue, game_picked)   
  
  # server menus
  elif current_menu == 'name':
    (current_menu, typing, game_name, instructions) = name_get(typing, game_name)
    
  elif current_menu == 'serve':
    (current_menu, instructions) = serve_get(game_name)     
  
  # neat quit
  elif current_menu == 'quit':
    ingame = False
  
  # messy quit
  else:
    if debug:
      print 'HALP'
    ingame = False
   
  # clear surface
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  screen.blit(background, (0,0)) 
  
  # splash if applicable
  if current_menu == 'splash':
    splash = pygame.image.load("output/textures/splash.jpg")
    splash_rect = splash.get_rect()
    splash_rect.width = 640
    splash_rect.height = 480
    splash = pygame.transform.smoothscale(splash, (640, 480))
    screen.blit(splash, splash_rect)      
  
  # background otherwise
  if not current_menu == 'splash':
    splash = pygame.image.load("output/textures/menu.jpg")
    splash_rect = splash.get_rect()
    splash_rect.width = 640
    splash_rect.height = 480
    splash = pygame.transform.smoothscale(splash, (640, 480))
    screen.blit(splash, splash_rect)  
    
  # font options, new list of labels
  insFont = pygame.font.SysFont(None, font_size)
  insLabels = []  

  # turn the list of labels into lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (0, 0, 0))
    insLabels.append(tempLabel)   
    
  # put the lines of text on the screen
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 50 + 30*i))
  
  # show screen
  pygame.display.flip()
