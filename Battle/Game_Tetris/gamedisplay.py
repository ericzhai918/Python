from settings import *
import pygame


class GameDisplay():
    @staticmethod
    def draw_game_area(screen, game_state, game_resource):
        '''绘制游戏区域'''
        GameDisplay.draw_grid(screen)
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)
        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_game_over(screen, game_resource)
            GameDisplay.draw_start_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen, game_resource)
        GameDisplay.draw_next_piece(screen, game_state.next_piece)

    @staticmethod
    def draw_grid(screen):
        # 行，20行，纵坐标衡量增大
        for row in range(0, 21):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR, GAME_AREA_TOP + CELL_WIDTH * row),
                             (GAME_AREA_LR + GAME_AREA_WIDTH, GAME_AREA_TOP + CELL_WIDTH * row))
        # 列，10列，横坐标衡量增大
        for column in range(0, 11):
            pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LR + CELL_WIDTH * column, GAME_AREA_TOP),
                             (GAME_AREA_LR + CELL_WIDTH * column, SCREEN_HEIGHT))

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
        cell_position = (column * CELL_WIDTH + GAME_AREA_LR + 1, row * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_score(screen, score):
        '''绘制游戏得分'''
        score_label_font = pygame.font.SysFont('simhei', 28)
        score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LR + GAME_AREA_WIDTH + 40, GAME_AREA_TOP)
        screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(score), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width, score_label_position[1])
        screen.blit(score_surface, score_position)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        start_tip_position = (GAME_AREA_LR + 2 * CELL_WIDTH, GAME_AREA_TOP + 10 * CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)

    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        pause_position = (GAME_AREA_LR + 1 * CELL_WIDTH, GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(game_resource.load_pausing_img(), pause_position)

        resume_tip_position = (GAME_AREA_LR + 1 * CELL_WIDTH, GAME_AREA_TOP + 11 * CELL_WIDTH)
        screen.blit(game_resource.load_continue_img(), resume_tip_position)

    @staticmethod
    def draw_game_over(screen, game_resource):
        gameover_position = (GAME_AREA_LR + 4 * CELL_WIDTH - CELL_WIDTH // 2, GAME_AREA_TOP + 8 * CELL_WIDTH)
        screen.blit(game_resource.load_gameover_img(), gameover_position)

    @staticmethod
    def draw_next_piece(screen, next_piece):
        start_x = GAME_AREA_LR + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH * 2
        start_y = GAME_AREA_TOP
        GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

        if next_piece:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            # cells变量存储姿态矩阵中有砖块的单元格
            cells = []
            # 扫描姿态矩阵，得出有砖块的单元格
            shape_turn = PIECES[next_piece.shape][next_piece.turn_times]
            for row in range(len(shape_turn)):
                for column in range(len(shape_turn[0])):
                    if shape_turn[row][column] == 'O':
                        cells.append((column, row, PIECE_COLORS[next_piece.shape]))

            # 绘制方块
            for cell in cells:
                color = cell[2]
                left_top = (start_x + cell[0] * CELL_WIDTH, start_y + cell[1] * CELL_WIDTH)
                GameDisplay.draw_cell_rect(screen, left_top, color)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        top_border = pygame.Rect(start_x, start_y, 2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, top_border)

        left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, 2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, left_border)

        right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
                                   2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, right_border)

        bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
                                    2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, bottom_border)

    @staticmethod
    def draw_cell_rect(screen, left_top_anchor, color):
        left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(left_top_anchor, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)
