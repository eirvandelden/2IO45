import os, math
import sys # system routines
import pygame
from pygame.locals import *

__author__ = "Neal van den Eertwegh"

pygame.init()

# contants
SCREEN_SIZE = (1024,768)
MAP_SIZE = (800,400)
MAP_SCREEN_RATIO = 3;

class HUD():
    def __init__(self):
        global screen
        self.screen = screen
        self.done = False
        
    def Draw_Mini_Map(self):
        map_height = math.floor(SCREEN_SIZE[1] / MAP_SCREEN_RATIO)
        map_width = math.floor(map_height / MAP_SIZE[1] * MAP_SIZE[0])
        
        map_x = math.floor((SCREEN_SIZE[0] - map_width) / 2)
        map_y = map_height * (MAP_SCREEN_RATIO - 1);
        
        map_outline = pygame.Rect((map_x, map_y), (map_width, map_height))
        pygame.draw.rect(screen, (255,255,255), map_outline, 0)
        
      # resize image: pygame.transform.smoothscale(score_img, (width, height), DestSurface = None)
        
  # def Draw_Power_Ups(self):
        
    def Draw_Stats(self):
        icon_label = []
        for i in range(10):
            icon_label.append(pygame.image.load("icon_label_" + str(i) + ".png"))
        
        score_img = pygame.image.load("icon_score.png")
        score_rect = score_img.get_rect()
        
        bomb_img = pygame.image.load("icon_bomb.png")
        bomb_rect = bomb_img.get_rect()
        
        range_img = pygame.image.load("icon_range.png")
        range_rect = range_img.get_rect()
        
        score_rect.top = 10
        bomb_rect.top = 85
        range_rect.top = 160
        
        score_rect.left = bomb_rect.left = range_rect.left = 10
        
        screen.blit(score_img, score_rect)
        screen.blit(bomb_img, bomb_rect)
        screen.blit(range_img, range_rect)
        
        screen.blit(icon_label[0], score_rect)
        screen.blit(icon_label[9], bomb_rect)
        screen.blit(icon_label[5], range_rect)
        
  # def Draw_Menu(self):
    
    def Display(self):
        pygame.mouse.set_visible(0)
        pygame.mouse.set_pos(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
        while not self.done:
            for event in pygame.event.get(): # watch for events
                if event.type == QUIT: 
                    self.done = True
                elif event.type == KEYDOWN: # if a key is pressed
                    if event.key == K_ESCAPE: # escape key
                        self.done = True
                        
            self.Draw_Mini_Map()
            self.Draw_Stats()
            pygame.display.flip()
            
if __name__ == '__main__':
    # init screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("GUI PyGame")
    
    ui = HUD()
    ui.Display()