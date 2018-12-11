import pygame

try:
    from settings import *
except:
    from .settings import *


class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.turn_times = 0
        self.screen = screen

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn_times]
        # r是行，c是列，x加的是行r，y加的是列c
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1, y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

    def move_right(self):
        if self.can_move_right():
            self.x += 1

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_down():
            self.y += 1

    def turn(self):
        shape_list_len = len(PIECES[self.shape])
        if self.can_turn():
            self.turn_times = (self.turn_times + 1) % shape_list_len

    def can_move_right(self):
        shape_mtx = PIECES[self.shape][0]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    # 如果方块在最右侧，该方法返回False，否则返回True
                    if self.x + c >= COLUMN_NUM - 1:
                        return False
        return True

    def can_move_left(self):
        shape_mtx = PIECES[self.shape][0]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.x + c <= 0:
                        return False
        return True

    def can_move_down(self):
        shape_mtx = PIECES[self.shape][0]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.y + r >= LINE_NUM - 1:
                        return False
        return True

    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c < 0 or self.x + c >= COLUMN_NUM) or (self.y + r < 0 or self.y + r >= LINE_NUM):
                        return False
        return True
