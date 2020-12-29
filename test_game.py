from board import Board, Player
from gomoku_rules import GomokuRules
from game import Game


def test_white_starts_new_game():
    board = Board()
    rules = GomokuRules()
    game = Game(board, rules)
    assert Player.White == game.whose_turn()


def test_after_a_turn_is_other_players_turn():
    board = Board()
    rules = GomokuRules()
    game = Game(board, rules)

    game.take_turn(0, 0)
    assert Player.White == board.get(0, 0)
    assert Player.Black == game.whose_turn()

    game.take_turn(1, 0)
    assert Player.Black == board.get(1, 0)
    assert Player.White == game.whose_turn()