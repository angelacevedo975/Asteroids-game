import pygame
import sys
import os
from .objects import *
import random

from .constants import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.surface= pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(  TITLE )
        self.running= False
        self.clock= pygame.time.Clock()
        self.font= pygame.font.Font(FONT, 24)
        self.dir= os.path.dirname(__file__)
        self.dir_images=os.path.join(self.dir, "assets")
        self.fondo= pygame.transform.scale( pygame.image.load(os.path.join(self.dir_images, "fondo.jpg")) , (WIDTH, HEIGHT) )
        
        
    
    def start(self):
        while not self.running:
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pressed= pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                self.running=True
                    
            font = pygame.font.Font(FONT, 48)
            text=font.render("Asteroids Game", True, (255,255,255))
            text_rect= text.get_rect()
            text_rect.center= ( WIDTH//2, HEIGHT//2 ) 
            
            sub_text= self.font.render("Press Space To Start", True, (255,255,255) )
            sub_text_rect=sub_text.get_rect()
            sub_text_rect.midtop= (WIDTH//2, HEIGHT//2+40)
            
            self.surface.blit(self.fondo, (0,0))
            self.surface.blit(text, text_rect )
            self.surface.blit(sub_text, sub_text_rect)
            
            pygame.display.flip()
            
        self.init()
            
            
    def init(self):
        self.score=0
        self.lives=LIVES
        self.vel_caida=GRAVITY
        self.contador=0
        
        self.generate_elements()
        
        self.run()
        
    def generate_elements(self):
        self.sprites= pygame.sprite.Group()
        self.meteors= pygame.sprite.Group()
        
        self.generate_meteors()
        
        self.player= Player(self.dir_images)
        
        
        self.sprites.add(self.player)
        
        
    def generate_meteors(self):
        for meteor in self.meteors:
            if meteor.pos_y>WIDTH:
                meteor.kill()
                self.lives-=1
                if self.lives<0:
                    self.lives=0
                    self.running=False
        
        
        if len(self.meteors)==0:
            self.contador+=1
            meteor= Meteor(self.dir_images, random.randrange(10, WIDTH-30))
            self.meteors.add(meteor)
            
        if self.contador>=5:
            self.contador=0
            self.vel_caida+=1
    
    def draw(self):
        #Draw the background
        self.surface.blit(self.fondo, (0,0))
        
        
        #Draw the sprites
        self.meteors.draw(self.surface)
        self.sprites.draw(self.surface)
        
        
        #Draw the Score
        score= self.font.render( f"Score: {self.score}", True, (255,255,255) )
        rect_score=score.get_rect()
        rect_score.x, rect_score.y = 10,10
        
        
        #Draw the lives
        lives= self.font.render( f"Lives: {self.lives}", True, (255,255,255))
        rect_lives= lives.get_rect()
        rect_lives.x, rect_lives.y = WIDTH-lives.get_width()-10, 10
        
        self.surface.blit(score, rect_score)
        self.surface.blit(lives, rect_lives)
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            print("left")
            self.player.x-=PLAYER_SPEED
        if pressed[pygame.K_RIGHT]:
            print("right")
            self.player.x+=PLAYER_SPEED
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            
            self.event()
            self.draw()
            self.update()
    
    def update(self):
        
        
        self.generate_meteors()
        self.validate_collition()
        
        self.meteors.update(self.vel_caida)
        self.sprites.update()
        
        pygame.display.flip()
        
        if not self.running:
            self.losing()
        
    def validate_collition(self):
        for meteor in self.meteors:
            sub_mask=( meteor.rect.x-self.player.rect.x, meteor.rect.y-self.player.rect.y )
            if self.player.mask.overlap(meteor.mask, sub_mask):
                meteor.kill()
                self.score+=1
                
                
    def losing(self):
        init_time= pygame.time.get_ticks()
        final_time=0
        while final_time< init_time+5000:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            #self.surface.blit(self.fondo, (0,0))
            
            self.draw()
            
            font = pygame.font.Font(FONT, 48)
            text=font.render("Has Perdido!", True, (255,255,255))
            text_rect= text.get_rect()
            text_rect.center= ( WIDTH//2, HEIGHT//2 )
            
            self.surface.blit(text, text_rect)
            
            pygame.display.flip() 
            final_time=pygame.time.get_ticks()
        self.start()
            
    
               

        
        