from settings import *
import pygame
import sys
from piece import *
import random
import time
from gamewall import *
from gamestate import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10, 100)

    bg_color = BG_COLOR
    random.seed(int(time.time()))
    game_wall = GameWall(screen)
    piece = Piece(random.choice(PIECE_TYPES), screen, game_wall)
    game_state = GameState(screen)

    while True:
        if game_state.piece.is_on_bottom:
            game_state.wall.add_to_wall(game_state.piece)
            game_state.piece = Piece(random.choice(PIECE_TYPES), screen, game_state.wall)

        check_events(game_state.piece)

        screen.fill(bg_color)
        GameDisplay.draw_game_area(screen, game_state.wall)
        game_state.piece.paint()

        pygame.display.flip()


def check_events(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, piece)
        elif event.type == pygame.USEREVENT:
            piece.move_down()


def on_key_down(event, piece):
    if event.key == pygame.K_DOWN:
        piece.move_down()
    elif event.key == pygame.K_UP:
        piece.turn()
    elif event.key == pygame.K_LEFT:
        piece.move_left()
    elif event.key == pygame.K_RIGHT:
        piece.move_right()
    elif event.key == pygame.K_f:
        piece.fall_down()


if __name__ == '__main__':
    main()
