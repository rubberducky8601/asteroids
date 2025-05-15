import pygame
from pygame.sprite import Group

from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)

        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()
