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
player = Player.Player(100, 250)
obsticles = []
score = 0
passedObsticles = 0
frameCounter = 0

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
    speed = (10 + rnd.random()*score/100)
    obsticles.append(Obsticle.Obsticle(x,y,speed+score/1000))

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
    t1 = time.perf_counter()
    if eventListener() == False:
        break

    #make the things
    if time.time()-time1 > 1:
        time1 = time.time()
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
    #pygame.display.set_caption("score: " + str(score+passedObsticles*100))
    
    

    # Update the screen
    pygame.display.flip()
    t2 = time.perf_counter()
    dt = t2-t1
    frametime=1000/59.93
    delay=frametime-dt
    time.sleep((delay/1e3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   