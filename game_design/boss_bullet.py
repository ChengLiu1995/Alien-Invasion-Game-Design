import pygame
from pygame.sprite import Sprite

class Boss_Bullet(Sprite):
    def __init__(self,ai_settings,screen,boss):
        super(Boss_Bullet,self).__init__()
        #super().__init__(ai_settings,screen,ship)
        self.screen = screen
        #self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.image = ai_settings.boss_bullet
        self.rect = self.image.get_rect()
        self.rect.centerx = boss.rect.centerx
        self.rect.bottom = boss.rect.bottom
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.boss_bullet_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        #pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image,self.rect)
