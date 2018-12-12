try:
    from settings import *
except:
    from .settings import *

class GameWall():
    '''游戏区墙体类。记住落到底部的方块组成的“墙”。'''
    def __init__(self, screen):
        '''游戏开始时，游戏区20*10个格子被'-'符号填充。“墙”是空的。'''
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    def print(self):
        '''打印20*10的二维矩阵self.area的元素值。用于调试。'''
        print(len(self.area), 'rows', len(self.area[0]), 'columns')
        for line in self.area:
            print(line)

    def add_to_wall(self, piece):
        '''把方块piece砌到墙体内'''
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell((piece.x + c, piece.y + r), piece.shape)

    def set_cell(self, position, shape_label):
        '''把第r行c列的格子打上方块记号（如S, L, ...），因为该格子被此方块占据。'''
        c, r = position
        self.area[r][c] = shape_label
