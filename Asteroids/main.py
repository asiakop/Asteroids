# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import * 
from player import Player

def main():
    pygame.init() # Pygame initialization

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating game window

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock() # Creating clock to control FPS

    dt = 0 # Time before frames

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return # Exits the game loop if window is closed

        screen.fill((0, 0, 0)) # Fill screen with black 
        player.draw(screen)

        pygame.display.flip() # Update the display
        dt = clock.tick(60) / 1000 # Limit the framerate to 60 FPS and calculating delta to from ms to seconds

if __name__ == "__main__":
    main()
