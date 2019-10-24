import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #self.image = pygame.image.load('images/alien2.png')
        self.image = ai_settings.alien_img
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.y += self.ai_settings.fleet_drop_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True
