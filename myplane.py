import pygame
#we will define a sprite class, because we want to do the collision detection
class MyPlane(pygame.sprite.Sprite):
    #we need add the bg_size because we don't want the aircraft go out of the screen.
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("protagonist.png").convert_alpha()
        self.rect = self.image.get_rect()
        #create a list to save the destroyed image
        self.destroy_image = []
        #and then we use the extend method to insert the image, otherwise when airplane died, it will not show up.
        self.destroy_image.extend([pygame.image.load("protagonist_died.png")])
        self.width, self.height = bg_size[0], bg_size[1]
        #We want the airplane borned in the middle, so we divided by 2, and we want some gapped to the bottom, so we minus 60.
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height) - 60
        #set the speed
        self.speed = 10
        self.active = True 
    #then we want the airplane to move
    #move up
    def moveUp(self):
        #first we want to determine if the airplane will go out of the screen
        #this mean, if the airplane reach to the side of the screen, it will stop, because of the -=.
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
            
    #move down
    def moveDown(self):
        if self.rect.bottom < self.height:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height
            
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
    