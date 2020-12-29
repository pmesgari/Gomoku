from enum import Enum
from abc import ABCMeta


class SpaceOccupied(Exception):
    pass


class BadLocation(Exception):
    pass


class Player(Enum):
    White = 'white'
    Black = 'black'
    Empty = 'empty'


# class Board(metaclass=ABCMeta):
#     def place(self, column, row, player):
#         pass
#
#     def get(self, column, row):
#         pass


class Board:
    def __init__(self):
        self.WIDTH = 19
        self.HEIGHT = 19
        self.placed_stones = {}

    def stones_placed(self):
        return len(self.placed_stones)

    def place(self, column, row, player):
        loc = self.make_location(column, row)
        if self.placed_stones.get(loc, None):
            raise SpaceOccupied
        self.placed_stones[loc] = player

    def make_location(self, column, row):
        if row < 0 or row >= self.HEIGHT or column < 0 or column >= self.WIDTH:
            raise BadLocation
        return column * self.WIDTH + row

    def get(self, column, row):
        loc = self.make_location(column, row)
        stone = self.placed_stones.get(loc, None)
        if stone:
            return stone
        else:
            return Player.Empty

