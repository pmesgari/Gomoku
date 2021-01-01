from business_rules import win


class GomokuRules:
    @staticmethod
    def is_win(board, player):
        grid = board.get_grid()
        for i in range(board.get_width()):
            for j in range(board.get_height()):
                if win.is_win(grid, (i, j), player, 5):
                    return True
        return False
