from enum import Enum
from abc import ABCMeta, abstractmethod


class SpaceOccupied(Exception):
    pass


class BadLocation(Exception):
    pass


class Player(Enum):
    White = 'white'
    Black = 'black'
    Empty = 'empty'


class BaseBoard(metaclass=ABCMeta):
    @abstractmethod
    def take_turn(self, column, row):
        pass

    @abstractmethod
    def place(self, column, row, player):
        pass

    @abstractmethod
    def get(self, column, row):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def whose_turn(self):
        pass


def make_board():
    return Board()


class Board(BaseBoard):
    def __init__(self):
        self.WIDTH = 19
        self.HEIGHT = 19
        self.placed_stones = {}
        self.grid = self.init_grid()
        self.player = Player.White

    def init_grid(self):
        grid = []
        for column in range(0, self.WIDTH):
            grid.append([])
            for row in range(0, self.HEIGHT):
                grid[column].append(Player.Empty)
        return grid

    def stones_placed(self):
        return len(self.placed_stones)

    def get_width(self):
        return self.WIDTH

    def get_height(self):
        return self.HEIGHT

    def get_grid(self):
        return self.grid

    def place(self, column, row, player):
        self._place(column, row, player)
        if self.get(column, row) != Player.Empty:
            raise SpaceOccupied
        self.grid[column][row] = player

    def get(self, column, row):
        return self.grid[column][row]

    def _place(self, column, row, player):
        loc = self.make_location(column, row)
        if self.get(column, row) != Player.Empty:
            raise SpaceOccupied
        self.placed_stones[loc] = player

    def make_location(self, column, row):
        if row < 0 or row >= self.HEIGHT or column < 0 or column >= self.WIDTH:
            raise BadLocation
        return column * self.WIDTH + row

    def _get(self, column, row):
        loc = self.make_location(column, row)
        stone = self.placed_stones.get(loc, None)
        if stone:
            return stone
        else:
            return Player.Empty

    def take_turn(self, column, row):
        self.place(column, row, self.whose_turn())
        self.player = self.other(self.player)

    @staticmethod
    def other(player):
        return Player.Black if player == Player.White else Player.White

    def whose_turn(self):
        return self.player
