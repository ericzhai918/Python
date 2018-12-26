from settings import *


class GameWall():
    def __init__(self, screen):
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    # def print(self):
    #     print(len(self.area),"rows",len(self.area[0]),"columns")
    #     for line in self.area:
    #         print(line)

    def add_to_wall(self, piece):
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for row in range(len(shape_turn)):
            for column in range(len(shape_turn[0])):
                if shape_turn[row][column] == 'O':
                    self.set_cell((piece.x + column, piece.y + row), piece.shape)
#?
    def set_cell(self, position, shape_label):
        column, row = position
        self.area[row][column] = shape_label
