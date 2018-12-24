import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("俄罗斯方块")

    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    main()
