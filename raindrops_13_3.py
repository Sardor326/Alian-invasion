'''#raindrops
''''''13-3. Raindrops: Find an image of a raindrop and create a grid of raindrops. 
Make the raindrops fall toward the bottom of the screen until they disappear.''''''

import sys
import pygame
from raindrop_image import RainDrop
from raindrop_settings import SettingsRain

class RainDropGame:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=SettingsRain()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rain Drop')

        self.drops=pygame.sprite.Group()
        self._create_raindrops()
        #creat drop helper method like creat _grid_drop
    
    def run_drop(self):
        while True:
            self._check_events()
            self.drops.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        
    def _create_raindrops(self):
        drop=RainDrop(self)
        drop_width, drop_height=drop.rect.size

        current_x, current_y= drop_width, drop_height
        while current_y < (self.settings.screen_height - 2*drop_height):
            while current_x < (self.settings.screen_width - 2*drop_width):
                self._create_drop(current_x, current_y)
                current_x +=2*drop_width

            current_x = drop_width
            current_y = 2 * drop_height

    def _create_drop(self, x_position, y_position):
        new_drop=RainDrop(self)
        new_drop.y=y_position
        new_drop.rect.x=x_position
        new_drop.rect.y=y_position
        self.drops.add(new_drop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    dp=RainDropGame()
    dp.run_drop()
'''

import sys
import pygame
from raindrop_image import RainDrop
from raindrop_settings import SettingsRain

class RainDropGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = SettingsRain()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rain Drop")

        self.drops = pygame.sprite.Group()
        self._create_raindrops()

    def run_drop(self):
        while True:
            self._check_events()
            self.drops.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_raindrops(self):
        drop = RainDrop(self)
        drop_width, drop_height = drop.rect.size

        current_y = drop_height
        while current_y < (self.settings.screen_height - 2 * drop_height):
            current_x = drop_width
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        new_drop = RainDrop(self)
        new_drop.y = y_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.drops.add(new_drop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = RainDropGame()
    game.run_drop()

#steady rain
'''13-4. Steady Rain: Modify your code in Exercise 13-3 so when a row of raindrops disappears off the bottom of the screen, a new row appears at the top of 
the screen and begins to fall.'''

'''import sys
import pygame
from raindrop_image import RainDrop
from raindrop_settings import SettingsRain


class RainDropGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = SettingsRain()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Steady Rain")

        self.drops = pygame.sprite.Group()
        self._create_raindrops()

    def run_drop(self):
        while True:
            self._check_events()
            self.drops.update()

            # NEW → check if any drop hits the bottom
            if self._check_rain_bottom():
                self._create_new_row()

            self._update_screen()
            self.clock.tick(60)

    # ---------------------------- EVENTS ----------------------------
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    # ---------------------------- CREATE GRID ----------------------------
    def _create_raindrops(self):
        drop = RainDrop(self)
        drop_width, drop_height = drop.rect.size

        current_y = drop_height
        while current_y < (self.settings.screen_height - 2 * drop_height):
            current_x = drop_width
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x, y):
        new_drop = RainDrop(self)
        new_drop.y = y
        new_drop.rect.x = x
        new_drop.rect.y = y
        self.drops.add(new_drop)

    # ---------------------------- STEADY RAIN LOGIC ----------------------------
    def _check_rain_bottom(self):
        """Return True if any raindrop touches the bottom."""
        for drop in self.drops.sprites():
            if drop.rect.top >= self.settings.screen_height:
                return True
        return False

    def _create_new_row(self):
        """Create one new row at the top."""
        drop = RainDrop(self)
        drop_width, drop_height = drop.rect.size

        x = drop_width
        y = drop_height  # always top row

        while x < (self.settings.screen_width - 2 * drop_width):
            self._create_drop(x, y)
            x += 2 * drop_width

    # ---------------------------- UPDATE SCREEN ----------------------------
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = RainDropGame()
    game.run_drop()'''
