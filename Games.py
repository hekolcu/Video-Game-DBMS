import tkinter as tk


class Games:

    def __init__(self, master: tk.Tk, games: dict, current_game=0):
        self.games = games
        self.current_game = current_game
        self.master = master
        self.mainframe = tk.Frame(
            self.master,
            width=800,
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
            font=info_font
        )
        self.title_label.grid(
            row=0,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_title = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_title.grid(
            row=0,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of title

        # start of description
        self.description_label = tk.Label(
            self.info_frame,
            text="Description:",
            bg=info_bg,
            font=info_font
        )
        self.description_label.grid(
            row=1,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_description = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_description.grid(
            row=1,
            column=1,
            pady=15,
            sticky="w",
            padx=20
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
            row=2,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_genre = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_genre.grid(
            row=2,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of genre

        # start of platform
        self.platform_label = tk.Label(
            self.info_frame,
            text="Platform:",
            bg=info_bg,
            font=info_font
        )
        self.platform_label.grid(
            row=3,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_platform = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_platform.grid(
            row=3,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of platform

        # start of mode
        self.mode_label = tk.Label(
            self.info_frame,
            text="Mode:",
            bg=info_bg,
            font=info_font
        )
        self.mode_label.grid(
            row=4,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_mode = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_mode.grid(
            row=4,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of mode

        # start of restrictions
        self.restrictions_label = tk.Label(
            self.info_frame,
            text="Restrictions:",
            bg=info_bg,
            font=info_font
        )
        self.restrictions_label.grid(
            row=5,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_restrictions = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_restrictions.grid(
            row=5,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of restrictions

        # start of requirements
        self.requirements_label = tk.Label(
            self.info_frame,
            text="Requirements:",
            bg=info_bg,
            font=info_font
        )
        self.requirements_label.grid(
            row=6,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_requirements = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_requirements.grid(
            row=6,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of requirements

        # start of year
        self.year_label = tk.Label(
            self.info_frame,
            text="Year:",
            bg=info_bg,
            font=info_font
        )
        self.year_label.grid(
            row=7,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_year = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_year.grid(
            row=7,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of year

        # start of popularity
        self.popularity_label = tk.Label(
            self.info_frame,
            text="Popularity:",
            bg=info_bg,
            font=info_font
        )
        self.popularity_label.grid(
            row=8,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_popularity = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_popularity.grid(
            row=8,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of popularity

        # start of rating
        self.rating_label = tk.Label(
            self.info_frame,
            text="Rating:",
            bg=info_bg,
            font=info_font
        )
        self.rating_label.grid(
            row=9,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_rating = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_rating.grid(
            row=9,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of rating

        # start of link
        self.link_label = tk.Label(
            self.info_frame,
            text="Link:",
            bg=info_bg,
            font=info_font
        )
        self.link_label.grid(
            row=10,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_link = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_link.grid(
            row=10,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of link

        # start of creators
        self.creators_label = tk.Label(
            self.info_frame,
            text="Creators:",
            bg=info_bg,
            font=info_font
        )
        self.creators_label.grid(
            row=11,
            column=0,
            sticky="e",
            padx=20
        )

        self.game_creators = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_creators.grid(
            row=11,
            column=1,
            pady=15,
            sticky="w",
            padx=20
        )
        # end of creators

        self.update_info_frame()
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
        self.game_description.config(
            text=self.games[self.current_game]["description"]
        )
        self.game_genre.config(
            text=self.games[self.current_game]["genre"]
        )
        self.game_platform.config(
            text=self.games[self.current_game]["platform"]
        )
        self.game_mode.config(
            text=self.games[self.current_game]["mode"]
        )
        self.game_restrictions.config(
            text=self.games[self.current_game]["restrictions"]
        )
        self.game_requirements.config(
            text=self.games[self.current_game]["requirements"]
        )
        self.game_year.config(
            text=self.games[self.current_game]["year"]
        )
        self.game_popularity.config(
            text=self.games[self.current_game]["popularity"]
        )
        self.game_rating.config(
            text=
            str(self.games[self.current_game]["rating"]) + " (" +
            str(self.games[self.current_game]["ratingCount"]) +
            " ratings)"
        )
        self.game_link.config(
            text=self.games[self.current_game]["link"]
        )
        self.game_creators.config(
            text=self.games[self.current_game]["creators"]
        )

