import tkinter as tk
from ui.grid_view import GridView
from ui.status_label import StatusLabel
from ui.game_presenter import GamePresenter
from ui.new_game_button import NewGameButton
from business_rules.game import Game


class ViewController:
    def __init__(self):
        self.root = tk.Tk()
        self.WIDTH = 400
        self.HEIGHT = 600

        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        self.root.resizable(height=0, width=0)

        self.frame = tk.Frame(self.root, bg='blue')
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.game = Game()
        self.presenter = GamePresenter()

        self.status_label = StatusLabel(
            self.frame,
            text=self.presenter.get_player_status(self.game.whose_turn())
        )
        self.grid_view = GridView(
            self.frame,
            width=self.WIDTH,
            height=self.HEIGHT,
            board=self.game.get_board()
        )
        self.grid_view.set_click_responder(lambda col, row: self.respond_to_click(col, row))
        self.new_game_button = NewGameButton(
            self.frame
        )
        self.new_game_button.set_new_game_responder(lambda: self.respond_to_new_game())

    def respond_to_new_game(self):
        self.game = self.game.make_new_game()
        self.grid_view.reset(self.game.get_board())
        self.status_label.set_text(self.presenter.get_player_status(self.game.whose_turn()))

    def respond_to_click(self, column, row):
        clicking_player = self.game.whose_turn()
        self.game.take_turn(column, row)
        if self.game.get_rules().is_win(self.game.get_board(), clicking_player):
            self.status_label.set_text(self.presenter.get_win_status(clicking_player))
            self.grid_view.unset_click_tag()
        else:
            self.status_label.set_text(self.presenter.get_player_status(self.game.whose_turn()))

    def render(self):
        self.root.title('Gomoku')
        self.root.mainloop()


if __name__ == '__main__':
    view_controller = ViewController()
    view_controller.render()