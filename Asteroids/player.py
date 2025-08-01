import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.shoot_timer = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # To the left
        if keys[pygame.K_d]:
            self.rotate(dt) # To the right
        if keys[pygame.K_w]:
            self.move(dt) # Up
        if keys[pygame.K_s]:
            self.move(-dt) # Down
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt   

    def shoot(self):
        if self.shoot_timer > 0:
            return # Prevent shooting if cooldown is active
        
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown
          