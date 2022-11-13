import tkinter as tk
from Games import Games


class EditGame:

    def __init__(self, master, games, current_game):
        self.games = games
        self.current_game = current_game
        self.master = master
        self.mainframe = tk.Frame(self.master, bg="green")
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 20, "bold"),
            bg="red"
        )
        self.title.grid(
            row=0,
            column=0
        )

        self.button = tk.Button(self.mainframe, text="Back", bg="lightgreen", command=self.back_to_brief)
        self.button.grid(row=1, column=1)

    def back_to_brief(self):
        self.mainframe.destroy()
        Games(self.master, self.games, self.current_game)
