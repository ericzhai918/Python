import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('俄罗斯方块')
    bg_color = (230, 230, 230)

    # 窗口主循环
    while True:
        # 遍历事件队列
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击右上角的'X'，终止主循环
                sys.exit()

        screen.fill(bg_color)
        # 重绘界面
        pygame.display.flip()


if __name__ == "__main__":
    main()
