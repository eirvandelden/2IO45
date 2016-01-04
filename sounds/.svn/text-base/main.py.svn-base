import os, math
import sys # system routines
import pygame
from pygame.locals import *

__author__ = "Neal van den Eertwegh"

pygame.init()

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

SCREEN_SIZE = (1024,768)
MAP_SIZE = (8,7)
TILE_SIZE = 100

PLAYER = [1,1,"left"]
BOMB = (3,3)

MAP = []
MAP.append([1,1,1,1,1,1,1,1])
MAP.append([1,0,0,0,0,0,0,1])
MAP.append([1,0,1,1,0,1,0,1])
MAP.append([1,0,1,0,0,1,0,1])
MAP.append([1,0,0,1,1,1,0,1])
MAP.append([1,0,0,0,0,0,0,1])
MAP.append([1,1,1,1,1,1,1,1])

class SIM():
    def __init__(self):
        global screen
        self.screen = screen
        self.done = False
            
    def Node_Content(self, node_map, node):
      cols = MAP_SIZE[0]
      return node_map[node/cols][node-node/cols*cols]
      
    def Change_Node(self, node_map, node, value):
      cols = MAP_SIZE[0]
      node_map[node/cols][node-node/cols*cols] = value
      
  # breadth-first search
    def Search(self, start_node, end_node, obstacles):
      empty = 0
      cols = MAP_SIZE[0]
      rows = MAP_SIZE[1]
      max = cols * rows
      
      queue = []
      origin = []
      front = 0
      rear = 0
      
    # check if both end and start node are open (0), else there's no path
      if self.Node_Content(MAP, start_node) != 0 or self.Node_Content(MAP, end_node) != 0:
        return -1
      
    # dummy array for search status
      DUMMY_MAP = []
      for i in range(MAP_SIZE[1]):
        DUMMY_MAP.append([])
        for j in range(MAP_SIZE[0]): 
        # all nodes are ready initially
          DUMMY_MAP[i].append('ready')
          
    # create queue's
      for i in range(max+1):
        queue.append(-2)
        origin.append(-2)
          
    # add starting node to queue
      queue[rear] = start_node
      origin[rear] = -1
      rear = rear + 1
      
      while (front != rear): # while queue not empty
        if (queue[front] == end_node): # found shortest path
          break
          
        current = queue[front]
        
        left = current - 1
        
        if (left >= 0 and left/cols == current/cols): # if left node exists
          if (self.Node_Content(MAP, left) == 0 or obstacles == True): # if left node is open(a path exists)
            if (self.Node_Content(DUMMY_MAP, left) == 'ready'): # if left node hasn't been inspected
              queue[rear] = left
              origin[rear] = current
              self.Change_Node(DUMMY_MAP, left, 'waiting') # node inspected, change to waiting
              rear = rear + 1
              
        right = current + 1
        
        if (right < max and right/cols == current/cols):
          if (self.Node_Content(MAP, right) == 0 or obstacles == True):
            if (self.Node_Content(DUMMY_MAP, right) == 'ready'):
              queue[rear] = right
              origin[rear] = current
              self.Change_Node(DUMMY_MAP, right, 'waiting')
              rear = rear + 1
              
        top = current - cols
        
        if (top >= 0):
          if (self.Node_Content(MAP, top) == 0 or obstacles == True):
            if (self.Node_Content(DUMMY_MAP, top) == 'ready'):
              queue[rear] = top
              origin[rear] = current
              self.Change_Node(DUMMY_MAP, top, 'waiting')
              rear = rear + 1
              
        down = current + cols
        
        if (down < max):
          if (self.Node_Content(MAP, down) == 0 or obstacles == True):
            if (self.Node_Content(DUMMY_MAP, down) == 'ready'):
              queue[rear] = down
              origin[rear] = current
              self.Change_Node(DUMMY_MAP, down, 'waiting')
              rear = rear + 1
                
        if obstacles == True:
          rightdown = current + cols + 1
          
          if (rightdown < max and rightdown >= 0 and rightdown/cols == current/cols+1):
            if (self.Node_Content(MAP, rightdown) == 0 or obstacles == True):
              if (self.Node_Content(DUMMY_MAP, rightdown) == 'ready'):
                queue[rear] = rightdown
                origin[rear] = current
                self.Change_Node(DUMMY_MAP, rightdown, 'waiting')
                rear = rear + 1
                
          rightup = current - cols + 1
          
          if (rightup < max and rightup >= 0 and rightup/cols == current/cols-1):
            if (self.Node_Content(MAP, rightup) == 0 or obstacles == True):
              if (self.Node_Content(DUMMY_MAP, rightup) == 'ready'):
                queue[rear] = rightup
                origin[rear] = current
                self.Change_Node(DUMMY_MAP, rightup, 'waiting')
                rear = rear + 1
                
          leftdown = current + cols - 1
          
          if (leftdown < max and leftdown >= 0 and leftdown/cols == current/cols+1):
            if (self.Node_Content(MAP, leftdown) == 0 or obstacles == True):
              if (self.Node_Content(DUMMY_MAP, leftdown) == 'ready'):
                queue[rear] = leftdown
                origin[rear] = current
                self.Change_Node(DUMMY_MAP, leftdown, 'waiting')
                rear = rear + 1
                
          leftup = current - cols - 1
          
          if (leftup < max and leftup >= 0 and leftup/cols == current/cols-1):
            if (self.Node_Content(MAP, leftup) == 0 or obstacles == True):
              if (self.Node_Content(DUMMY_MAP, leftup) == 'ready'):
                queue[rear] = leftup
                origin[rear] = current
                self.Change_Node(DUMMY_MAP, leftup, 'waiting')
                rear = rear + 1
        
      # change status of current node to processed, continue with next node
        self.Change_Node(DUMMY_MAP, current, 'processed')
        front = front + 1
			
      if obstacles == False:
      # count the path length using the queue's
        path = 0
        current = end_node
        
        for i in range(front+1):
          if queue[front-i] == current:
            current = origin[front-i]
            if current == -1: # maze is solved
              return path
            path = path + 1
      else:
      # count the obstacles in the path
        obstacle = 0
        current = end_node
        stri = ""
        
        for i in range(front+1):
          if queue[front-i] == current:
            stri = stri + str(current) + ", "
            current = origin[front-i]
            if current == -1: # maze is solved
              return obstacle
            obstacle = obstacle + self.Node_Content(MAP, current)
      
    # no path exists
      return -1
            
  # find shortest path between two points on the map
    def Shortest_Path(self, start, end):
        start_node = start[1] * MAP_SIZE[0] + start[0]
        end_node = end[1] * MAP_SIZE[0] + end[0]
        return self.Search(start_node, end_node, 0)
        
    def Straight_Path(self, start, end):
        if start[0] == end[0] and start[1] == end[1]:
        # same point
          return 0
        elif start[0] == end[0]:
        # straight vertical line
          return abs(start[1] - end[1])
        elif start[1] == end[1]:
        # straight horizontal line
          return abs(start[0] - end[0])
        else:
        # sloped line
          return math.sqrt(((start[0] - end[0]) * (start[0] - end[0])) + ((start[1] - end[1]) * (start[1] - end[1])))
          
    def Count_Obstacles(self, start, end):        
        start_node = start[1] * MAP_SIZE[0] + start[0]
        end_node = end[1] * MAP_SIZE[0] + end[0]
        return self.Search(start_node, end_node, 1)
        
    def Distance(self):
        shortest = self.Shortest_Path((PLAYER[0],PLAYER[1]),(BOMB))
        straight = self.Straight_Path((PLAYER[0],PLAYER[1]),(BOMB))
        print "Shortest: " + str(shortest)
        print "Straight: " + str(straight)
        
        if shortest != straight:
        # obstacles between player and bomb
          obstacles = self.Count_Obstacles((PLAYER[0],PLAYER[1]),(BOMB))
        else:
          obstacles = 0
          
        print "Obstacles: " + str(obstacles)
        
        return (shortest, straight, obstacles)
        
    def Play_Sound(self, (shortest, straight, obstacles)):
        volume = max(1.0 - (shortest*shortest / 20.0), 0.0)
        print "Volume: " + str(volume)
        if volume >= 0.0:
          pygame.mixer.Channel(0).set_volume(volume)
        if pygame.mixer.Channel(0).get_busy() == False and volume > 0:
          pygame.mixer.Channel(0).play(pygame.mixer.Sound("fuse.ogg"), -1)
        elif pygame.mixer.music.get_busy() != False and volume <= 0:
          pygame.mixer.Channel(0).stop()
          
        volume = max(min(volume + (1.0/(straight*3+1)-obstacles*0.1), 1.0), 0.0)
        print "Volume: " + str(volume)
        if volume >= 0.0:
          pygame.mixer.Channel(1).set_volume(volume)
        if pygame.mixer.Channel(1).get_busy() == False and volume > 0:
          pygame.mixer.Channel(1).play(pygame.mixer.Sound("fuse.ogg"), -1)
        elif pygame.mixer.music.get_busy() != False and volume <= 0:
          pygame.mixer.Channel(1).stop()
          
    def Move(self,direction):
        if direction == PLAYER[2]:
        # move towards current direction
          if direction == "up" and MAP[PLAYER[1]-1][PLAYER[0]] == 0:
            PLAYER[1] = max(PLAYER[1] - 1, 0)
          elif direction == "right" and MAP[PLAYER[1]][PLAYER[0]+1] == 0:
            PLAYER[0] = min(PLAYER[0] + 1, MAP_SIZE[0]-1)
          elif direction == "down" and MAP[PLAYER[1]+1][PLAYER[0]] == 0:
            PLAYER[1] = min(PLAYER[1] + 1, MAP_SIZE[1]-1)
          elif direction == "left" and MAP[PLAYER[1]][PLAYER[0]-1] == 0:
            PLAYER[0] = max(PLAYER[0] - 1, 0)
        else:
        # change current direction
          PLAYER[2] = direction
        
        self.Play_Sound(self.Distance())
        
    def Draw_Map(self):
        map_width = TILE_SIZE * MAP_SIZE[0]
        map_height = TILE_SIZE * MAP_SIZE[1]
        
        map_x = math.floor((SCREEN_SIZE[0] - map_width) / 2)
        map_y = math.floor((SCREEN_SIZE[1] - map_height) / 2)
        
      # map_outline = pygame.Rect((map_x, map_y), (map_width, map_height))
      # pygame.draw.rect(screen, (255,255,255), map_outline, 0)
        
        floor_img = pygame.image.load("floor.jpg")
        wall_img = pygame.image.load("wall.jpg")
        bomb_img = pygame.image.load("bomb.png")
        player_img = pygame.image.load("player.png")
        
        floor_img = pygame.transform.smoothscale(floor_img, (TILE_SIZE, TILE_SIZE))
        wall_img = pygame.transform.smoothscale(wall_img, (TILE_SIZE, TILE_SIZE))
        bomb_img = pygame.transform.smoothscale(bomb_img, (TILE_SIZE, TILE_SIZE))
        player_img = pygame.transform.smoothscale(player_img, (TILE_SIZE, TILE_SIZE))
        
        img_rect = wall_img.get_rect()
        
        # draw all tiles
        for i in range(MAP_SIZE[0]):
          for j in range(MAP_SIZE[1]):  
            img_rect.left = map_x + i * TILE_SIZE    
            img_rect.top = map_y + j * TILE_SIZE
            if MAP[j][i] == 0:
              # floor              
              screen.blit(floor_img, img_rect)
            else:
              # wall
              screen.blit(wall_img, img_rect)
              
        img_rect.left = map_x + TILE_SIZE * BOMB[0]
        img_rect.top = map_y + TILE_SIZE * BOMB[1]
        screen.blit(bomb_img, img_rect)
              
        img_rect.left = map_x + TILE_SIZE * PLAYER[0]
        img_rect.top = map_y + TILE_SIZE * PLAYER[1]
        if PLAYER[2] == "up": 
          player_img = pygame.transform.rotate(player_img, 180)
        if PLAYER[2] == "left": 
          player_img = pygame.transform.rotate(player_img, 270)
        if PLAYER[2] == "right": 
          player_img = pygame.transform.rotate(player_img, 90)
        screen.blit(player_img, img_rect)
    
    def Go(self):
        pygame.mouse.set_visible(0)
        pygame.mouse.set_pos(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)

        try:
            pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
        except pygame.error, exc:
            print >>sys.stderr, "Could not initialize sound system: %s" % exc
            return 1
            
        while not self.done:
            for event in pygame.event.get(): # watch for events
                if event.type == QUIT: 
                    self.done = True
                elif event.type == KEYDOWN: # if a key is pressed
                    if event.key == K_ESCAPE: # escape key
                        self.done = True
                    if event.key == K_UP: 
                        self.Move("up")
                    if event.key == K_DOWN: 
                        self.Move("down")
                    if event.key == K_LEFT: 
                        self.Move("left")
                    if event.key == K_RIGHT: 
                        self.Move("right")
                        
            self.Draw_Map()
            pygame.display.flip()
            
if __name__ == '__main__':
    # init screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Sound SIM PyGame")
    simulation = SIM()
    simulation.Go()