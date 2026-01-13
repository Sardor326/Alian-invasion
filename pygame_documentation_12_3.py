#pygame documentation
'''12-3. Pygame Documentation: We’re far enough into the game now that you 
might want to look at some of the Pygame documentation. The Pygame home 
page is at https://pygame.org, and the home page for the documentation is at 
https://pygame.org/docs. Just skim the documentation for now. You won’t need 
it to complete this project, but it will help if you want to modify Alien Invasion or 
make your own game afterward.'''

#rocket
'''12-4. Rocket: Make a game that begins with a rocket in the center of the screen. 
Allow the player to move the rocket up, down, left, or right using the four arrow 
keys. Make sure the rocket never moves beyond any edge of the screen.'''
import sys
import pygame
from ship_task import ShipTask
from settings_task import Settings_2

class AlienInvasion: 
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        #self.screen=pygame.display.set_mode((self.settings.screed_width, self.settings.screen_height))
        self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screed_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship=ShipTask(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

#keys
'''12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop, 
print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run 
the program and press various keys to see how Pygame responds.'''

class KeyGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings_2()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key Game")

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
        # Show the key that was pressed, then quit if q was pressed.
        #   For more information about the output, see here:
        #   https://www.pygame.org/docs/ref/key.html
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    kg = KeyGame()
    kg.run_game()