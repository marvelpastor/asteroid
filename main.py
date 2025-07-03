import pygame
import sys
from constants import *
from player import *
from circleshape import CircleShape
from asteroid import *
from asteroidfield import AsteroidField
from shots import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroidfield = AsteroidField()
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player.timer <= 0:
            player.shoot(shots)
        screen.fill((0,0,0))
        for thing in drawable:    
            thing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisionCheck(asteroid) == True:
                    shot.kill()
                    asteroid.split()
            if asteroid.collisionCheck(player) == True:
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
