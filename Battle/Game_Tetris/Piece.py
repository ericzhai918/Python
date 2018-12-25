from settings import *
import pygame


class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.screen = screen

    def paint(self):
        shape_template = PIECES[self.shape]

        for row in range(len(shape_template)):
            for column in range(len(shape_template[0])):
                if shape_template[row][column] == 'O':
                    self.draw_cell(self.x + column, self.y + row)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LR + 1, y * CELL_WIDTH + GAMW_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_down(self):
        self.y += 1
