'''#stars
#13-1. Stars: Find an image of a star. Make a grid of stars appear on the screen
import sys
import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.image=pygame.image.load('"C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\star_2.bmp"')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.x)



class Stars:
    def __init__(self):
        pygame.init()

        #sreen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0, 0, 0)

        self.stars=pygame.sprite.Group()
        self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        #star settings
    def run_star(self, event):
        while True:
            self._update_screen()
            if event.key == pygame.K_q:
                sys.exit()

    def _creat_star(self, x_position, y_position):
        new_star=Star(self)
        new_star.x=x_position
        new_star.rect.x=x_position
        new_star.rect.y=y_position
        self.stars.add(new_star)
                    
    def star_grid(self):
        star=Star(self)
        star_width, star_height=star.rect.size
        current_x, current_y=star_width, star_height
        while current_y < (self.screen_height - 3*star_height):
            while current_x < (self.screen_width - 2*star_width):
                self._creat_star(current_x, current_y)
                current_x +=2*star_width
            current_x = star_width
            current_y += 2*star_height

                    
    def _update_screen(self):
        self.star.blitme()
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__=='__main__':
    ai=Stars()
    ai.run_star()


'''

'''import sys

import pygame

from star_settings import Settings
from star_image import Star


class StarsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """Create a sky full of stars."""
        # Create a star and keep adding stars until there's no room left.
        #   Spacing between stars is two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = 2 * star_width
            current_y += 2 * star_height
        print(star_width, star_height)

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sg = StarsGame()
    sg.run_game()
'''

#better_stars

import sys
from random import randint

import pygame

from star_settings import Settings
from star_image import Star


class StarsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_stars(self):
        """Create a sky full of stars."""
        # Create a star and keep adding stars until there's no room left.
        #   Spacing between stars is two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size

        x_max = self.settings.screen_width - star_width
        y_max = self.settings.screen_height - star_height
        for _ in range(500):
            x_position = randint(star_width, x_max)
            y_position = randint(star_height, y_max)
            self._create_star(x_position, y_position)

    def _create_star(self, x_position, y_position):
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position

        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sg = StarsGame()
    sg.run_game()


