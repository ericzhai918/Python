import pygame
from pygame.locals import *
import sys
try:
    from settings import *
    from piece import Piece
except:
    from .settings import *
    from .piece import Piece

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('俄罗斯方块')
    bg_color = BG_COLOR
    piece = Piece('S',screen)

    # 窗口主循环
    while True:
        # 遍历事件队列
        check_events(piece)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击右上角的'X'，终止主循环
                sys.exit()

        screen.fill(bg_color)
        draw_game_area(screen)
        draw_cell(screen, GAME_AREA_LEFT, GAME_AREA_TOP)
        piece.paint()
        # 重绘界面
        pygame.display.flip()


def draw_game_area(screen):
    # 左上到左下(竖线)，向右x+40
    for x in range(11):
        x = x * 40
        pygame.draw.line(screen, (0, 0, 0),(GAME_AREA_LEFT + x, GAME_AREA_TOP), (GAME_AREA_LEFT + x, SCREEN_HEIGHT))

    ##左上到右上(横线)，y+40
    for y in range(21):
        y = y * 40
        pygame.draw.line(screen, (0, 0, 0),(GAME_AREA_LEFT, GAME_AREA_TOP + y),(GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + y))

def draw_cell(screen, left, top):
    cell_left_top = (left, top)
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cell_rect = pygame.Rect(cell_left_top, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)


def check_events(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                piece.move_down()
            elif event.key == pygame.K_UP:
                piece.move_up()
            elif event.key == pygame.K_LEFT:
                piece.move_left()
            elif event.key == pygame.K_RIGHT:
                piece.move_right()

if __name__ == "__main__":
     main()

