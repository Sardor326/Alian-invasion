import pygame
from pygame.sprite import Sprite
class AlienSideway(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.image=pygame.image.load("C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\alien.bmp")
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
    
    def update(self):
        self.x -=self.settings.alien_speed
        self.rect.x = self.x