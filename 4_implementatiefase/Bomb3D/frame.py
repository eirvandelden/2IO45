# 08/09 OGO 2.3.2
# Coded by: Anson
import pygame
import Queue
import engine.event as event

# minimal pygame stuff, to be changed in final code.
pygame.init()
screen = pygame.display.set_mode((640, 480))

# options file name and location
optionsfile = 'input/options.ini'

# example player_id, to be changed in final code.      
player_id = 0

# Queue.Queue(<1) means length is infinity: used for debugging. 
# ie is short for 'input-to-engine'
ie_queue = Queue.Queue(0)

# start an 'inputReader' input thread.
# args: pygame screen, options file, queue to write to, id of owning player, debug_mode_on bool
inputread = input.input(screen, optionsfile, ie_queue, player_id, True)
inputread.run()
