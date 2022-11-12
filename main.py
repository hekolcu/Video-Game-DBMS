import tkinter as tk


class FirstFrame:

    def __init__(self, master: tk.Tk, games: dict):
        self.games = games
        self.current_game = 0
        self.master = master
        self.mainframe = tk.Frame(
            self.master,
            bg="red"
        )
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 30, "bold"),
            bg="red"
        )
        self.title.grid(
            row=0,
            column=0
        )

        # start of current game information frame

        info_font = ("Helvetica", 15, "bold")

        self.info_frame = tk.Frame(
            self.mainframe,
            bg="yellow"
        )
        self.info_frame.grid(
            row=1,
            column=0,
            pady=10
        )

        self.title_label = tk.Label(
            self.info_frame,
            text="Title:",
            bg="yellow",
            width=10,
            font=info_font
        )
        self.title_label.grid(
            row=0,
            column=0
        )

        self.game_title = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["title"],
            bg="yellow",
            width=30,
            font=info_font
        )
        self.game_title.grid(
            row=0,
            column=1
        )

        self.genre_label = tk.Label(
            self.info_frame,
            text="Genre:",
            bg="yellow",
            font=info_font
        )
        self.genre_label.grid(
            row=1,
            column=0
        )

        self.game_genre = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["genre"],
            bg="yellow",
            font=info_font
        )
        self.game_genre.grid(
            row=1,
            column=1
        )

        self.rating_label = tk.Label(
            self.info_frame,
            text="Rating:",
            bg="yellow",
            font=info_font
        )
        self.rating_label.grid(
            row=2,
            column=0
        )

        self.game_rating = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["rating"],
            bg="yellow",
            font=info_font
        )
        self.game_rating.grid(
            row=2,
            column=1
        )

        # end of current game information
        # start of button frame

        button_font = ("Helvetica", 20, "italic")

        self.button_frame = tk.Frame(
            self.mainframe,
            bg="purple"
        )
        self.button_frame.grid(
            row=2,
            column=0,
            columnspan=4
        )

        self.previous_button = tk.Button(
            self.button_frame,
            text="<",
            bg="blue",
            fg="white",
            font=button_font,
            width=7,
            command=self.previous_button_action
        )
        self.previous_button.grid(
            row=0,
            column=0
        )

        self.more_detail_button = tk.Button(
            self.button_frame,
            text="Show",
            bg="green",
            font=button_font,
            width=7,
            command=self.more_detail_button_action
        )
        self.more_detail_button.grid(
            row=0,
            column=1
        )

        self.edit_button = tk.Button(
            self.button_frame,
            text="Edit",
            bg="red",
            font=button_font,
            width=7,
            command=self.edit_button_action
        )
        self.edit_button.grid(
            row=0,
            column=2
        )

        self.next_button = tk.Button(
            self.button_frame,
            text=">",
            bg="blue",
            fg="white",
            font=button_font,
            width=7,
            command=self.next_button_action
        )
        self.next_button.grid(
            row=0,
            column=3
        )
        # end of button frame

    def switch(self):
        self.mainframe.destroy()
        SecondFrame(self.master, self.games)

    def next_button_action(self):
        number_of_games = len(self.games)
        if self.current_game < number_of_games - 1:
            self.current_game += 1
            self.update_info_frame()

    def previous_button_action(self):
        if self.current_game > 0:
            self.current_game -= 1
            self.update_info_frame()

    def more_detail_button_action(self):
        print(self, "show")  # yet to be added

    def edit_button_action(self):
        print(self, "show")  # yet to be added

    def update_info_frame(self):
        self.game_title.config(
            text=self.games[self.current_game]["title"]
        )
        self.game_genre.config(
            text=self.games[self.current_game]["genre"]
        )
        self.game_rating.config(
            text=self.games[self.current_game]["rating"]
        )


class SecondFrame:

    def __init__(self, master, games):
        self.games = games
        self.master = master
        self.mainframe = tk.Frame(self.master, bg="green")
        self.mainframe.grid()

        self.title = tk.Label(self.mainframe, text="Video Games", font=("Courier", 20, "bold"), bg="red")
        self.title.grid(row=0, column=0, columnspan=3)

        self.button = tk.Button(self.mainframe, text="Back", bg="lightgreen", command=self.switch)
        self.button.grid(row=1, column=1)

    def switch(self):
        self.mainframe.destroy()
        FirstFrame(self.master, self.games)


def main():
    from VideoGamesData import games
    root = tk.Tk()
    FirstFrame(root, games)
    root.mainloop()


if __name__ == '__main__':
    main()
