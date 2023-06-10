import pygame
import Player
import random as rnd 
import Obsticle
import sys
import numpy as np
import time


# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height), vsync=1)
clock = pygame.time.Clock()

# Set up the things
player = Player.Player(100, 50)
obsticles = []
TimeSurvived = 0
passedObsticles = 0
frameCounter = 0
score = 0

def eventListener():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    if player.has_collided(obsticles):
        return False
            
def drawObsticles(screen):
    for o in obsticles:
        o.draw(screen)

def generateObsticle():
    global score
    x = screen_width
    y=np.abs(rnd.random()*screen_height-100)
    speed = (10 + rnd.random()*score/500)
    obsticles.append(Obsticle.Obsticle(x,y,speed))

def updateObsticles():
    global passedObsticles
    for o in obsticles:
        o.update()
        #this can be inserted into the drawObsticels to avoid a second loop
        if o.x < -o.size[0]:
            obsticles.remove(o)
            passedObsticles +=1

time1 = time.time()
# Main game loop
while True:
    frameCounter += 1
    if eventListener() == False:
        break

    #make the things
    #generate an obsticle with a 2% chance
    if rnd.random() >0.98:
        time1 = time.time()
        generateObsticle()

    #update the things 
    TimeSurvived += 1
    player.update()
    updateObsticles()
    if player.restrictVertical(screen_height, OuterBoundsBehavior="kill") == False:
        break
  
    # Clear the screen
    screen.fill((70, 70, 70))    

    #draw the things
    player.draw(screen)
    drawObsticles(screen)

    # Update the screen
    pygame.display.flip()

    #limits the game to 60 FPS, regardless of screen refreshrate 
    clock.tick(60)
    
    score = TimeSurvived+passedObsticles*100
    #the below updates the score every now and then, but never stops calulating it, 
    # because updating the text takes too much calculation that it causes lag if done every frame
    if frameCounter >10:
        pygame.display.set_caption("score: " + str(score))
        frameCounter = 0

#the actual total score is displayed in full after the game has ended
pygame.display.set_caption("score: " + str(score))

# this runs a game loop after the game has ended, essentially a pause function, 
# at 10FPS to decrease the cpu demand
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
    clock.tick(10)