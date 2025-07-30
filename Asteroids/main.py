# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # Pygame initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating game window
    clock = pygame.time.Clock() # Creating clock to control FPS
    
    #Creating groups/containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Seting both containers for the Player
    Player.containers =(updatable, drawable)

    #Seting container for asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    #Seting container for AsteroidField
    AsteroidField.containers = (updatable)

    #Seting container for shots
    Shot.containers = (shots, updatable, drawable)

    #Creating a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Creating an AsteroidField
    asteroid_field = AsteroidField() 

    dt = 0 # Time before frames
    
    # Game loop
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return # Exits the game loop if window is closed
        
        updatable.update(dt) # Update of all updatable objects 

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
                if player.collision(asteroid):
                    print("Game over!") # Print message if player collides with an asteroid
                    pygame.quit()
                    exit()
        
        # Check for collisions between shot and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill() # Remove both shot and asteroid if they collide
        
        # Draw all drawable objects
        screen.fill("black") # Fill screen with black 
        for object in drawable: 
            object.draw(screen)      
        pygame.display.flip() # Update the display
        
        dt = clock.tick(60) / 1000 # Limit the framerate to 60 FPS and calculating delta to from ms to seconds

if __name__ == "__main__":
    main()
