import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):

    def __init__(self,game_settings,screen):
        super().__init__()
        self.screen=screen
        self.game_settings=game_settings
        
        self.image=pygame.image.load('./image/time3.bmp')
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        self.speed=random.randint(4,9)/200
        
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.y+=self.speed
        self.rect.y=self.y
        