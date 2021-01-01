import tkinter as tk


class NewGameButton:
    def __init__(self, frame):
        self.frame = frame
        self.new_game_responder = None
        self.button = tk.Button(frame, text='New Game', command=self.new_game_responder)
        self.button.pack()

    def set_new_game_responder(self, responder):
        self.new_game_responder = responder
        self.button.configure(text='New Game', command=self.new_game_responder)
