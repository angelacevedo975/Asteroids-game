import pygame
from .constants import *


class Player(pygame.sprite.Sprite):
    
    def __init__(self, top):
        pygame.sprite.Sprite.__init__(self)
        
        self.image= pygame.Surface( (70,15) )
        self.rect= self.image.get_rect()
        
        self.image.fill(AQUA)
        self.rect.x, self.rect.y = WIDTH//2, top- self.rect.height
        self.pos_x=WIDTH//2
        self.puntuacion=0
        
        
    def collide_with(self, meteors):
        for m in meteors:
            if pygame.sprite.collide_rect(self, m):
                m.kill()
                self.puntuacion+=1
                
        
    def update(self):
        if self.pos_x>=0 and self.pos_x<=WIDTH-self.rect.width:
            self.rect.x=self.pos_x
        else:
            if self.pos_x<0:
                self.pos_x=0
            else:
                self.pos_x=WIDTH-self.rect.width