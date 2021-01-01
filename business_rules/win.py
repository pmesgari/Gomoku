from enum import Enum


class Direction(Enum):
    UR = 'upper_right'
    LR = 'lower_right'
    LL = 'lower_left'
    UL = 'upper_left'
    UM = 'upper_middle'
    LM = 'lower_middle'
    MR = 'middle_right'
    ML = 'middle_left'


class BadDirection(Exception):
    pass


def get_direction_vectors():
    return {
        Direction.UR: lambda start: (start[0] + 1, start[1] - 1),
        Direction.LR: lambda start: (start[0] + 1, start[1] + 1),
        Direction.LL: lambda start: (start[0] - 1, start[1] + 1),
        Direction.UL: lambda start: (start[0] - 1, start[1] - 1),
        Direction.UM: lambda start: (start[0], start[1] - 1),
        Direction.LM: lambda start: (start[0], start[1] + 1),
        Direction.MR: lambda start: (start[0] + 1, start[1]),
        Direction.ML: lambda start: (start[0] - 1, start[1])
    }


def get_direction_vector(direction):
    direction_vectors = get_direction_vectors()
    return direction_vectors.get(direction)


def is_valid(x, y, width, height):
    if x <= -1 or y <= -1 or x >= width or y >= height:
        return False
    return True


def explore(grid, start, direction, match=None, result=None):
    """
    Explore the grid from the start point in the given direction.
    If a match is given, stop exploring as soon as the match condition is not
    satisfied anymore. Otherwise explore until an invalid coordinate is reached.
    """
    if result is None:
        result = []
    direction_vector = get_direction_vector(direction)
    if direction_vector:
        x, y = direction_vector(start)
        if not is_valid(x, y, len(grid), len(grid[0])):
            return result
        else:
            if match:
                if grid[x][y] == match:
                    result.append((x, y))
            else:
                result.append((x, y))
            return explore(grid, (x, y), direction, match, result)
    else:
        raise BadDirection


def reverse(direction):
    return {
        Direction.UR: Direction.LL,
        Direction.LR: Direction.UL,
        Direction.LL: Direction.UR,
        Direction.UL: Direction.LR,
        Direction.UM: Direction.LM,
        Direction.LM: Direction.UM,
        Direction.MR: Direction.ML,
        Direction.ML: Direction.MR
    }.get(direction, None)


def is_win(grid, start, match, win_length):
    win_directions = get_win_directions(grid, start, match)
    explored_directions = {}
    for wd in win_directions:
        if reverse(wd) in explored_directions:
            explored_directions[reverse(wd)].extend(explore(grid, start, wd, match))
        else:
            explored_directions[wd] = explore(grid, start, wd, match)
    for key, value in explored_directions.items():
        if len(value) + 1 >= win_length:
            return True
    return False


def get_win_directions(grid, start, match):
    win_directions = []
    if grid[start[0]][start[1]] != match:
        return win_directions

    all_directions = [
        Direction.UR,
        Direction.LR,
        Direction.LL,
        Direction.UL,
        Direction.UM,
        Direction.MR,
        Direction.LM,
        Direction.ML
    ]

    width = len(grid)
    height = len(grid[0])

    for d in all_directions:
        dv = get_direction_vector(d)
        x, y = dv(start)
        if is_valid(x, y, width, height):
            if grid[x][y] == match:
                win_directions.append(d)
    return win_directions
