import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        dt = clock.tick(60) / 1000
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
