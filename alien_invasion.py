import sys
import pygame
from settings import Settings
from dog import Dog
import game_function as gf
from pygame.sprite import Group
from alien import Alien
import time
from time import sleep
def run_game():
    pygame.init()#initial pygame
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))#set the size of the window to 800*600
    dog=Dog(screen,game_settings)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(game_settings,screen,aliens)
    pygame.display.set_caption("Time Collection")#set title
    time_before=time.time()
    while True:
        time_now=time.time()
        if time_now-time_before>=2:
            gf.create_fleet(game_settings,screen,aliens)
            time_before=time.time()
        
        gf.clickevent(dog,screen,game_settings,bullets)
        gf.refleshscreen(screen,dog,game_settings,bullets,aliens)
        
        
        
run_game()