import pygame
from pygame.sprite import Sprite
class Boss(Sprite):
    def __init__(self,ai_settings,screen):
        super(Boss,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.alien_points = 20
        self.alien_life = 10
        self.image = ai_settings.boss_img
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top+20
        #self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.boss_direction
        self.y += 0
        self.rect.x = self.x
        self.rect.y = self.y
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
