from settings import *
import pygame
from gamedisplay import *


class Piece():
    def __init__(self, shape, screen, gamewall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.screen = screen
        self.turn_times = 0
        self.is_on_bottom = False
        self.game_wall = gamewall

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]

        for row in range(len(shape_turn)):
            for column in range(len(shape_turn[0])):
                if shape_turn[row][column] == 'O':
                    self.draw_cell(self.y + row, self.x + column)

    def draw_cell(self, row, column):
        GameDisplay.draw_cell(self.screen, row, column, PIECE_COLORS[self.shape])

    def move_right(self):
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_bottom = True

    def can_move_right(self):
        shape_template = PIECES[self.shape][self.turn_times]

        for row in range(len(shape_template)):
            for column in range(len(shape_template[0])):
                if shape_template[row][column] == 'O':
                    # 方块到最右侧墙体时或者紧挨着方块的右侧有墙体时，返回False
                    if self.x + column >= COLUMN_NUM - 1 or self.game_wall.is_wall(self.y + row, self.x + column + 1):
                        return False
        return True

    def can_move_left(self):
        shape_template = PIECES[self.shape][self.turn_times]

        for row in range(len(shape_template)):
            for column in range(len(shape_template[0])):
                if shape_template[row][column] == 'O':
                    #方块到最左侧墙体时或者紧挨着方块的左侧有墙体时，返回False
                    if self.x + column <= 0 or self.game_wall.is_wall(self.y + row, self.x + column - 1):
                        return False
        return True

    def can_move_down(self):
        shape_template = PIECES[self.shape][self.turn_times]

        for row in range(len(shape_template)):
            for column in range(len(shape_template[0])):
                if shape_template[row][column] == 'O':
                    # 方块在底部时或者紧挨着方块的下方单元格有被墙体占据时，返回False
                    if self.y + row >= LINE_NUM - 1 or self.game_wall.is_wall(self.y + row + 1, self.x + column):
                        return False
        return True

    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
            self.turn_times = (self.turn_times + 1) % shape_list_len

    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for row in range(len(shape_mtx)):
            for column in range(len(shape_mtx[0])):
                if shape_mtx[row][column] == 'O':
                    if (self.x + column < 0 or self.x + column >= COLUMN_NUM - 1) or (self.y + row < 0 or self.y + row >= LINE_NUM - 1)\
                            or (self.game_wall.is_wall(self.y + row, self.x + column)):
                        return False
        return True

    def fall_down(self):
        while not self.is_on_bottom:
            self.move_down()

    def hit_wall(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for row in range(len(shape_mtx)):
            for column in range(len(shape_mtx[0])):
                if shape_mtx[row][column] == 'O':
                    if self.game_wall.is_wall(self.y+row,self.x+column):
                        return True
        return False