import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        self.screen=star_game.screen

        image=pygame.image.load("C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\star_2.bmp")
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()

'''        self.rect.x=self.rect.width
        self.rect.y=self.rect.height'''