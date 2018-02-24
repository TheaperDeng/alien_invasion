import pygame
from pygame.sprite import Sprite
import random
class Bullet(Sprite):
    '''Bullet'''
    def __init__(self,game_settings,screen,dog):
        super().__init__()
        self.screen=screen
        
        self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx=dog.rect.centerx
        self.rect.top=dog.rect.top
        
        self.y=float(self.rect.y)
        
        self.color=game_settings.bullet_bg_color
        self.speed=game_settings.bullet_speed
        #self.speed=random.randint(1,5)/10
    def update(self):
        self.y-=self.speed
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)