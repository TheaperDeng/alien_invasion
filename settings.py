import random
class Settings():
    '''Settings stores the setting value of the game'''
    def __init__(self):
        '''initialize the game's setting'''
        self.screen_width=600#screen's width
        self.screen_height=600#screen's height
        self.bg_color=(230,230,230)#screen's background color
        self.moving_speed=0.005
        
        self.bullet_speed=0.3
        self.bullet_height=15
        self.bullet_width=3
        self.bullet_bg_color=(60,60,60)
        self.bullet_limit=15