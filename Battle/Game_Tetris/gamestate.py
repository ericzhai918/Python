import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame


class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.next_piece = None
        self.timer_interval = TIMER_INTERVAL
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.session_count = 0

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_score(self, score):
        self.game_score += score

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        # self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        self.piece = self.new_piece()
        self.piece = self.new_piece()
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False

    def pause_game(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                self.stopped = True
                break
        if not self.stopped:
            # self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
            self.piece = self.new_piece()
            if self.piece.hit_wall():
                self.stopped = True
        if self.stopped:
            self.stop_timer()

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)

    def new_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)

        return self.piece

