import pygame
from asteroidfield import AsteroidField
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_unit = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:  # Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        FPS = clock.tick(60)
        dt = FPS / 1000

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
