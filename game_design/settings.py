import pygame
class Settings():
    """saving all the classes"""
    def __init__(self):
        """initial game setting"""
        self.screen_width = 800
        self.screen_height = 700
        self.bg_color = (185,127,87)
        #self.background_image = pygame.image.load('images/Capture2.png')
        self.background_image = pygame.image.load('images/BG3.png')
        self.alien_img1 = pygame.image.load('images/enemy1.png')
        self.alien_img2 = pygame.image.load('images/enemy2.png')
        self.boss_img = pygame.image.load('images/boss1.png')
        self.bullet= pygame.image.load('images/bullet.png')
        self.boss_bullet =  pygame.image.load('images/enemy_bullet3.png')
        self.ship_limit = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3*3
        self.fleet_drop_speed = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.alien_points = 50
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5*3
        self.bullet_speed_factor = 3*2
        self.boss_bullet_speed_factor = 3*3
        self.alien_speed_factor = 1
        self.fleet_direction = 0
        self.boss_direction = 1
        self.background_speed_factor = 2
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.boss_bullet_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
