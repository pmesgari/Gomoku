from board import Player


class Game:
    def __init__(self, board, rules):
        self.board = board
        self.rules = rules
        self.player = Player.White

    def whose_turn(self):
        return self.player

    @staticmethod
    def other(player):
        return Player.Black if player == Player.White else Player.White

    def take_turn(self, column, row):
        self.board.place(column, row, self.whose_turn())
        self.player = self.other(self.player)

    def get_board(self):
        return self.board

    def get_rules(self):
        return self.rules