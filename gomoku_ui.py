from tkinter import *
from board import Board, Player
from gomoku_rules import GomokuRules
from game import Game
from game_presenter import GamePresenter


class ViewController:
    def __init__(self):
        self.root = Tk()
        self.WIDTH = 400
        self.HEIGHT = 600

        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.root.resizable(height=0, width=0)

        self.frame = Frame(self.root, bg='blue')
        self.frame.pack(expand=True, fill=BOTH)

        self.board = Board()
        self.rules = GomokuRules()
        self.game = Game(self.board, self.rules)
        self.presenter = GamePresenter()

        self.board.place(0, 0, Player.White)
        self.board.place(18, 0, Player.White)
        self.board.place(10, 10, Player.White)
        self.board.place(11, 11, Player.Black)
        self.board.place(0, 11, Player.Black)

        self.status_label = StatusLabel(
            self.frame,
            text=self.presenter.get_player_status(self.game.whose_turn())
        )
        self.grid_view = GridView(
            self.frame,
            width=self.WIDTH,
            height=self.HEIGHT,
            game=self.game
        )
        self.grid_view.set_click_responder(lambda col, row: self.respond_to_click(col, row))

    def respond_to_click(self, column, row):
        self.game.take_turn(column, row)
        if self.game.get_rules().is_win(self.board, self.game.whose_turn()):
            self.status_label.set_text(self.presenter.get_win_status(self.game.whose_turn()))
        else:
            self.status_label.set_text(self.presenter.get_player_status(self.game.whose_turn()))

    def render(self):
        self.root.title('Gomoku')
        self.root.mainloop()


class GridView:
    def __init__(self, frame, width, height, game):
        self.frame = frame
        self.width = width
        self.height = height

        self.game = game
        self.board = game.get_board()

        self.cell_count = self.board.WIDTH + 1
        self.cell_size = self.width / self.cell_count

        self.canvas = Canvas(self.frame, bg='orange', width=self.width, height=self.width)
        self.draw_grid()
        self.draw_stones()
        self.canvas.pack(expand=True)

        self.click_responder = None

    def set_click_responder(self, responder):
        self.click_responder = responder

    def draw_grid(self):
        for i in range(1, self.cell_count):
            x_pos = i * self.cell_size
            line = self.canvas.create_line((
                x_pos, self.cell_size,
                x_pos, self.cell_size * (self.cell_count - 1)),
                fill='black')
            self.canvas.tag_bind(line, '<Button-1>', self.add_stone)
        for i in range(1, self.cell_count):
            y_pos = i * self.cell_size
            line = self.canvas.create_line((
                self.cell_size, y_pos,
                self.cell_size * (self.cell_count - 1), y_pos),
                fill='black')
            self.canvas.tag_bind(line, '<Button-1>', self.add_stone)

    def draw_stones(self):
        for col in range(0, self.board.WIDTH):
            for row in range(0, self.board.HEIGHT):
                stone = self.board.get(col, row)
                if stone != Player.Empty:
                    color = 'black'
                    if stone == Player.White:
                        color = 'white'
                    center = ((col + 1) * self.cell_size, (row + 1) * self.cell_size)
                    radius = self.cell_size / 3
                    self.canvas.create_oval(
                        center[0] - radius,
                        center[1] - radius,
                        center[0] + radius,
                        center[1] + radius,
                        fill=color)

    def add_stone(self, event):
        clicked_column = int((event.x - self.cell_size) / self.cell_size + .5)
        clicked_row = int((event.y - self.cell_size) / self.cell_size + .5)
        self.click_responder(clicked_column, clicked_row)
        self.draw_stones()
        print(f'{clicked_row}, {clicked_column}')


class StatusLabel:
    def __init__(self, frame, text):
        self.frame = frame
        self.label = Label(frame, text=text)
        self.label.pack()

    def set_text(self, text):
        self.label.configure(text=text)


if __name__ == '__main__':
    view_controller = ViewController()
    view_controller.render()