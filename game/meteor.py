import pygame
from .constants import *

class Meteor(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, gravity):
        pygame.sprite.Sprite.__init__(self)
        
        self.image= pygame.Surface( (30,30) )
        self.image.fill( PURPLE )
        
        self.rect=self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y
        self.pos_y= 0
        self.gravity=gravity
        
    def update(self):
        if self.pos_y<HEIGHT:
            self.pos_y+=self.gravity
            self.rect.y= self.pos_y