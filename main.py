import pygame
import sys

from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.checkCollision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(("black"))  # Fill the screen with black
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()  # Update the display

        dt = clock.tick(60) / 1000 # Limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()
