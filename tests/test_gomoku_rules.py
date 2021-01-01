from business_rules.board import Player, make_board


def test_empty_board_is_not_win(rules, board):
    assert rules.is_win(board, Player.White) is False


def test_not_empty_board_but_not_win_is_not_a_win(rules, board):
    board.place(1, 1, Player.White)
    assert rules.is_win(board, Player.White) is False


def test_five_in_a_row_in_the_first_row_is_a_win(rules, board):
    for col in range(0, 5):
        board.place(col, 0, Player.White)
    assert rules.is_win(board, Player.White)


def test_five_consecutive_stones_for_other_player_is_a_lose(rules, board):
    for col in range(0, 5):
        board.place(col, 0, Player.Black)
    assert rules.is_win(board, Player.White) is False


def test_six_in_a_row_in_the_first_row_is_a_win(rules, board):
    for col in range(0, 6):
        board.place(col, 0, Player.White)
    assert rules.is_win(board, Player.White)


def test_four_in_a_row_in_the_first_row_is_a_lose(rules, board):
    for col in range(0, 4):
        board.place(col, 0, Player.White)
    assert rules.is_win(board, Player.White) is False


def test_five_consecutive_in_any_row_is_a_win(rules, board):
    for row in range(0, board.HEIGHT):
        board = make_board()
        for col in range(0, 5):
            board.place(col, row, Player.White)
        assert rules.is_win(board, Player.White)


def test_five_non_consecutive_stones_in_row_is_a_lose(rules, board):
    board.place(1, 0, Player.White)
    board.place(3, 0, Player.White)
    board.place(5, 0, Player.White)
    board.place(7, 0, Player.White)
    board.place(9, 0, Player.White)

    assert rules.is_win(board, Player.White) is False


def test_five_consecutive_stones_in_a_column_is_a_win(rules, board):
    for row in range(0, 5):
        board.place(0, row, Player.White)
    assert rules.is_win(board, Player.White)
