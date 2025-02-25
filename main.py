# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *



def main():
    pygame.init()
    print("Starting asteroids!")
    #This sets the screen size to var's set in constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    #this while loop is the main game loop, we created a clock object above this to use to setup and limit the fps, the flip method redraws the scene
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt =  clock.tick(60) / 1000
        


    
if __name__ == "__main__":
    main()
