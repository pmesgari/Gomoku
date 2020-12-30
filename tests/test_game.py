from business_rules.board import Player
from business_rules.game import Game


def test_white_starts_new_game():
    game = Game()
    assert Player.White == game.whose_turn()


def test_after_a_turn_is_other_players_turn():
    game = Game()

    game.take_turn(0, 0)
    assert Player.White == game.get_board().get(0, 0)
    assert Player.Black == game.whose_turn()

    game.take_turn(1, 0)
    assert Player.Black == game.get_board().get(1, 0)
    assert Player.White == game.whose_turn()