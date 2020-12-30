import pytest
from business_rules.gomoku_rules import GomokuRules
from business_rules.board import make_board


@pytest.fixture
def board():
    board = make_board()
    return board


@pytest.fixture
def rules():
    gomoku_rules = GomokuRules()
    return gomoku_rules
