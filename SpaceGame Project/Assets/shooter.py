import pygame
from random import *
import os

pygame.init()
clock = pygame.time.Clock()
FPS = 60

win_width = 750

global win_height
win_height =700

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Space Shooter")
background = pygame.transform.scale(pygame.image.load("SpaceBG2.jpg"),(win_width, win_height))
window.blit(background,(0, 0))

pygame.font.init()

pygame.mixer.init()
pygame.mixer.music.load("SpaceMusic.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

#The SpaceHero-Sprite Class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y):
        super().__init__()
        self.image=player_image
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_image=pygame.transform.scale(pygame.image.load("spaceSa.png"), (100, 90))
player_x=280
player_y=400
player_speed=10
GameS=GameSprite(player_image,player_speed,player_x,player_y)

mini_image=pygame.transform.scale(player_image , (30, 30))
mini_image2=pygame.transform.scale(player_image , (30, 30))
mini_image3=pygame.transform.scale(player_image , (30, 30))

#The asteroids Class
class Asteroids(pygame.sprite.Sprite):
    def __init__(self,asteroid_image,asteroid_speed,asteroid_x,asteroid_y):
        super().__init__()
        self.image=asteroid_image
        self.speed=asteroid_speed
        self.rect=self.image.get_rect()
        self.rect.x= asteroid_x
        self.rect.y= asteroid_y
    def reset2(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Asteroid(Asteroids):
    def update(self):
        self.rect.y += self.speed
        self.rect.x -= self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_width+50)
            self.rect.y = randint(50,150)
        window.blit(self.image, (self.rect.x, self.rect.y))

asteroid_image=pygame.transform.scale(pygame.image.load("asteroid.png"), (50, 60))
asteroid_speed=randint(4,7)
asteroid_x=-150
asteroid_y=400

Meteor=Asteroid(asteroid_image,randint(4,10),asteroid_x,asteroid_y)

asteroids = pygame.sprite.Group()

asteroid1=Asteroid(asteroid_image,randint(4,10),150,asteroid_y)
asteroid2=Asteroid(asteroid_image,randint(4,10),130,asteroid_y)
asteroid3=Asteroid(asteroid_image,randint(4,10),100,asteroid_y)
asteroid4=Asteroid(asteroid_image,randint(4,10),160,asteroid_y)
 
asteroids.add(asteroid1,asteroid2,asteroid3,asteroid4)

gameover=pygame.transform.scale(pygame.image.load("gameover.png"), (300, 100))

#The Invaders Class
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self,player_image2,player_speed2,player_x2,player_y2,g):
        super().__init__()
        self.image=player_image2
        self.speed=player_speed2
        self.rect=self.image.get_rect()
        self.rect.x= player_x2
        self.rect.y= player_y2
        self.g=g
    def reset2(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Enemy(EnemySprite):
    def update(self):
        self.rect.y += self.speed
        for i in invaders:
            if self.rect.y > win_height:
                self.rect.x = randint(80, win_width - 80)
                self.rect.y = 0
                self.g=self.g + 1    
            if self.g==1:
                mini_image.fill((255,255,255,0))
            elif self.g==2:
                mini_image2.fill((255,255,255,0))
            elif self.g>=3:
                mini_image3.fill((255,255,255,0))
                i.kill()
                pygame.mixer.music.stop()
                for a in asteroids:
                    a.kill()
                player_image.fill((255,255,255,0))
                bullet_image.fill((255,255,255,0))
                      
        window.blit(self.image, (self.rect.x, self.rect.y))

player_image2=pygame.transform.scale(pygame.image.load("invaderGa.png"), (120, 90))
player_x2=200
player_y2=20
player_speed2=randint(4,10)
global g
g=0

EnemyS=Enemy(player_image2,player_speed2,player_x2,player_y2,g)

invaders = pygame.sprite.Group()

invader2=Enemy(player_image2,randint(4,8),player_x2,player_y2,g)
invader3=Enemy(player_image2,randint(4,8),player_x2,player_y2,g)
invader4=Enemy(player_image2,randint(4,8),player_x2,player_y2,g)

invaders.add(invader2,invader3,invader4)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        window.blit(self.image, (self.rect.x, self.rect.y))
            
bullet_image=pygame.transform.scale(pygame.image.load("lazerB.png"), (60, 50))
bullet_x=280
bullet_y=400
bullet_speed=-20

bulletGr=pygame.sprite.Group()

c=0
Hits=0   

youwin=pygame.transform.scale(pygame.image.load("Youwin.png"), (300, 100))

game =True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    window.blit(background,(0, 0))
    window.blit(GameS.image,(player_x, player_y))
    window.blit(mini_image,(10,20))
    window.blit(mini_image2,(40,20))
    window.blit(mini_image3,(70,20))

    for i in invaders:
        if EnemyS.rect.y > win_height:
            EnemyS.rect.x = randint(80, win_width - 80)
            EnemyS.rect.y = 0
            g=g+1
            print(g)

    c=c+1

    #Keys for moving spaceship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 5:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x <win_width - 80:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 5:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < win_height - 80:
        player_y += player_speed


    if c%12==0:
        if keys[pygame.K_SPACE]:
            b=Bullet(bullet_image,player_speed,player_x,player_y)
            bullet_snd= pygame.mixer.Sound("laser.wav")
            bullet_snd.play()
            
            bulletGr.add(b)

    
    for b in bulletGr:
        if pygame.sprite.spritecollide(b,invaders,True):
            b.kill()
            Hits=Hits+1
            e=Enemy(player_image2,randint(4,8),randint(20,500),player_y2,g)
            invaders.add(e)
            explosion_snd=pygame.mixer.Sound("explosionS.mp3")
            inicial_som = pygame.mixer.Sound((os.path.join('explosionS.mp3')))
            explosion_snd.play()

        if pygame.sprite.spritecollide(b,asteroids,True):
            b.kill()
            a=Asteroid(asteroid_image,randint(4,10),asteroid_x,asteroid_y)
            asteroids.add(a)
            explosion_snd=pygame.mixer.Sound("explosionS.mp3")
            inicial_som = pygame.mixer.Sound((os.path.join('explosionS.mp3')))
            explosion_snd.play()

    font1 = pygame.font.Font(None, 30)
    text_hits = font1.render("Hits: " + str(Hits), 1, (200, 50, 255))
    window.blit(text_hits,(20,60))

    if Hits>=100:
        window.blit(youwin,(200,300))
        pygame.mixer.music.stop()
        bullet_snd.stop()
        player_image.fill((255,255,255,0))
        bullet_image.fill((255,255,255,0))
        for i in invaders:
            i.kill()
        for a in asteroids:
            a.kill()
    
    invaders.update()
    asteroids.update()
    bulletGr.update()
    
    clock.tick(FPS)
    pygame.display.update()