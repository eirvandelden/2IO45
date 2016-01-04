__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

# TODO: - Player dies sound
#       - Power-up sound
#       - Random shout-outs xD
#       - ?????

from math import sqrt
from operator import itemgetter
import pygame
pygame.init()

FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

SQUARE_SIZE = 80
SOUND_RADIUS = 4

BOMB_CHANNELS = 3
EXPLOSION_CHANNELS = 10

class Sound(): # The Sound Module
  def __init__(self, events, player):
    self.player = player
    self.explosions = []
    
    events.playerspawned.register(self.Player_Die)
    events.bombexplode.register(self.Start_Explosion)
    events.poweruppickup.register(self.Start_Powerup)
    
    try:
        pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
        pygame.mixer.set_num_channels(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 3)
        pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2).set_volume(0.2)
    except pygame.error, exc:
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        return 1
    
  def Node_Content(self, node_map, node):
    cols = len(node_map[0])
    return node_map[int(node/cols)][int(node-node/cols*cols)]
    
  def Change_Node(self, node_map, node, value):
    cols = len(node_map[0])
    node_map[node/cols][node-node/cols*cols] = value
    
# breadth-first search
  def Search(self, map, start_node, end_node, obstacles):
    empty = 0
    cols = len(map[0])
    rows = len(map)
    max = cols * rows
    
    queue = []
    origin = []
    front = 0
    rear = 0
    
  # check if both end and start node are open (0), else there's no path
    if self.Node_Content(map, start_node) != 0 or self.Node_Content(map, end_node) != 0:
      return float("infinity")
    
  # dummy array for search status
    dummy_map = []
    for i in range(len(map)):
      dummy_map.append([])
      for j in range(len(map[0])): 
      # all nodes are ready initially
        dummy_map[i].append('ready')
        
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
        if (self.Node_Content(map, left) == 0 or obstacles == True): # if left node is open(a path exists)
          if (self.Node_Content(dummy_map, left) == 'ready'): # if left node hasn't been inspected
            queue[rear] = left
            origin[rear] = current
            self.Change_Node(dummy_map, left, 'waiting') # node inspected, change to waiting
            rear = rear + 1
            
      right = current + 1
      
      if (right < max and right/cols == current/cols):
        if (self.Node_Content(map, right) == 0 or obstacles == True):
          if (self.Node_Content(dummy_map, right) == 'ready'):
            queue[rear] = right
            origin[rear] = current
            self.Change_Node(dummy_map, right, 'waiting')
            rear = rear + 1
            
      top = current - cols
      
      if (top >= 0):
        if (self.Node_Content(map, top) == 0 or obstacles == True):
          if (self.Node_Content(dummy_map, top) == 'ready'):
            queue[rear] = top
            origin[rear] = current
            self.Change_Node(dummy_map, top, 'waiting')
            rear = rear + 1
            
      down = current + cols
      
      if (down < max):
        if (self.Node_Content(map, down) == 0 or obstacles == True):
          if (self.Node_Content(dummy_map, down) == 'ready'):
            queue[rear] = down
            origin[rear] = current
            self.Change_Node(dummy_map, down, 'waiting')
            rear = rear + 1
              
      if obstacles == True:
        rightdown = current + cols + 1
        
        if (rightdown < max and rightdown >= 0 and rightdown/cols == current/cols+1):
          if (self.Node_Content(map, rightdown) == 0 or obstacles == True):
            if (self.Node_Content(dummy_map, rightdown) == 'ready'):
              queue[rear] = rightdown
              origin[rear] = current
              self.Change_Node(dummy_map, rightdown, 'waiting')
              rear = rear + 1
              
        rightup = current - cols + 1
        
        if (rightup < max and rightup >= 0 and rightup/cols == current/cols-1):
          if (self.Node_Content(map, rightup) == 0 or obstacles == True):
            if (self.Node_Content(dummy_map, rightup) == 'ready'):
              queue[rear] = rightup
              origin[rear] = current
              self.Change_Node(dummy_map, rightup, 'waiting')
              rear = rear + 1
              
        leftdown = current + cols - 1
        
        if (leftdown < max and leftdown >= 0 and leftdown/cols == current/cols+1):
          if (self.Node_Content(map, leftdown) == 0 or obstacles == True):
            if (self.Node_Content(dummy_map, leftdown) == 'ready'):
              queue[rear] = leftdown
              origin[rear] = current
              self.Change_Node(dummy_map, leftdown, 'waiting')
              rear = rear + 1
              
        leftup = current - cols - 1
        
        if (leftup < max and leftup >= 0 and leftup/cols == current/cols-1):
          if (self.Node_Content(map, leftup) == 0 or obstacles == True):
            if (self.Node_Content(dummy_map, leftup) == 'ready'):
              queue[rear] = leftup
              origin[rear] = current
              self.Change_Node(dummy_map, leftup, 'waiting')
              rear = rear + 1
      
    # change status of current node to processed, continue with next node
      self.Change_Node(dummy_map, current, 'processed')
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
      
      for i in range(front+1):
        if queue[front-i] == current:
          current = origin[front-i]
          if current == -1: # maze is solved
            return obstacle
          obstacle = obstacle + self.Node_Content(map, current)
    
  # no path exists
    return float("infinity")
          
