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
