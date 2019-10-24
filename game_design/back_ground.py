import pygame
from pygame.sprite import Sprite
class BackGround(Sprite):
    def __init__(self,ai_settings,screen,bg_position):
        super(BackGround,self).__init__()
        self.screen = screen
        screen_rect = self.screen.get_rect()
        self.image = ai_settings.background_image
        self.rect = self.image.get_rect()
        self.bg_position = bg_position + ai_settings.screen_height
        self.rect.centerx = screen_rect.centerx
        self.rect.top = screen_rect.top
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.background_speed_factor

    def update(self):
        self.bg_position += self.speed_factor

    def draw_picture(self):
        self.screen.blit(self.image,(0,self.bg_position))
        #print(self.bg_position)
