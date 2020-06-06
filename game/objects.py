import pygame
import os
from .constants import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, images_dir):
        super().__init__()
        
        route= os.path.join(images_dir, "ship.png")
        self.image= pygame.transform.scale( pygame.image.load(route), (125,125) )
        
        self.rect=self.image.get_rect()
        self.rect.x= WIDTH//2
        self.rect.y= HEIGHT-self.rect.height
        
        self.x=self.rect.x
        self.mask=pygame.mask.from_surface(self.image, 127)
        
        
    def update(self):
        if self.x<0:
            self.x=0
        if self.x> WIDTH- self.rect.width:
            self.x= WIDTH- self.rect.width
        
        self.rect.x= self.x
        

class Meteor(pygame.sprite.Sprite):
    
    def __init__(self, images_dir, pos_x):
        super().__init__()
        
        route= os.path.join(images_dir, "meteor.png")
        self.image= pygame.transform.scale( pygame.image.load(route), (65,65) )
        self.rect= self.image.get_rect()
        self.pos_x=pos_x
        self.pos_y=0-self.rect.height
        self.rect.x= pos_x
        self.rect.y= self.pos_y
        self.mask=pygame.mask.from_surface(self.image, 127)
        
    def update(self, vel_caida):
        self.pos_y+=vel_caida
        self.rect.y=self.pos_y
        
        
        
        
        