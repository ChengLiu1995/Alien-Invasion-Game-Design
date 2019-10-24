import sys
from time import sleep
import pygame
from bullet import*
from alien import*
from back_ground import BackGround
from numpy import random
from boss import Boss
from boss_bullet import Boss_Bullet
def check_key_down_events(event,ai_settings,screen,ship,bullets,stats,boss):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_UP:
        ship.moveing_up = True
    elif event.key == pygame.K_DOWN:
        ship.moveing_down = True
    elif event.key == pygame.K_c:
        stats.game_pause = False
        sleep(1)
    elif event.key == pygame.K_p:
        stats.game_pause = True
    elif event.key == pygame.K_SPACE:
        #creat bullets

        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        if stats.new_high:
            with open('high_score.txt','w') as hs:
                hs.write(str(stats.high_score))
        sys.exit()

def check_key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moveing_right= False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left= False
    elif event.key == pygame.K_UP:
        ship.moveing_up = False
    elif event.key == pygame.K_DOWN:
        ship.moveing_down= False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,boss):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event,ai_settings,screen,ship,bullets,stats,boss)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y,boss)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y,boss):
    buttom_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if buttom_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        #sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens,boss,stats)
        ship.center_ship()
        pygame.mouse.set_visible(False)

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,backgrounds,play_button,bg_position,boss,bullets_boss):
    # re draw the screen each loop
    screen.fill(ai_settings.bg_color)
    #screen.blit(ai_settings.background_image,(0,bg_position))
    #screen.blit(ai_settings.background_image,(0,bg_position-2408))
    #screen.blit(ai_settings.background_image,(0,bg_position-2408*2))
    for back in backgrounds:
        back.draw_picture()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for b_bullet in bullets_boss.sprites():
        b_bullet.draw_bullet()
    ship.blitme()

    aliens.draw(screen)
    #print(len(boss))
    for bos in boss.sprites():
        bos.blitme()
        stats.boss = False
    # make the new window clear
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_background(ai_settings,screen,stats,backgrounds,bg_position):
    if len(backgrounds) <1:
        new_back = BackGround(ai_settings,screen,bg_position)
        backgrounds.add(new_back)
    if len(backgrounds) <2:
        new_back = BackGround(ai_settings,screen,bg_position*2)
        backgrounds.add(new_back)
    #print(len(backgrounds))
    backgrounds.update()
    for background in backgrounds.copy():
        if background.bg_position >= ai_settings.screen_height:
            backgrounds.remove(background)



def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss):
    bullets.update()
    bullets_boss.update()
    #print(len(bullets_boss))
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for b_bullet in bullets_boss.copy():
        #if bullet.rect.bottom > screen_rect.bottom:
        if b_bullet.rect.top >= screen_rect.bottom:
            bullets_boss.remove(b_bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets,boss)
    check_boss_bullet_ship_collision(ai_settings,screen,stats,sb,ship,aliens,bullets_boss,boss,bullets)

def check_boss_bullet_ship_collision(ai_settings,screen,stats,sb,ship,aliens,bullets_boss,boss,bullets):
    collisions = pygame.sprite.spritecollideany(ship,bullets_boss)
    if collisions:
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss)
    #print(len(bullets_boss))
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        stats.new_high = True
        sb.prep_high_score()
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets,boss):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,pygame.sprite.collide_mask)
    collisions_b = pygame.sprite.groupcollide(bullets,boss,True,False,pygame.sprite.collide_mask)
    if collisions:
        #print(collisions)
        for alienss in collisions.values():
            #print(aliens)
            #stats.score += ai_settings.alien_points*len(aliens)
            #sb.prep_score()
            for alien in alienss:
                #stats.score += ai_settings.alien_points
                #sb.prep_score()
                stats.score += alien.alien_points

                #print(alien.x)
            #print(aliens.rect.x,aliens.rect.y)
                check_high_score(stats,sb)
                sb.prep_score()
                sb.prep_high_score()
    #for bos in boss.sprites():
            #if pygame.sprite.spritecollideany(bos,bullets):
    if collisions_b:
        for bos in boss.sprites():
                bos.alien_life -= 1
                #print(bos.alien_life)
                if bos.alien_life <1:
                    boss.remove(bos)
                    stats.boss = False
                    stats.score += bos.alien_points

                    check_high_score(stats,sb)
                    sb.prep_score()
                    sb.prep_high_score()

    #print(len(aliens))
    new_alien = True
    for alien in aliens.sprites():
        if alien.rect.y<alien.rect.height*2:
            new_alien = False
    #print(len(aliens))
    if len(aliens) <3 and new_alien:
    #if random.random()>0.7:
        #bullets.empty()
        #ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        creat_fleet(ai_settings,screen,ship,aliens,boss,stats)
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) <ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
def boss_fire_bullet(ai_settings,screen,boss,bullets_boss):
    for bos in boss:
        new_boss_bullet =  Boss_Bullet(ai_settings,screen,bos)
        bullets_boss.add(new_boss_bullet)
