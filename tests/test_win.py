import pytest
from business_rules.win import Direction, explore, is_win, get_win_directions


def test_can_explore_directions_without_match():
    grid = [
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24],
        [5, 10, 15, 20, 25]
    ]

    # check all the coreners
    assert explore(grid, (0, 0), Direction.UR) == []
    assert explore(grid, (0, 4), Direction.UR) == [
        (1, 3),
        (2, 2),
        (3, 1),
        (4, 0)
    ]  # [17, 13, 9, 5]
    assert explore(grid, (4, 4), Direction.UR) == []
    assert explore(grid, (4, 0), Direction.UR) == []

    # check edges
    assert explore(grid, (2, 0), Direction.UR) == []
    assert explore(grid, (4, 2), Direction.UR) == []
    assert explore(grid, (2, 4), Direction.UR) == [
        (3, 3),
        (4, 2)
    ]  # [19, 15]
    assert explore(grid, (0, 2), Direction.UR) == [
        (1, 1),
        (2, 0)
    ]  # [7, 3]

    # check inner points
    assert explore(grid, (1, 2), Direction.UR) == [
        (2, 1),
        (3, 0)
    ]  # [8, 4]
    assert explore(grid, (1, 3), Direction.UR) == [
        (2, 2),
        (3, 1),
        (4, 0)
    ]  # [13, 9, 5]


def test_can_explore_directions_with_match():
    grid = [
        [1, 6, 11, 'b', 'b'],
        [2, 'b', 12, 'b', 22],
        [3, 8, 'b', 18, 23],
        [4, 'b', 14, 19, 24],
        ['b', 10, 15, 20, 25]
    ]

    assert explore(grid, (4, 0), Direction.LL, 'b') == [
        (3, 1),
        (2, 2),
        (1, 3),
        (0, 4)
    ]

    assert explore(grid, (2, 2), Direction.UL, 'b') == [(1, 1)]


def test_five_in_a_row_is_a_win():
    """
        - - - - - -
        - - - - - -
        b b b b b -
        - b - - - -
        b - - - - -
        - - - - - -
    """
    grid = [
        ['e', 'e', 'b', 'e', 'b', 'e'],
        ['e', 'e', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e']
    ]

    assert is_win(grid, (0, 2), 'b', 5)
    assert is_win(grid, (2, 2), 'b', 5)


def test_six_in_a_row_is_a_win():
    """
        - - - - - -
        - - - - - -
        b b b b b b
        - b - - - -
        b - - - - -
        - - - - - -
    """
    grid = [
        ['e', 'e', 'b', 'e', 'b', 'e'],
        ['e', 'e', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e']
    ]

    assert is_win(grid, (0, 2), 'b', 5)
    assert is_win(grid, (2, 2), 'b', 5)
    assert is_win(grid, (5, 2), 'b', 5)


def test_four_in_a_row_is_a_lose():
    """
        - - - - - -
        - - - - - -
        - b b b b -
        - b - - - -
        b - - - - -
        - - - - - -
    """
    grid = [
        ['e', 'e', 'e', 'e', 'b', 'e'],
        ['e', 'e', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e']
    ]

    assert is_win(grid, (1, 2), 'b', 5) is False
    assert is_win(grid, (4, 2), 'b', 5) is False
    assert is_win(grid, (3, 2), 'b', 5) is False


def test_five_in_a_column_is_a_win():
    """
        - b - - - -
        - b - - - -
        b b b - b -
        - b - - - -
        b b - - - -
        - - - - - -
    """
    grid = [
        ['e', 'e', 'b', 'e', 'b', 'e'],
        ['b', 'b', 'b', 'b', 'b', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e']
    ]

    assert is_win(grid, (1, 0), 'b', 5)
    assert is_win(grid, (1, 4), 'b', 5)
    assert is_win(grid, (1, 2), 'b', 5)


def test_six_in_a_column_is_a_win():
    """
        - b - - - -
        - b - - - -
        b b b - b -
        - b - - - -
        b b - - - -
        - b - - - -
    """
    grid = [
        ['e', 'e', 'b', 'e', 'b', 'e'],
        ['b', 'b', 'b', 'b', 'b', 'b'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e']
    ]

    assert is_win(grid, (1, 0), 'b', 5)
    assert is_win(grid, (1, 2), 'b', 5)
    assert is_win(grid, (1, 5), 'b', 5)


def test_four_in_a_column_is_a_lose():
    """
        - - - - - -
        - - b - - -
        - b b b - -
        - b b - - -
        b - b - - -
        - - - - - -
    """
    grid = [
        ['e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'b', 'e', 'e'],
        ['e', 'b', 'b', 'e', 'e', 'e'],
        ['e', 'b', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'b', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e']
    ]

    assert is_win(grid, (2, 1), 'b', 5) is False
    assert is_win(grid, (2, 4), 'b', 5) is False
    assert is_win(grid, (2, 2), 'b', 5) is False


def test_five_in_a_diagonal_is_a_win():
    """
        - - - - b
        - - - b -
        - - b - -
        - b - - -
        b - - - -
    """
    grid = [
        [1, 6, 11, 16, 'b'],
        [2, 7, 12, 'b', 22],
        [3, 8, 'b', 18, 23],
        [4, 'b', 14, 19, 24],
        ['b', 10, 15, 20, 25]
    ]

    # starting at the corners
    assert is_win(grid, (0, 4), 'b', 5)
    assert is_win(grid, (4, 0), 'b', 5)

    # starting at the inner point
    assert is_win(grid, (2, 2), 'b', 5)


def test_four_in_a_diagonal_is_a_lose():
    """
        - - - b -
        - b b b -
        - b b - -
        b b - - -
        b - - - -
    """
    grid = [
        [1, 6, 11, 'b', 'b'],
        [2, 'b', 'b', 'b', 22],
        [3, 'b', 'b', 18, 23],
        ['b', 'b', 14, 19, 24],
        [5, 10, 15, 20, 25]
    ]

    assert is_win(grid, (0, 3), 'b', 5) is False
    assert is_win(grid, (1, 3), 'b', 5) is False


def test_six_in_a_diagonal_is_a_win():
    """
        - - - b b b
        - b b b b w
        - b w b - -
        b b b - - b
        b b - - - w
        b - w w - w
    """
    grid = [
        [1, 6, 11, 'b', 'b', 'b'],
        [2, 'b', 'b', 'b', 'b', 'e'],
        [3, 'b', 'w', 'b', 23, 'w'],
        ['b', 'b', 'b', 19, 24, 'w'],
        ['b', 'b', 15, 20, 25, 'e'],
        ['b', 'w', 'e', 'b', 'w', 'w']
    ]

    assert is_win(grid, (0, 5), 'b', 5)
    assert is_win(grid, (2, 3), 'b', 5)
    assert is_win(grid, (5, 0), 'b', 5)


def test_can_detect_win_directions():
    grid = [
        [1, 6, 11, 'b', 'b'],
        [2, 'b', 12, 'b', 22],
        [3, 8, 'b', 18, 23],
        [4, 'b', 14, 19, 24],
        ['b', 10, 15, 20, 25]
    ]

    assert set(get_win_directions(grid, (2, 2), 'b')) == {
        Direction.UR, Direction.UL, Direction.LL
    }
    assert set(get_win_directions(grid, (3, 1), 'b')) == {
        Direction.UR, Direction.LL
    }
    assert set(get_win_directions(grid, (4, 0), 'b')) == {
        Direction.LL
    }
    assert set(get_win_directions(grid, (2, 0), 'b')) == set()
