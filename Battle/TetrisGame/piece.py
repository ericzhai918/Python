class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.screen = screen


# PIECES = {
#     'S': S_SHAPE_TEMPLATE,
#     'Z': Z_SHAPE_TEMPLATE,
#     'J': J_SHAPE_TEMPLATE,
#     'L': L_SHAPE_TEMPLATE,
#     'O': O_SHAPE_TEMPLATE,
#     'T': T_SHAPE_TEMPLATE,
# }
#
# S_SHAPE_TEMPLATE = ['.OO.',
#                     'OO..',
#                     '....']