import pygame
import Player
import random as rnd 
import Obsticle
import sys
import numpy as np


# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set up the things
player = Player.Player(100, 250)
obsticles = []
score = 0
passedObsticles = 0


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
    speed = (10 + rnd.random())
    obsticles.append(Obsticle.Obsticle(x,y,speed+score/1000))

def updateObsticles():
    global passedObsticles
    for o in obsticles:
        o.update()
        #this can be inserted into the drawObsticels to avoid a second loop
        if o.x < -o.size[0]:
            obsticles.remove(o)
            passedObsticles +=1


frameCounter = 0


# Main game loop
while True:
    if eventListener() == False:
        break

    #make the things
    if frameCounter >3600-rnd.random()*100 - score:
        frameCounter = 0
        generateObsticle()




    #update the things 
    player.update()
    updateObsticles()
    player.restrictVertical(screen_height)

    # Clear the screen
    screen.fill((70, 70, 70))

    #draw the things
    player.draw(screen)
    drawObsticles(screen)

    score = score +1
    pygame.display.set_caption("score: " + str(score+passedObsticles*100))
    frameCounter += clock.get_fps()

    # Update the screen
    pygame.display.flip()
    clock.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   