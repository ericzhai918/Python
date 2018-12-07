import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAME_AREA_HEIGHT = CELL_WIDTH * 20
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT
EDGE_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)
BG_COLOR = (230, 230, 230)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('俄罗斯方块')
    bg_color = BG_COLOR

    # 窗口主循环
    while True:
        # 遍历事件队列
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击右上角的'X'，终止主循环
                sys.exit()

        screen.fill(bg_color)
        draw_game_area(screen)
        draw_cell(screen, GAME_AREA_LEFT, GAME_AREA_TOP)
        # 重绘界面
        pygame.display.flip()


def draw_game_area(screen):
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (200, 200))
    pass


def draw_cell(screen, left, top):
    cell_left_top = (left, top)
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cell_rect = pygame.Rect(cell_left_top, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)
    pass


if __name__ == "__main__":
    main()
