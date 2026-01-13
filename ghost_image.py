import pygame

class Ghost:
    def __init__(self, ai_image):
        self.screen=ai_image.screen
        self.screen_rect=ai_image.screen.get_rect()
        self.image=pygame.image.load("C:\\Users\\Hp\\OneDrive\\Desktop\\WORKS\\alien_invasion_python\\images\\ghost_2.bmp")#"C:\Users\Hp\OneDrive\Desktop\WORKS\alien_invasion_python\images\ship.bmp"
        self.rect=self.image.get_rect()
        self.rect.center=self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)