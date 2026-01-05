import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Player.containers = updatable, drawable
    Shot.containers = shots, updatable, drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(obj):
                    log_event("asteroid_shot")
                    obj.split()
                    shot.kill()

        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
