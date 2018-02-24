import pygame
class Dog():
    
    def __init__(self,screen,game_settings):
        '''Let the ship be at the bottom of the screen'''
        self.screen=screen
        
        self.image=pygame.image.load('./image/dog.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
        self.moving_speed=game_settings.moving_speed
        
        self.x=float(self.rect.centerx)
        self.y=float(self.rect.centery)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        if self.moving_right==True and self.rect.right<self.screen_rect.right:
            self.x+=0.15
            self.rect.centerx=self.x
        if self.moving_left==True and self.rect.left>=0:
            self.x-=0.15
            self.rect.centerx=self.x
        if self.moving_up==True and self.rect.top>=0:
            self.y-=0.15
            self.rect.centery=self.y
        if self.moving_down==True and self.rect.bottom<self.screen_rect.bottom:
            self.y+=0.15
            self.rect.centery=self.y