def check_boss_shot(ai_settings,screen,boss,bullets_boss,stats):
    if len(bullets_boss) >= stats.boss_bullets_limit:
        stats.boss_shot = False
        stats.reset_boss_bulet()
    if len(bullets_boss) == 0:
        #print('preparinf to shot')
        stats.boss_bullet_time_count -= 1
        if stats.boss_bullet_time_count >= 19:
            thr = random.random()*random.random()  + 0.5
            if random.random()>thr:
                    stats.boss_shot = True
                    #print('shoting----------------------------------------')
                    stats.reset_boss_bulet()
        if stats.boss_bullet_time_count < 0:
                stats.reset_boss_bulet()

    if stats.boss_shot:
        if stats.boss_bullet_time_count >= 20:
            boss_fire_bullet(ai_settings,screen,boss,bullets_boss)
        stats.boss_bullet_time_count -= 1
        if stats.boss_bullet_time_count < 0:
            stats.reset_boss_bulet()
def get_number_aliens(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    print(available_space_x)
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
    #print(available_space_y)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number,stats):
    if random.random()<0.8:
        alien = Alien(ai_settings,screen)
    else:
        alien = Alien2(ai_settings,screen)
    #print(alien.rect.y)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number+(random.random()-0.5)*alien_width*0.5
    alien.rect.y = alien.rect.height-(random.random()-0.5)*alien.rect.height-alien.rect.height*2# + 2*alien.rect.height*row_number
    alien.rect.x = alien.x
    alien.x = float(alien.rect.x)
    alien.y = float(alien.rect.y)
    if random.random()>0.6:
        aliens.add(alien)
def creat_fleet(ai_settings,screen,ship,aliens,boss,stats):
    if stats.boss:
        bos = Boss(ai_settings,screen)
        boss.add(bos)
        stats.boss = False
# make the new window cle
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_aliens(ai_settings,alien_width)
    print(number_aliens_x)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien_height)
    #print(number_rows)
    for row_number in range(1):
        for alien_number in range(number_aliens_x+1):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number,stats)
def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss):
    check_fleet_edges(ai_settings,aliens)
    check_boss_edges(ai_settings,boss)
    aliens.update()
    boss.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss)
    check_aliens_buttom(ai_settings,screen,stats,sb,ship,aliens,bullets,boss)
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
    #for alien in aliens.copy():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def check_boss_edges(ai_settings,boss):
    for bos in boss.sprites():
    #for alien in aliens.copy():
        if bos.check_edges():
            change_boss_direction(ai_settings,boss)
            break
def change_fleet_direction(ai_settings,aliens):
    #for alien in aliens.sprites():
        #alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def change_boss_direction(ai_settings,boss):
    #for alien in aliens.sprites():
        #alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.boss_direction *= -1

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets,boss,bullets_boss):
    if stats.ship_left >0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets_boss.empty()
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens,boss,stats)
        ship.center_ship()
        sleep(0.5)
    else:
        sb.prep_ships()
        aliens.empty()
        boss.empty()
        bullets_boss.empty()
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens,boss,stats)
        ship.center_ship()
        sleep(0.5)
        if stats.new_high:
            with open('high_score.txt','w') as hs:
                hs.write(str(stats.high_score))
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_aliens_buttom(ai_settings,screen,stats,sb,ship,aliens,bullets,boss):
    screen_rect = screen.get_rect()
    #print(len(aliens))
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #print(alien.rect.bottom)
            aliens.remove(alien)

            stats.alien_bot += 1
            stats.count += 1
            #print(stats.count)
            if stats.count >10:
                stats.boss = True
            if len(boss) >= 1:
                stats.reset_count()

            #stats.score -= alien.alien_points*2
            sb.prep_score()
            #print(len(aliens))
