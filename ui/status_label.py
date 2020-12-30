import tkinter as tk


class StatusLabel:
    def __init__(self, frame, text):
        self.frame = frame
        self.label = tk.Label(frame, text=text)
        self.label.pack()

    def set_text(self, text):
        self.label.configure(text=text)