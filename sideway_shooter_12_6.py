#sideways shooter
'''12-6. Sideways Shooter: Write a game that places a ship on the left side of the 
screen and allows the player to move the ship up and down. Make the ship fire 
a bullet that travels right across the screen when the player presses the spacebar. 
Make sure bullets are deleted once they disappear off the screen.

13-5. Sideways Shooter Part 2: We’ve come a long way since Exercise 12-6, 
Sideways Shooter. For this exercise, try to develop Sideways Shooter to the 
same point we’ve brought Alien Invasion to. Add a fleet of aliens, and make 
them move sideways toward the ship. Or, write code that places aliens at random positions along the right side of the screen and then sends them toward 
the ship. Also, write code that makes the aliens disappear when they’re hit.'''

'''13-6. Game Over: In Sideways Shooter, keep track of the number of times the 
ship is hit and the number of times an alien is hit by the ship. Decide on an 
appropriate condition for ending the game, and stop the game when this situation occurs.'''

import sys
from time import sleep

import pygame

from settings_sideway_task import SettingsSideway
from ship_sidaway_task import ShipSideway
from bullet_sideway_task import BulletSideway
from alien_sideway_task import AlienSideway
from game_stats import GameStats
class AlienInvasionSideway: 
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=SettingsSideway()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        '''self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screed_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height'''
        pygame.display.set_caption('Alien Invasion')
        self.stats=GameStats(self)
        self.ship=ShipSideway(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._creat_fleet()
        self.game_active=True

    def run_game(self):
        while True:
            if self.game_active:
                self._check_events()
                self.ship.update()
                self.bullets.update()
                self._update_bullet()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event) 
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet=BulletSideway(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        self.aliens.update()

        if len(self.aliens) == 0:
            self._creat_fleet()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()
    


    def _check_bullet_alien_collisions(self):
        collisions=pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -=1
            self.bullets.empty()
            self.aliens.empty()
            self._creat_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active=False
            

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break



    def _creat_fleet(self):
        alien=AlienSideway(self)
        alien_width, alien_height = alien.rect.size
        current_x = self.settings.screen_width - alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height - 2 * alien_height ):
            current_x = self.settings.screen_width - alien_width
            while current_x > 0 :
                self._creat_alien(current_x, current_y)
                current_x -=5 * alien_width
            start_x=current_x 
            current_y += 2 * alien_height



    def _creat_alien(self, x_position, y_position):
        new_alien=AlienSideway(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _fleet_move(self):
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasionSideway()
    ai.run_game()
