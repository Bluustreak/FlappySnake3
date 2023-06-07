import pygame
import Player
import random as rnd
import Obsticle
import sys

def eventListener():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

def drawObsticles(screen):
    for o in obsticles:
        o.draw(screen)

def generateObsticle():
    x = screen_width
    y=rnd.random()*screen_height
    speed = (5 + rnd.random()*10)
    obsticles.append(Obsticle.Obsticle(x,y,speed))

def updateObsticles():
    for o in obsticles:
        o.update()
        #this can be inserted into the drawObsticels to avoid a second loop
        if o.x < 0:
            obsticles.remove(o)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Set up the things
player = Player.Player(screen_width // 5, screen_height // 2)
obsticles = []
score = 0


# Main game loop
while True:
    eventListener()

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
    updateObsticles()

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