# find shortest path between two points on the map
  def Shortest_Path(self, map, start, end):
    start_node = int(start['y'] / SQUARE_SIZE+0.5) * len(map[0]) + int(start['x'] / SQUARE_SIZE+0.5)
    end_node = int(end['y'] / SQUARE_SIZE+0.5) * len(map[0]) + int(end['x'] / SQUARE_SIZE+0.5)
    if start_node == end_node:
      return 0
    else:
      return self.Search(map, start_node, end_node, 0)
    
  def Straight_Path(self, start, end):
    if start == end:
      return 0
    else:
      return sqrt(((start['x'] - end['x']) * (start['x'] - end['x'])) + ((start['y'] - end['y']) * (start['y'] - end['y'])))
      
  def Count_Obstacles(self, map, start, end):        
    start_node = int(start['y'] / SQUARE_SIZE+0.5) * len(map[0]) + int(start['x'] / SQUARE_SIZE+0.5)
    end_node = int(end['y'] / SQUARE_SIZE+0.5) * len(map[0]) + int(end['x'] / SQUARE_SIZE+0.5)
    return self.Search(map, start_node, end_node, 1)
      
  def Obstacles(self, map, shortest, straight, start, end):    
    if shortest != straight:
    # obstacles between player and bomb
      obstacles = self.Count_Obstacles(map, start, end)
    else:
      obstacles = 0
    
    return obstacles
      
  def PlaySound(self, gamestate, player):
    map = []
    bombs = []
    explosions = []
    
    for i in range(gamestate.level.size['y'] / SQUARE_SIZE):
      map.append([])
      for j in range(gamestate.level.size['x'] / SQUARE_SIZE): 
      # all nodes are ready initially
        map[i].append(0)
    
    volume = 0
    
    for placeable in gamestate.placeables:
      if placeable.type == "softwall":
        map[int(placeable.coordinate['y'] / SQUARE_SIZE)][int(placeable.coordinate['x'] / SQUARE_SIZE)] = 1
      elif placeable.type == "hardwall":
        map[int(placeable.coordinate['y'] / SQUARE_SIZE)][int(placeable.coordinate['x'] / SQUARE_SIZE)] = 2
      elif placeable.type == "bomb":
        bombs.append(placeable.coordinate)
      elif placeable.type == "bomberman" and (placeable.velocity['x'] != 0 or placeable.velocity['y'] != 0) and self.Straight_Path(self.player.bomberman.coordinate, placeable.coordinate) <= SQUARE_SIZE * 2:
        if placeable.owner != player:
          volume = min(volume + (SQUARE_SIZE * 2 - self.Straight_Path(player.bomberman.coordinate, placeable.coordinate)) / (SQUARE_SIZE * 8.0), 1.0)

    if (player.bomberman.velocity['x'] != 0 or player.bomberman.velocity['y'] != 0) and pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2).get_busy() == False:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2).play(pygame.mixer.Sound("output/sounds/strafe.ogg"), -1)
    elif (player.bomberman.velocity['x'] == 0 and player.bomberman.velocity['y'] == 0) and pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2).get_busy() == True:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2).stop()
      
    pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2+1).set_volume(volume)
    if volume > 0 and pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2+1).get_busy() == False:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2+1).play(pygame.mixer.Sound("output/sounds/strafe.ogg"), -1)
    elif volume <= 0 and pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2+1).get_busy() == True:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2+1).stop()
      
    bomb_path = []
    bomb_wall = []
    
    for bomb in bombs:
      straight_len = self.Straight_Path(self.player.bomberman.coordinate, bomb)
      shortest_len = self.Shortest_Path(map, self.player.bomberman.coordinate, bomb)
      obstacles = self.Obstacles(map, shortest_len, straight_len, self.player.bomberman.coordinate, bomb)
      
      bomb_path.append(shortest_len)
      bomb_wall.append((straight_len + SQUARE_SIZE * obstacles) / SQUARE_SIZE)
      
    bomb_path.sort()
    bomb_wall.sort()
    
    for i in range(BOMB_CHANNELS):
      if i < len(bomb_path):
        volume = max(0.5 - bomb_path[i]/10.0, 0.0)
        
        if volume >= 0.0:
          pygame.mixer.Channel(i*2).set_volume(volume)
        if pygame.mixer.Channel(i*2).get_busy() == False and volume > 0:
          pygame.mixer.Channel(i*2).play(pygame.mixer.Sound("output/sounds/fuse.ogg"), -1)
        elif pygame.mixer.music.get_busy() != False and volume <= 0:
          pygame.mixer.Channel(i*2).stop()
          
      else:
        pygame.mixer.Channel(i*2).set_volume(0)
        if pygame.mixer.music.get_busy() != False:
          pygame.mixer.Channel(i*2).stop()
            
      if i < len(bomb_wall):
        volume = max(0.3 - bomb_wall[i] / 10.0, 0.0)
        if volume >= 0.0:
          pygame.mixer.Channel(i*2+1).set_volume(volume)
        if pygame.mixer.Channel(i*2+1).get_busy() == False and volume > 0:
          pygame.mixer.Channel(i*2+1).play(pygame.mixer.Sound("output/sounds/fuse.ogg"), -1)
        elif pygame.mixer.music.get_busy() != False and volume <= 0:
          pygame.mixer.Channel(i*2+1).stop()
          
      else:
        pygame.mixer.Channel(i*2+1).set_volume(0)
        if pygame.mixer.music.get_busy() != False:
          pygame.mixer.Channel(i*2+1).stop()
    
    explosion_distance = []
      
    for explosion in self.explosions:
      if explosion['channel'] > 0 and pygame.mixer.Channel(explosion['channel']).get_busy() == False:
      # find allready played explosions, and set them to idle
        explosion['channel'] = 0
        pygame.mixer.Channel(explosion['channel']).stop()
        pygame.mixer.Channel(explosion['channel']+1).stop()
        del self.explosions[self.explosions.index(explosion)]
      else:
        straight_len = self.Straight_Path(self.player.bomberman.coordinate, explosion['coordinate'])
        shortest_len = self.Shortest_Path(map, self.player.bomberman.coordinate, explosion['coordinate'])
        obstacles = self.Obstacles(map, shortest_len, straight_len, self.player.bomberman.coordinate, explosion['coordinate'])
        
        straight_len = straight_len / SQUARE_SIZE + obstacles
          
        if explosion['channel'] != 0:
          volume = max(1.0 - (shortest_len*shortest_len / 30.0), 0.0)
          volume = min(volume + volume * explosion['range'] / 10, 1)
        # adjust explosion volume
          pygame.mixer.Channel(explosion['channel']).set_volume(volume)
            
          volume = max(1.0 - (straight_len*straight_len / 25.0), 0.0)
          volume = min(volume + volume * explosion['range'] / 15, 1)
          pygame.mixer.Channel(explosion['channel']+1).set_volume(volume)
          
        explosion['timeplayed'] = explosion['timeplayed'] + 1
        
  def Start_Explosion(self, coordinate, bombrange):
    for explosion in self.explosions:
      if explosion['channel'] > 0 and pygame.mixer.Channel(explosion['channel']).get_busy() == False:
      # find allready played explosions, and set them to idle
        explosion['channel'] = 0
        pygame.mixer.Channel(explosion['channel']).stop()
        pygame.mixer.Channel(explosion['channel']+1).stop()
      explosion['timeplayed'] = explosion['timeplayed'] + 1
        
    if len(self.explosions) > EXPLOSION_CHANNELS - 1:
    # too much explosions going on, kill oldest
      self.explosions.sort(key=itemgetter('timeplayed'))
      count = len(self.explosions)
      for explosion in self.explosions:
        if count > EXPLOSION_CHANNELS - 2:
          if explosion['channel'] > 0:
            pygame.mixer.Channel(explosion['channel']).stop()
            pygame.mixer.Channel(explosion['channel']+1).stop()
          explosion['channel'] = 0
          del self.explosions[self.explosions.index(explosion)]
          count = count - 1
        else:
          break
        
  # assign new channel to explosion
    for i in range(EXPLOSION_CHANNELS):
      if pygame.mixer.Channel(BOMB_CHANNELS+i*2).get_busy() == False:
        self.explosions.append({'channel': BOMB_CHANNELS+i*2, 'timeplayed': 0, 'coordinate': coordinate, 'range': bombrange})
        pygame.mixer.Channel(BOMB_CHANNELS+i*2).set_volume(0)
        pygame.mixer.Channel(BOMB_CHANNELS+i*2).play(pygame.mixer.Sound("output/sounds/explosion.ogg"), 0)
        pygame.mixer.Channel(BOMB_CHANNELS+i*2+1).set_volume(0)
        pygame.mixer.Channel(BOMB_CHANNELS+i*2+1).play(pygame.mixer.Sound("output/sounds/explosion.ogg"), 0)
        break
        
  def Start_Powerup(self):
    if pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).get_busy() != False:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).stop()
    pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).set_volume(0.5)
    pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).play(pygame.mixer.Sound("output/sounds/powerup.ogg"), 0)
        
  def End_Powerup(self):
    if pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).get_busy() != False:
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).stop()
    pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).set_volume(0.5)
    pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).play(pygame.mixer.Sound("output/sounds/powerdown.ogg"), 0)
    
  def FTW(self, won):
    pygame.mixer.fadeout(1500)
    pygame.mixer.Channel(0).set_volume(1)
    if won:
      pygame.mixer.Channel(0).play(pygame.mixer.Sound("output/sounds/victory.ogg"), 0)
    else:
      pygame.mixer.Channel(0).play(pygame.mixer.Sound("output/sounds/defeat.ogg"), 0)
      
  def Player_Die(self, bomberman):
    straight_len = self.Straight_Path(bomberman.coordinate, self.player.bomberman.coordinate)
    volume = max(0.5 - straight_len / 800.0, 0)
    if volume > 0:
      if pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).get_busy() != False:
        pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).stop()
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).set_volume(volume)
      pygame.mixer.Channel(BOMB_CHANNELS*2 + EXPLOSION_CHANNELS*2 + 2).play(pygame.mixer.Sound("output/sounds/die.ogg"), 0)
      