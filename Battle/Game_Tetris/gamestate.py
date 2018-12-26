import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame


class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = Piece(random.choice(PIECE_TYPES), screen, self.wall)
        self.timer_interval = TIMER_INTERVAL
        self.set_timer(self.timer_interval)
        self.game_score = 0

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_score(self, score):
        self.game_score += score
