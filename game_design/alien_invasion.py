import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import*
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from back_ground import BackGround
from boss import Boss
from boss_bullet import Boss_Bullet
def run_game():
    #initial the game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"Play")
    #print(play_button.rect.centerx,play_button.rect.center)
    ship = Ship(ai_settings,screen)
    aliens = Group()
    bullets = Group()
    bullets_boss = Group()
    boss = Group()
    backgrounds = Group()
    #gf.creat_fleet(ai_settings,screen,ship,aliens,boss)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #print(ship.screen_rect.centerx)
    #print(ship.screen_rect.bottom)
    #bg_color = (230,230,230)
    # start the loop of the game
    #bg_position = -2408 + ai_settings.screen_height
    bg_position = -2408
    count = int(0)
    stats.game_active = False
    while True:
        #supervise the mouse and keyboard events
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,boss)
        if stats.game_active:
            if not stats.game_pause:
                gf.check_boss_shot(ai_settings,screen,boss,bullets_boss,stats)
                ship.update()
                gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss)
                gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss)
                gf.update_background(ai_settings,screen,stats,backgrounds,bg_position)
        #print(len(bullets))
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,backgrounds,play_button,bg_position,boss,bullets_boss)
        #bg_position += 2

run_game()
