SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
LINE_NUM = 20
COLUMN_NUM = 10
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAME_AREA_HEIGHT = CELL_WIDTH * 20
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT
EDGE_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)
BG_COLOR = (230, 230, 230)

S_SHAPE_TEMPLATE = ['.OO.',
                    'OO..',
                    '....']

Z_SHAPE_TEMPLATE = ['OO..',
                    '.OO.',
                    '....']

I_SHAPE_TEMPLATE = ['.O..',
                    '.O..',
                    '.O..',
                    '.O..']

O_SHAPE_TEMPLATE = ['OO..',
                    'OO..',
                    '....']

J_SHAPE_TEMPLATE = ['..O.',
                    '..O.',
                    '.OO.']

L_SHAPE_TEMPLATE = ['.O..',
                    '.O..',
                    '.OO.']

T_SHAPE_TEMPLATE = ['.O..',
                    'OOO.',
                    '....']

PIECES = {
    'S': S_SHAPE_TEMPLATE,
    'Z': Z_SHAPE_TEMPLATE,
    'J': J_SHAPE_TEMPLATE,
    'L': L_SHAPE_TEMPLATE,
    'O': O_SHAPE_TEMPLATE,
    'T': T_SHAPE_TEMPLATE,
}
