import pygame
from .constants import *

class Platform(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image= pygame.Surface( (WIDTH, 30) )
        self.image.fill( BROWN )
        self.rect= self.image.get_rect()
        self.rect.x, self.rect.y = 0,HEIGHT-30
        
    def collide_with(self, meteors):
        for m in meteors:
            if pygame.sprite.collide_rect(self, m):
                m.kill()
                return True