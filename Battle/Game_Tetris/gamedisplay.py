from settings import *
import pygame


class GameDisplay():
    @staticmethod
    def draw_game_area(screen, game_wall):
        '''绘制游戏区域'''
        # 行，20行，纵坐标衡量增大
        for row in range(0, 21):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAMW_AREA_TOP + CELL_WIDTH * row),
                             (GAME_AREA_LR + GAME_AREA_WIDTH, GAMW_AREA_TOP + CELL_WIDTH * row))

        # 列，10列，横坐标衡量增大
        for column in range(0, 11):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR + CELL_WIDTH * column, GAMW_AREA_TOP),
                             (GAME_AREA_LR + CELL_WIDTH * column, SCREEN_HEIGHT))

        GameDisplay.draw_wall(game_wall)

    @staticmethod
    def draw_wall(game_wall):
        '''绘制墙体'''
        for row in range(LINE_NUM):
            for column in range(COLUMN_NUM):
                if game_wall.area[row][column] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, row, column, PIECE_COLORS[game_wall.area[row][column]])

    @staticmethod
    def draw_cell(screen, row, column, color):
        '''第row行column列的格子里填充color颜色。一种方块对应一种颜色。'''
        cell_position = (column * CELL_WIDTH + GAME_AREA_LR + 1, row * CELL_WIDTH + GAMW_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

'''
知识点：类定义内部，方法名之前的 @staticmethod 表明这一方法是一个静态方法。
所谓静态方法，是指没有访问对象的属性的方法。静态方法本质上跟函数类似。
只不过调用的写法是“类名.方法()”，比如 GameDisplay.draw_cell()，或 GameDisplay.draw_wall()
'''
