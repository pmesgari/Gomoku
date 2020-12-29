import pytest
from gomoku_rules import GomokuRules
from board import Board


# @pytest.fixture
# def board_data():
#     board_data = BoardData()
#     return board_data


@pytest.fixture
def board():
    board = Board()
    return board


@pytest.fixture
def rules():
    gomoku_rules = GomokuRules()
    return gomoku_rules
