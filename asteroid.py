import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            va = self.velocity.rotate(angle)
            vb = self.velocity.rotate(-angle)
            nradius = self.radius - ASTEROID_MIN_RADIUS
            asteroida = Asteroid(self.position.x, self.position.y, nradius)
            asteroidb = Asteroid(self.position.x, self.position.y, nradius)
            asteroida.velocity = va * 1.2
            asteroidb.velocity = vb * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
