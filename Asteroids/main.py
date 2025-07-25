# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import * 

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return # Exits the game loop if window is closed

        screen.fill((0, 0, 0)) # Fill screen with black 
        pygame.display.flip() # Update the display

if __name__ == "__main__":
    main()
