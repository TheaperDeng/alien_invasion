import sys
import pygame
from bullet import Bullet
from alien import Alien
import random
def clickevent(dog,screen,game_settings,bullets):
    for event in pygame.event.get():#get what users do 
        if event.type == pygame.QUIT:#quit
            sys.exit()
        elif event.type == pygame.KEYDOWN:#move right and left
            checkKEYDOWN(event,dog,game_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            checkKEYUP(event,dog)
          
def refleshscreen(screen,dog,game_settings,bullets,aliens):
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    aliens.draw(screen)
        
    update_dog(dog)
    update_bullets(bullets)
    update_aliens(bullets,aliens,dog)
    pygame.display.flip()
    
    
def checkKEYDOWN(event,dog,game_settings,screen,bullets):
    if event.key==pygame.K_RIGHT:
        dog.moving_right=True
    elif event.key==pygame.K_LEFT:
        dog.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(dog,game_settings,screen,bullets)
    elif event.key==pygame.K_UP:
        dog.moving_up=True
    elif event.key==pygame.K_DOWN:
        dog.moving_down=True
    elif event.key==pygame.K_q:
        sys.exit()

def fire_bullet(dog,game_settings,screen,bullets):
    if len(bullets)<=game_settings.bullet_limit:
        new_bullet=Bullet(game_settings,screen,dog)
        bullets.add(new_bullet)
            

def checkKEYUP(event,dog):
    if event.key==pygame.K_RIGHT:
        dog.moving_right=False
    elif event.key==pygame.K_LEFT:
        dog.moving_left=False
    elif event.key==pygame.K_UP:
        dog.moving_up=False
    elif event.key==pygame.K_DOWN:
        dog.moving_down=False

def update_aliens(bullets,aliens,dog):
    aliens.update()
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if pygame.sprite.spritecollideany(dog,aliens):
        pass
        #print("Target Down!!!")
        

def update_dog(dog):
    dog.update()
    dog.blitme()
        
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def create_fleet(game_settings,screen,aliens):
    alien=Alien(game_settings,screen)
    alien_width=alien.rect.width
    available_space_x=game_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x / (2*alien_width))
    
    for alien_number in range(number_aliens_x-3):
        alien=Alien(game_settings,screen)
        #alien.x=alien_width+2*alien_width*alien_number
        alien.x=random.randint(alien_width,game_settings.screen_width-50)
        alien.rect.x=alien.x
        aliens.add(alien)
