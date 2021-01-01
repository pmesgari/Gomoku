from business_rules.board import make_board
from business_rules.gomoku_rules import GomokuRules


class Game:
    def __init__(self):
        self.board = make_board()
        self.rules = GomokuRules()

    @classmethod
    def make_new_game(cls):
        return cls()

    def take_turn(self, column, row):
        return self.board.take_turn(column, row)

    def whose_turn(self):
        return self.board.whose_turn()

    def get_board(self):
        return self.board

    def get_rules(self):
        return self.rules
