import tkinter as tk
from business_rules.board import Player


class GridView:
    def __init__(self, frame, width, height, board):
        self.frame = frame
        self.width = width
        self.height = height

        self.board = board
        self.cell_count = self.board.WIDTH + 1
        self.cell_size = self.width / self.cell_count

        self.canvas = tk.Canvas(self.frame, bg='orange', width=self.width, height=self.width)
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

