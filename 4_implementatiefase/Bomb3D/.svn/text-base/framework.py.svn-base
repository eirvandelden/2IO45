# 08/09 OGO 2.3.2
# Coded by: Etienne, Anson
# This is the framework of our program.

import time
import pygame
import ConfigParser
#import Engine.engine as engine
#import Input.input as input
from network.token import Token
#import Output.main as output

# The code that makes the splash screen
def splash():

  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  #insFont = pygame.font.SysFont(None, 50)
  #insLabels = []
  #instructions = (
  #"- Splash placeholder -",
  #"",  
  #"Press any key to continue..."
  #)

  # create lines of text
  #for line in instructions:
  #  tempLabel = insFont.render(line, 1, (255, 255, 255))
  #  insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  #for i in range(len(insLabels)):
  #  screen.blit(insLabels[i], (50, 30*i))
  
  splash = pygame.image.load("output/textures/splash.jpg")
  splash_rect = splash.get_rect()
  splash_rect.width = 640
  splash_rect.height = 480
  
  splash = pygame.transform.smoothscale(splash, (640, 480))
  
  screen.blit(splash, splash_rect)
  
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN:
        keepgoing = False
        current_menu = 'main_menu'

        
        
# The code that makes the start menu
def main_menu():

  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  insFont = pygame.font.SysFont(None, 20)
  insLabels = []
  instructions = (
  "- Main menu -",
  "",  
  "Press t for a tournament",
  "Press o for options",
  "Press q to quit",  
  )

  # create lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (255, 255, 255))
    insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 30*i))
   
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN and chr(event.key) == 't':
        keepgoing = False
        current_menu = 'toursear_menu'

      if event.type == pygame.KEYDOWN and chr(event.key) == 'o':
        keepgoing = False
        current_menu = 'options_menu'

      if event.type == pygame.KEYDOWN and chr(event.key) == 'q':
        keepgoing = False
        current_menu = 'quit'
        
      elif event.type == pygame.QUIT:
        keepgoing = False
        current_menu = 'quit'
        
# The code that makes the start menu
def options_menu():

  global current_menu
  global playername
  global debug
  global config

  # loop vars
  keepgoing = True
  typing = False
  keying = False
  slot = 0
  key = ''
  
  while keepgoing:
  
    # background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    # what to display
    insFont = pygame.font.SysFont(None, 20)
    insLabels = []
    instructions = (
    "- Options menu -",
    "",  
    "Press m to return to the main menu",
    )

    if not keying:
      instructions = instructions + ("Press Tab to toggle playername entering mode",)
      
    if typing:
      instructions = instructions + ("Press Delete to clear the current name",)
      instructions = instructions + ("current name: " + playername,)   

    if not typing:
      instructions = instructions + ("Press k to toggle key assignment mode",)
    
    if keying:
      instructions = instructions + ("Keying",)
      
    # instructions = instructions + ("Accelerate Forward: " + config.get('Input', 'AcceForw'),) werkt niet
    
    # create lines of text
    for line in instructions:
      tempLabel = insFont.render(line, 1, (255, 255, 255))
      insLabels.append(tempLabel)   
      
    # put everything on the screen
    screen.blit(background, (0,0)) 
    for i in range(len(insLabels)):
      screen.blit(insLabels[i], (50, 30*i))
     
    # show screen
    pygame.display.flip()
      
    # event handling
    for event in pygame.event.get():
 
      if typing:

        if event.type == pygame.KEYDOWN and event.key == 9:
          typing = False
          if debug:
            print 'not typing'          
          
        elif event.type == pygame.KEYDOWN:
          # legal chat input
          if (31 < event.key) and ( event.key < 127):
            playername = playername + chr(event.key)    
      
        if event.type == pygame.KEYDOWN and event.key == 127:
          playername = ''
          if debug:
            print 'deleting'    

      elif keying:

        if event.type == pygame.KEYDOWN and chr(event.key) == 'k':
          keying = False
          if debug:
            print 'not keying'          
          
        elif event.type == pygame.KEYDOWN:
          # legal chat input
          if (event.key < 256):
            key = chr(event.key)    
      
        if event.type == pygame.KEYDOWN and event.key == 127:
          playername = ''
          if debug:
            print 'deleting'   

      elif (not typing) and (not keying):
 
        if event.type == pygame.KEYDOWN and chr(event.key) == 'm':
          keepgoing = False
          current_menu = 'main_menu'
          
        elif event.type == pygame.KEYDOWN and event.key == 9:
          typing = True
          if debug:
            print 'typing'
            
        elif event.type == pygame.KEYDOWN and chr(event.key) == 'k':
          keying = True
          if debug:
            print 'keying'            
      
