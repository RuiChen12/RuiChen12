import pygame
from random import *

class SmallEnemy(pygame.sprite.pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        #load the image

        self.image = pygame.image.load("enemy_1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend(["enemy_1_died.png"])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]

        #speed
        self.speed = 3
        #borning place
        self.active = True 
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)
    #Make the plane move forward
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    #Make the plane reset
    def reset(self):
        self.active = True 
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-5 * self.height, 0)

class MidEnemy(pygame.sprite.pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        #load the image

        self.image = pygame.image.load("enemy_2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend(["enemy_2_died.png"])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        #speed
        self.speed = 2
        self.active = True 
        #borned place
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)
    #Make the plane move forward
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    #Make the plane reset
    def reset(self):
        self.active = True 
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-10 * self.height, -self.height)


class boss(pygame.sprite.pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        #load the image

        self.image = pygame.image.load("boss_1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend(["boss_1_died.png"])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        #if it is true, it mean the airplane still alive, if it is false, it mean it is died, if it is died, trun the image to died picture.
        self.active = True 
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height, -5 * self.height)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    
    def reset(self):
        #reset it
        self.active = True 
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), randint(-15 * self.height, -5 * self.height )
