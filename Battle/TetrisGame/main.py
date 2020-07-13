import pygame
import sys

from piece import Piece
from gamewall import *
from gamedisplay import *
import random
import time

def main():
    # 初始化pygame
    pygame.init()
    # 创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 设置窗口标题
    pygame.display.set_caption('俄罗斯方块')
    # 一直按下某个键，每过100毫秒就引发一个KEYDOWN事件
    pygame.key.set_repeat(10, 100)
    # 屏幕背景色
    bg_color = BG_COLOR

    random.seed(int(time.time()))#产生不同的随机序列
    game_wall = GameWall(screen)
    piece = Piece(random.choice(PIECE_TYPES), screen, game_wall)
    # 窗口主循环
    while True:
        if piece.at_bottom:
            game_wall.add_to_wall(piece)
            piece = Piece(random.choice(PIECE_TYPES), screen,game_wall)
        # 遍历事件队列
        check_events(piece)
        screen.fill(bg_color)
        # 绘制游戏区域网格线和墙体
        GameDisplay.draw_game_area(screen, game_wall)
        # 绘制方块
        piece.paint()
        # 重绘界面
        pygame.display.flip()

def check_events(piece):
    '''捕捉和处理键盘按键事件'''
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
            elif event.key == pygame.K_f:
                piece.fall_down()


if __name__ == "__main__":
    main()
