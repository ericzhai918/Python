import pygame
import sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

CELL_WIDTH = 40
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAMW_AREA_HEIGHT = CELL_WIDTH * 20

GAME_AREA_LR = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAMW_AREA_TOP = SCREEN_HEIGHT - GAMW_AREA_HEIGHT

BG_COLOR = (230, 230, 230)
EDGE_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")

    bg_color = BG_COLOR

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()


if __name__ == '__main__':
    main()
