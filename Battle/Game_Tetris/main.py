from settings import *
import pygame
import sys
from Piece import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")

    bg_color = BG_COLOR
    piece = Piece('S', screen)

    while True:
        check_events(piece)

        screen.fill(bg_color)
        draw_game_area(screen)
        piece.paint()

        pygame.display.flip()


def check_events(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                piece.move_down()
            elif event.key == pygame.K_UP:
                piece.turn()
            elif event.key == pygame.K_LEFT:
                piece.move_left()
            elif event.key == pygame.K_RIGHT:
                piece.move_right()


def draw_game_area(screen):
    # 行，20行，纵坐标衡量增大
    for n in range(0, 21):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAMW_AREA_TOP + CELL_WIDTH * n),
                         (GAME_AREA_LR + GAME_AREA_WIDTH, GAMW_AREA_TOP + CELL_WIDTH * n))

    # 列，10列，横坐标衡量增大
    for n in range(0, 11):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR + CELL_WIDTH * n, GAMW_AREA_TOP),
                         (GAME_AREA_LR + CELL_WIDTH * n, SCREEN_HEIGHT))


if __name__ == '__main__':
    main()
