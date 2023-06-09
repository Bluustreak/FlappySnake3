import pygame
import Player
import random as rnd 
import Obsticle
import sys


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
    if player.has_collided(obsticles, screen_height):
        return False
            

def drawObsticles(screen):
    for o in obsticles:
        o.draw(screen)

def generateObsticle():
    x = screen_width
    y=rnd.random()*screen_height
    speed = (2 + rnd.random()*10)
    obsticles.append(Obsticle.Obsticle(x,y,speed))

def updateObsticles():
    for o in obsticles:
        o.update()
        #this can be inserted into the drawObsticels to avoid a second loop
        if o.x < 0:
            obsticles.remove(o)
            passedObsticles +=1
        



run = True
# Main game loop
while True:
    if eventListener() == False:
        break

    #make the things
    if rnd.random()>0.97:
        generateObsticle()

    # Clear the screen
    screen.fill((70, 70, 70))

    #draw the things
    player.draw(screen)
    drawObsticles(screen)

    #update the things 
    player.update()
    #updateObsticles()
    for o in obsticles:
        o.update()
        #this can be inserted into the drawObsticels to avoid a second loop
        if o.x < 0:
            obsticles.remove(o)
            passedObsticles +=1

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
    score = score +1
    pygame.display.set_caption("score: " + str(score+passedObsticles*100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   