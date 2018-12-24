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
        draw_game_area(screen)
        draw_cell(screen, GAME_AREA_LR, GAMW_AREA_TOP)

        pygame.display.flip()


def draw_game_area(screen):
    # 左
    # pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAMW_AREA_TOP), (GAME_AREA_LR, SCREEN_HEIGHT))
    # 上
    # pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAMW_AREA_TOP), (GAME_AREA_LR + GAME_AREA_WIDTH, GAMW_AREA_TOP))
    # 右
    # pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR + GAME_AREA_WIDTH, GAMW_AREA_TOP),
    #                  (GAME_AREA_LR + GAME_AREA_WIDTH, SCREEN_HEIGHT))
    # 下
    # pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, SCREEN_HEIGHT), (GAME_AREA_LR + GAME_AREA_WIDTH, SCREEN_HEIGHT))

    # 行，20行，纵坐标衡量增大
    for n in range(0, 21):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAMW_AREA_TOP + CELL_WIDTH * n),
                         (GAME_AREA_LR + GAME_AREA_WIDTH, GAMW_AREA_TOP + CELL_WIDTH * n))

    # 列，10列，横坐标衡量增大
    for n in range(0, 11):
        pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR + CELL_WIDTH * n, GAMW_AREA_TOP),
                         (GAME_AREA_LR + CELL_WIDTH * n, SCREEN_HEIGHT))


def draw_cell(screen, left, top):
    cell_left_top = (left, top)
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cell_rect = pygame.Rect(cell_left_top, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)


if __name__ == '__main__':
    main()
