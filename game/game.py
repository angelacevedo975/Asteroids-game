import pygame
from .constants import *
import sys
from .player import Player
from .platform import Platform
from .meteor import Meteor
import random

class Game:
    
    def __init__(self):
        pygame.init()
        self.surface= pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(  TITLE )
        self.running= False
        self.clock= pygame.time.Clock()
        self.font= pygame.font.Font(FONT, 24)
        
    def start(self):
        self.new()
    
    def new(self):
        while(not self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.surface.fill(  PURPLE )
            
            text=self.font.render("Presiona espacio para comenzar", True, WHITE)
            rect= text.get_rect()
            rect.center=(WIDTH//2, HEIGHT//2)
            self.surface.blit(text, rect)
            
            pressed=pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.running=True
            
            pygame.display.flip()
        
        
        self.lives=5
        self.gravity=GRAVITY
        self.num=0
        self.generate_elements()
        self.run()
        
    def generate_elements(self):
        self.sprites= pygame.sprite.Group()
        self.wave= pygame.sprite.Group()
        
        self.platform=Platform()
        self.player=Player(self.platform.rect.top)
        self.generate_wave()
        
        self.sprites.add(self.player)
        self.sprites.add(self.platform)
        
        
    def generate_wave(self):
        if len(self.wave)<1:
            
                wave=Meteor(
                    random.randrange(0, WIDTH-40),
                    random.randrange(-HEIGHT, -40),
                    self.gravity
                    )
                self.wave.add(wave)
                self.num+=1
                if self.num>9:
                    self.gravity+=1
                    self.num=0
        
    
    def draw_score(self):
        pass
    
    def run(self):
        while self.running:
            self.clock.tick(30)
            
            self.events()
            self.draw()
            self.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running=False
                sys.exit()
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.player.pos_x-=SPEED
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.player.pos_x+=SPEED
        
    
    def draw(self):
        
        self.surface.fill( BLACK  )
        
        
        self.sprites.draw(self.surface)
        self.wave.draw(self.surface)
        
        text=self.font.render("Score: "+str(self.player.puntuacion)+"   x "+str(self.lives), True, WHITE)
        rect= text.get_rect()
        rect.midtop=(WIDTH//2, 30)
        self.surface.blit(text, rect)

    
    def update(self):
        pygame.display.flip()
        self.sprites.update()
        self.wave.update()
        
        self.generate_wave()
        self.player.collide_with(self.wave)
        if self.platform.collide_with(self.wave):
            self.lives-=1
            print(self.lives)
            
        if self.lives<0:
            self.running=False
            self.new()
            
        

        
        