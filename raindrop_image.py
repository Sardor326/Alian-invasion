'''import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen=rd_game.screen
        self.screen=rd_game.settings

        self.image=pygame.image.load("C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\ship.bmp")
        #self.image=pygame.transform.scale(image, (20, 20))
        self.rect = self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.y=float(self.rect.y)

    def update(self):
        self.y +=self.settings.raindrop_speed
        self.rect.y = self.y'''

import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()

        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load your image (use a raindrop if you have it)
        image = pygame.image.load(
            "C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\raindrop_1.bmp"
        )
        self.image=pygame.transform.scale(image, (20, 20))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Track exact vertical position
        self.y = float(self.rect.y)

    def update(self):
        # Move raindrop downward
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

        # Remove when it leaves screen
        if self.rect.top > self.settings.screen_height:
            self.kill()
