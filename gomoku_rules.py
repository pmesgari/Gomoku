from board import Player


class GomokuRules:
    def is_win(self, board, player):
        if self.is_row_win(board, player)\
                or self.is_col_win(board, player):
            return True
        else:
            return False

    def is_row_win(self, board, player):
        return self.is_consecutive(
            board,
            player,
            board.HEIGHT,
            board.WIDTH,
            lambda i, j: board.get(j, i)
        )

    def is_col_win(self, board, player):
        return self.is_consecutive(
            board,
            player,
            board.WIDTH,
            board.HEIGHT,
            lambda i, j: board.get(i, j)
        )

    def is_consecutive(self, board, player, i_max, j_max, get_stone):
        consecutive_stones = 0
        for i in range(0, i_max):
            for j in range(0, j_max):
                player_piece = get_stone(i, j)
                if player_piece == player:
                    consecutive_stones += 1
                    if consecutive_stones > 4:
                        return True
                else:
                    consecutive_stones = 0
        return consecutive_stones > 4