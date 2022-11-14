import tkinter as tk
import webbrowser


class Games:

    def __init__(self, master: tk.Tk, games: dict, current_game=0):
        self.games = games
        self.current_game = current_game
        self.master = master
        bg_color = "#808080"
        self.mainframe = tk.Frame(
            self.master,
            width=800,
            bg=bg_color
        )
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 30, "bold"),
            fg="white",
            bg=bg_color
        )
        self.title.grid(
            row=0,
            column=0,
            padx=5
        )

        # start of game information frame
        info_font = ("Helvetica", 15, "bold")
        info_bg = bg_color

        self.info_frame = tk.Frame(
            self.mainframe,
            bg=info_bg
        )
        self.info_frame.grid(
            row=1,
            column=0,
            pady=10
        )

        # start of title frame
        self.title_frame = tk.Frame(
            self.info_frame,
            bg="yellow"
        )
        self.title_frame.grid(
            row=0,
            column=0,
            rowspan=2
        )

        # start of title
        self.game_title = tk.Label(
            self.title_frame,
            bg="yellow",
            fg="#232069",
            font=("Helvetica", 20, "bold", "underline"),
            width=20,
            height=3,
            wraplength=415
        )
        self.game_title.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w"
        )
        # end of title

        # start of rating
        self.game_rating = tk.Label(
            self.title_frame,
            bg=info_bg,
            font=info_font
        )
        self.game_rating.grid(
            row=1,
            column=0,
            padx=5,
            sticky="w"
        )
        # end of rating
        # end of title frame

        # start of creators
        self.game_creators = tk.Text(
            self.info_frame,
            bg=info_bg,

            cursor="arrow",
            width=25,
            height=5
        )
        self.game_creators.grid(
            row=0,
            column=1,
            sticky="w"
        )
        # end of creators

        # start of platform
        self.game_platform = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font
        )
        self.game_platform.grid(
            row=1,
            column=1,
            sticky="w"
        )
        # end of platform

        # start of description
        self.game_description = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=400
        )
        self.game_description.grid(
            row=2,
            column=0,
            rowspan=6,
            sticky="w"
        )
        # end of description

        # start of side information frame
        self.side_information_frame = tk.Frame(
            self.info_frame,
            bg=info_bg
        )
        self.side_information_frame.grid(
            row=2,
            column=1
        )

        # start of genre
        self.game_genre = tk.Label(
            self.side_information_frame,
            bg=info_bg,
            font=info_font
        )
        self.game_genre.pack(
            side=tk.TOP,
            anchor=tk.W
        )
        # end of genre

        # start of mode
        self.game_mode = tk.Label(
            self.side_information_frame,
            bg=info_bg,
            font=info_font
        )
        self.game_mode.pack(
            side=tk.TOP,
            anchor=tk.W
        )
        # end of mode

        # start of restrictions
        self.game_restrictions = tk.Label(
            self.side_information_frame,
            bg=info_bg,
            font=info_font
        )
        self.game_restrictions.pack(
            side=tk.TOP,
            anchor=tk.W
        )
        # end of restrictions
        # end of side information frame

        # start of requirements
        self.game_requirements = tk.Label(
            self.info_frame,
            bg=info_bg,
            font=info_font,
            wraplength=500
        )
        self.game_requirements.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w"
        )
        # end of requirements

        # start of popularity
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

        # start of link
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

        self.update_info_frame()
        # end of current game information

        # start of button frame
        button_font = ("Helvetica", 15, "bold")

        self.button_frame = tk.Frame(
            self.mainframe,
            bg="gray"
        )
        self.button_frame.grid(
            row=2,
            column=0
        )

        self.previous_button = tk.Button(
            self.button_frame,
            text="<",
            bg="black",
            fg="white",
            font=button_font,
            #width=7,
            activebackground="lightgray",
            activeforeground="blue",
            cursor="hand2",
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
            #width=7,
            cursor="hand2",
            command=self.edit_button_action
        )
        self.edit_button.grid(
            row=0,
            column=1,
            padx=10
        )

        self.next_button = tk.Button(
            self.button_frame,
            text=">",
            bg="black",
            fg="white",
            font=button_font,
            #width=7,
            cursor="hand2",
            activebackground="lightgray",
            activeforeground="blue",
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
            text=self.games[self.current_game]["title"] + " (" + str(self.games[self.current_game]["year"]) + ")"
        )
        self.game_title.bind(
            "<Button-1>", lambda e: webbrowser.open_new(self.games[self.current_game]["link"])
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
        self.game_popularity.config(
            text=self.games[self.current_game]["popularity"]
        )
        self.game_rating.config(
            text=str(self.games[self.current_game]["rating"]) + " (" +
            str(self.games[self.current_game]["ratingCount"]) +
            " ratings)"
        )
        self.game_link.config(
            text=self.games[self.current_game]["link"]
        )
        creators = str(self.games[self.current_game]["creators"]).split(";")
        self.game_creators.config(state="normal")
        self.game_creators.delete(1.0, tk.END)
        self.game_creators.insert(tk.END, "by\n")
        for creator in creators:
            self.game_creators.insert(tk.END, creator.strip())
        self.game_creators.config(state="disabled")
