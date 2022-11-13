import tkinter as tk


class Games:

    def __init__(self, master: tk.Tk, games: dict, current_game=0):
        self.games = games
        self.current_game = current_game
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

        # start of game information frame
        info_font = ("Helvetica", 15, "bold")
        info_bg = "red"

        self.info_frame = tk.Frame(
            self.mainframe,
            bg=info_bg
        )
        self.info_frame.grid(
            row=1,
            column=0,
            pady=10
        )

        # start of title
        self.title_label = tk.Label(
            self.info_frame,
            text="Title:",
            bg=info_bg,
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
            bg=info_bg,
            width=30,
            font=info_font
        )
        self.game_title.grid(
            row=0,
            column=1
        )
        # end of title

        # start of description
        self.description_label = tk.Label(
            self.info_frame,
            text="Description:",
            bg=info_bg,
            width=10,
            font=info_font
        )
        self.description_label.grid(
            row=0,
            column=0
        )

        self.game_title = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["description"],
            bg=info_bg,
            width=30,
            font=info_font
        )
        self.game_title.grid(
            row=0,
            column=1
        )
        # end of description

        # start of genre
        self.genre_label = tk.Label(
            self.info_frame,
            text="Genre:",
            bg=info_bg,
            font=info_font
        )
        self.genre_label.grid(
            row=1,
            column=0
        )

        self.game_genre = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["genre"],
            bg=info_bg,
            font=info_font
        )
        self.game_genre.grid(
            row=1,
            column=1
        )
        # end of genre

        # start of rating
        self.rating_label = tk.Label(
            self.info_frame,
            text="Rating:",
            bg=info_bg,
            font=info_font
        )
        self.rating_label.grid(
            row=2,
            column=0
        )

        self.game_rating = tk.Label(
            self.info_frame,
            text=self.games[self.current_game]["rating"],
            bg=info_bg,
            font=info_font
        )
        self.game_rating.grid(
            row=2,
            column=1
        )
        # end of rating
        # end of current game information

        # start of button frame
        button_font = ("Helvetica", 20, "italic")

        self.button_frame = tk.Frame(
            self.mainframe,
            bg="purple"
        )
        self.button_frame.grid(
            row=2,
            column=0
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
            column=1
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
            column=2
        )
        # end of button frame

    def next_button_action(self):
        number_of_games = len(self.games)
        if self.current_game < number_of_games - 1:
            self.current_game += 1
            self.update_info_frame()

    def previous_button_action(self):
        if self.current_game > 0:
            self.current_game -= 1
            self.update_info_frame()

    def edit_button_action(self):
        from EditGame import EditGame
        self.mainframe.destroy()
        EditGame(self.master, self.games, self.current_game)

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
