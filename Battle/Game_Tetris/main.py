from settings import *
import pygame
import sys
from piece import *
import random
import time
from gamewall import *
from gamestate import *
from gameresource import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10, 100)

    bg_color = BG_COLOR
    random.seed(int(time.time()))
    game_state = GameState(screen)
    game_resource = GameResource()

    while True:
        if game_state.piece and game_state.piece.is_on_bottom:
            game_state.wall.add_to_wall(game_state.piece)
            game_state.add_score(game_state.wall.eliminate_lines())
            game_state.piece = Piece(random.choice(PIECE_TYPES), screen, game_state.wall)

        check_events(game_state)

        screen.fill(bg_color)
        GameDisplay.draw_game_area(screen, game_state, game_resource)
        if game_state.piece:
            game_state.piece.paint()

        pygame.display.flip()


def check_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()


def on_key_down(event, game_state):
    if not game_state.paused and event.key == pygame.K_DOWN:
        if game_state.piece:
            game_state.piece.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        if game_state.piece:
            game_state.piece.turn()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        if game_state.piece:
            game_state.piece.move_left()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        if game_state.piece:
            game_state.piece.move_right()
    elif not game_state.paused and event.key == pygame.K_f:
        if game_state.piece:
            game_state.piece.fall_down()
    elif not game_state.paused and event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()


if __name__ == '__main__':
    main()
