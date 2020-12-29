from game_presenter import GamePresenter
from board import Player


# read format as representation
def test_format_of_player_status():
    presenter = GamePresenter()
    assert presenter.get_player_status(Player.White) == "White's Turn"
    assert presenter.get_player_status(Player.Black) == "Black's Turn"


def test_format_of_player_win_status():
    presenter = GamePresenter()
    assert presenter.get_win_status(Player.White) == "White Wins!"
