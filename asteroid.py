import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update(self, dt):
        # (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
        self.position += (self.velocity * dt)