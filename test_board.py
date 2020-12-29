import pytest
from board import Player, BadLocation, SpaceOccupied


def test_new_board_has_no_stones(board):
    stones = board.stones_placed()
    assert stones == 0


def test_can_add_stones_in_bounds(board):
    board.place(1, 1, Player.White)
    assert board.stones_placed() == 1

    placed_stone = board.get(1, 1)
    assert placed_stone == Player.White

    board.place(board.WIDTH - 1, board.HEIGHT - 1, Player.Black)
    assert board.stones_placed() == 2

    placed_stone = board.get(board.WIDTH - 1, board.HEIGHT - 1)
    assert placed_stone == Player.Black


def test_knows_about_empty_intersection(board):
    assert Player.Empty == board.get(0, 1)
    board.place(0, 1, Player.White)
    assert Player.White == board.get(0, 1)


def test_cannot_add_to_occupied_intersection(board):
    board.place(0, 0, Player.White)
    with pytest.raises(SpaceOccupied):
        board.place(0, 0, Player.Black)
    with pytest.raises(SpaceOccupied):
        board.place(0, 0, Player.White)


def test_cannot_place_stone_outside_bounds(board):
    with pytest.raises(BadLocation):
        board.place(-1, -1, Player.White)
    with pytest.raises(BadLocation):
        board.place(board.WIDTH + 1, board.HEIGHT + 1, Player.White)
    with pytest.raises(BadLocation):
        board.place(0, -1, Player.White)
    with pytest.raises(BadLocation):
        board.place(0, board.HEIGHT + 1, Player.White)
    with pytest.raises(BadLocation):
        board.place(-1, 0, Player.White)
    with pytest.raises(BadLocation):
        board.place(board.WIDTH + 1, 0, Player.White)
    assert board.stones_placed() == 0