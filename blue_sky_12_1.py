import sys
import pygame
from ghost_image import Ghost

#blue sky
#12-1. Blue Sky: Make a Pygame window with a blue background.
'''class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200, 1000))
        self.bg_color=(0, 50, 255)
        pygame.display.set_caption('Blue Sky')
    def blue_sky(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()

blue=BlueSky()
blue.blue_sky()'''

#game character
'''12-2. Game Character: Find a bitmap image of a game character you like or 
convert an image to a bitmap. Make a class that draws the character at the 
center of the screen, then match the background color of the image 
to the background color of the screen or vice versa.'''

class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1000, 800))
        self.bg_color=(0, 0, 0)
        pygame.display.set_caption('Scary Ghost')
        self.ghost=Ghost(self)
    def blue_sky(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.ghost.blitme()
            pygame.display.flip()

blue=BlueSky()
blue.blue_sky()
