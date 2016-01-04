# Particle Simulator

import sys, os, pygame, random, math
from pygame.locals import *

if sys.platform == 'win32': #for compatibility on some hardware platforms
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
xmax = 1000    #width of window
ymax = 600     #height of window
psize = 3      #particle size

class Particle:
   def __init__(self, x = 0, y = 0, dx = 0, dy = 0, col = (255,255,255)):
       self.x = x    #absolute x,y in pixel coordinates
       self.y = y
       self.rx = x   #absolute x,y in real coordinates
       self.ry = y
       self.dx = dx   #force-like vectors
       self.dy = dy
       self.col = col

   def mass(self, points):
       dx = 0.0
       dy = 0.0
       for p in points:         #where is everybody else?
           dx1 = p.rx - self.rx
           dy1 = p.ry - self.ry
           
           d = math.sqrt(pow(dx1, 2) + pow(dy1, 2))   #distance from me to p

           if d < 15: 
               dx -= 7 * dx1
               dy -= 7 * dy1

       #induce simple drag and energy
       self.dx = 0.98 * self.dx + 0.03 * dx
       self.dy = 0.98 * self.dy + 0.03 * dy
        
   def move(self):
               
       self.rx += self.dx
       self.ry += self.dy
       self.x = int(self.rx + 0.5)
       self.y = int(self.ry + 0.5)
       
def main():
   # Initialize PyGame
   pygame.init()
   pygame.display.set_caption('Particle Sim')
   screen = pygame.display.set_mode((xmax,ymax))
   #want fullscreen? pygame.display.set_mode((xmax,ymax), pygame.FULLSCREEN)
   white = (255, 255, 255)
   black = (0,0,0)

   particles = []
   for i in range(50):
       if i % 2 > 0: col = black
       else: col = black
       particles.append( Particle(500 + random.randint(-25, 25), 300 + random.randint(-25, 25), 0, 0, col) )

   exitflag = False
   while not exitflag:
       
       # Handle events
       for event in pygame.event.get():
           if event.type == QUIT:
               exitflag = True
           elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   exitflag = True
       screen.fill(white)
       for p in particles:
           p.mass(particles)
       for p in particles:
           p.move()
           pygame.draw.circle(screen, p.col, (p.x, p.y), psize)
           
       pygame.display.flip()

   # Close the Pygame window
   pygame.quit()

#Run the system

if __name__ == "__main__":
    main()