from turtle import delay
import pygame
import sys
import traceback
from enemy import boss
import myplane
import enemy
from pygame.locals import *
from random import *
# Initialization of pygame
pygame.init()
pygame.mixer.init()
#Background Setting
bg_size = width, height = 1048, 768
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Aircraft Fight Game")

background = pygame.image.load("scene.png").convert()


#Load the Music

#Background music
pygame.mixer.music.load("backgroundmusic.wav")
pygame.mixer.music.set_volume(0.2)
#Shot sound
shot_sound = pygame.mixer.Sound("shot.wav")
shot_sound.set_volume(0.2)
#the boom of enemy aircraft died
boom_sound = pygame.mixer.Sound("boom.wav")
boom_sound.set_volume(0.2)
#boss bmg
boss_bgm = pygame.mixer.Sound("bossbgm.wav")
boss_bgm.set_volume(0.2)
#finished sound
done_sound = pygame.mixer.Sound("done.wav")
done_sound.set_volume(0.2)

#generate enemy
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_boss(group1, group2, num):
    for i in range(num):
        e3 = enemy.boss(bg_size)
        group1.add(e3)
        group2.add(e3)


#Play the background music'
def main():
    pygame.mixer.music.play(-1)
    #the borned of our airplane
    protagonist = myplane.MyPlane(bg_size)

    #the borned of enemy
    enemies = pygame.sprite.Group()

    #the small enemy
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)

    #the middle enemy
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 10)

    #the boss
    boss = pygame.sprite.Group()
    add_boss(boss, enemies, 2)

    #destroyed image import
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    protagonist_destroy_index = 0

    #set the frame time
    clock = pygame.time.Clock()
    running = True 
    
    #the quit system, 
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        #Check the key press
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            protagonist.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            protagonist.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            protagonist.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            protagonist.moveRight()
        
        #Use the background
        screen.blit(background,(0, 0))
        #detect if the protagonist is bumped
        enemie_down = pygame.sprite.spritecollide(protagonist, enemies, False)
        if enemie_down:
            protagonist.active = False
            for e in enemie_down:
                e.active = False

        #to get our airplane
        if protagonist.active:
            screen.blit(protagonist.image, protagonist.rect)
        else:
            boom_sound.play()
            if not(delay % 3):
                screen.blit(each.destroy_image[protagonist_destroy_index], each.rect)
                    # if 1 / 1 = 0, there is no remainder, which mean the image play is done.
                protagonist_destroy_index = (protagonist_destroy_index + 1) % 1
                if protagonist_destroy_index == 0:
                    print("game over")
                    running = False
        
        #to get boss
        for each in boss:
            #check if the airplane is alive
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                boom_sound.play()
                if not(delay % 3):
                    screen.blit(each.destroy_image[e3_destroy_index], each.rect)
                    # if 1 / 1 = 0, there is no remainder, which mean the image play is done.
                    e3_destroy_index = (e3_destroy_index + 1) % 1
                    if e3_destroy_index == 0:
                        each.reset()

        
        for each in mid_enemies:
            #check if the airplane is alive
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                boom_sound.play()
                if not(delay % 3):
                    screen.blit(each.destroy_image[e2_destroy_index], each.rect)
                    # if 1 / 1 = 0, there is no remainder, which mean the image play is done.
                    e2_destroy_index = (e2_destroy_index + 1) % 1
                    if e2_destroy_index == 0:
                        each.reset()

        for each in small_enemies:
            #check if the airplane is alive
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                boom_sound.play()
                if not(delay % 3):
                    screen.blit(each.destroy_image[e1_destroy_index], each.rect)
                    # if 1 / 1 = 0, there is no remainder, which mean the image play is done.
                    e1_destroy_index = (e1_destroy_index + 1) % 1
                    if e1_destroy_index == 0:
                        each.reset()
        #flip the screen
        pygame.display.flip()
        
        clock.tick(60)

# If it is normal quit the screen or game, then we just skip it, but if there is a error, then it will report and print out.
# the reason i do this, because i don't want if i clicked file, but it didn't pops out. I need to know why it is error.
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        # only if i put something to the message, it will gone.
        input()