# The code that makes the start menu
def toursear_menu():

  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  insFont = pygame.font.SysFont(None, 20)
  insLabels = []
  instructions = (
  "- Tournament searching menu -",
  "",  
  "Press m to return to the main menu",
  "Press c to go to the tournament creation menu",
  "Press j to join a tournament",
  )
  
  # create lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (255, 255, 255))
    insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 30*i))
   
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN and chr(event.key) == 'm':
        keepgoing = False
        current_menu = 'main_menu'
    
      if event.type == pygame.KEYDOWN and chr(event.key) == 'c':
        keepgoing = False
        current_menu = 'newtour_menu'
        
      if event.type == pygame.KEYDOWN and chr(event.key) == 'j':
        keepgoing = False
        current_menu = 'lobby'
        
# The code that makes the start menu
def newtour_menu():
  
  global ops
  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  insFont = pygame.font.SysFont(None, 20)
  insLabels = []
  instructions = (
  "- Tournament Creation Menu -",
  "",  
  "Press t to return to the tournament searching menu",
  "Press c to create a game",
  )

  # create lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (255, 255, 255))
    insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 30*i))
   
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN and chr(event.key) == 't':
        keepgoing = False
        current_menu = 'toursear_menu'
        
      if event.type == pygame.KEYDOWN and chr(event.key) == 'c':
        keepgoing = False
        current_menu = 'lobby'
        ops = True
 

# The code that makes the start menu
def lobby():

  global ops
  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  insFont = pygame.font.SysFont(None, 20)
  insLabels = []
  instructions = (
  "- Tournament lobby -",
  "",  
  "Press e to return to exit the lobby",
  )

  if ops:
    instructions = instructions + ('Press S to start the game',)
  
  # create lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (255, 255, 255))
    insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 30*i))
   
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN and chr(event.key) == 'e':
        keepgoing = False
        current_menu = 'toursear_menu'
        
      if event.type == pygame.KEYDOWN and chr(event.key) == 'e':
        keepgoing = False
        current_menu = 'toursear_menu'
        
      if ops:  
        if event.type == pygame.KEYDOWN and chr(event.key) == 's':
          keepgoing = False
          current_menu = 'tourover_screen' 
 
 
# The code that makes the start menu
def tourover_screen():

  global current_menu
  
  # background
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))
  
  # what to display
  insFont = pygame.font.SysFont(None, 20)
  insLabels = []
  instructions = (
  "- Tournament overview -",
  "",  
  "Tournament name:",
  "",
  "(...)",
  "",
  "Player list sorted by score:",
  "", 
  "(...)",
  "",  
  "Press e to exit the tournament",
  )

  # create lines of text
  for line in instructions:
    tempLabel = insFont.render(line, 1, (255, 255, 255))
    insLabels.append(tempLabel)   
    
  # put everything on the screen
  screen.blit(background, (0,0)) 
  for i in range(len(insLabels)):
    screen.blit(insLabels[i], (50, 30*i))
   
  # show screen
  pygame.display.flip()
  
  # loop
  keepgoing = True
  while keepgoing:
    
    # event handling
    for event in pygame.event.get():

      if event.type == pygame.KEYDOWN and chr(event.key) == 'e':
        keepgoing = False
        current_menu = 'toursear_menu'
        ops = False  
        
        
def menu_system():
  
  global ingame
  global current_menu
  
  # While in the game
  while ingame:
  
    # display the correct menu
    if current_menu == 'splash':
      splash()
    elif current_menu == 'main_menu':
      main_menu()
    elif current_menu == 'options_menu':
      options_menu()
    elif current_menu == 'toursear_menu':
      toursear_menu() 
    elif current_menu == 'lobby':
      lobby() 
    elif current_menu == 'newtour_menu':
      newtour_menu() 
    elif current_menu == 'tourover_screen':
      tourover_screen() 
    elif current_menu == 'quit':
      ingame = False
      
 
# pygame stuff
pygame.init()
pygame.display.set_caption("Bomb3D")
screen = pygame.display.set_mode((640,480))
pygame.mouse.set_visible(False)

# enable options file editing
optionsfile = 'input/options.ini'
config = ConfigParser.RawConfigParser()
config.read(optionsfile)

# enter ingame, with starting status
current_menu = 'splash'
ingame = True 
ops = False 
playername = []
# playername = config.get('Player', 'Player')
debug = True

# Start up the menu system
menu_system()






