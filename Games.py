import sqlite3
import tkinter as tk
import webbrowser
import sqlite3
# from sqlite3 import Connection


class Games:

    def __init__(self, master: tk.Tk, gamesdb_con: sqlite3.Connection, current_game=0):
        self.gamesdb_con = gamesdb_con
        self.games = self.gamesdb_con.cursor().execute("SELECT * FROM GAMES").fetchall()
        self.current_game = current_game
        self.master = master
        bg_color = "#808080"
        self.mainframe = tk.Frame(
            self.master,
            width=800,
            bg="black"
        )
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 25, "bold"),
            fg="white",
            bg="black"
        )
        self.title.grid(
            row=0,
            column=0,
            padx=5
        )

        # start of game information frame
        info_bg = "black"

        self.info_frame = tk.Frame(
            self.mainframe,
            bg=info_bg
        )
        self.info_frame.grid(
            row=1,
            column=0,
            pady=10,
            padx=35
        )

        # start of title frame
        self.title_frame = tk.Frame(
            self.info_frame,
            bg=info_bg
        )
        self.title_frame.grid(
            row=0,
            column=0,
            rowspan=2
        )

        # start of title
        self.game_title = tk.Label(
            self.title_frame,
            bg="black",
            fg="white",
            font=("Courier", 20, "bold", "underline"),
            width=35,
            height=0,
            wraplength=515,
            cursor="hand2"
        )
        self.game_title.pack(
            side=tk.TOP
        )
        # end of title

        # start of rating
        self.game_rating = tk.Label(
            self.title_frame,
            bg="black",
            fg="white",
            font=("Courier", 10, "bold")
        )
        self.game_rating.pack(
            side=tk.TOP,
            anchor="w"
        )
        # end of rating
        # end of title frame

        # start of creators
        self.game_creators = tk.Text(
            self.info_frame,
            bg="black",
            fg="white",
            font=("Courier", 12, "bold"),
            borderwidth=0,
            cursor="arrow",
            width=25,
            height=5
        )
        self.game_creators.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="we"
        )
        # end of creators

        # start of platform
        self.game_platform = tk.Label(
            self.info_frame,
            bg=bg_color,
            fg="white",
            font=("Courier", 11, "bold"),
            width=35
        )
        self.game_platform.grid(
            row=1,
            column=1
        )
        # end of platform

        # start of description
        self.game_description = tk.Label(
            self.info_frame,
            bg=bg_color,
            fg="white",
            font=("Courier", 15, "bold"),
            wraplength=500,
            anchor="nw"
        )
        self.game_description.grid(
            row=2,
            column=0,
            ipadx=10,
            pady=10,
            sticky="nsew"
        )
        # end of description

        # start of side information frame
        self.side_information_frame = tk.Frame(
            self.info_frame
        )
        self.side_information_frame.grid(
            row=2,
            column=1,
            padx=20
        )

        # start of genre
        self.game_genre = tk.Label(
            self.side_information_frame,
            font=("Courier", 11, "bold"),
            width=30,
            anchor=tk.W
        )
        self.game_genre.pack(
            side=tk.TOP,
            pady=10,
            padx=15
        )
        # end of genre

        # start of mode
        self.game_mode = tk.Label(
            self.side_information_frame,
            font=("Courier", 11, "bold"),
            width=30,
            anchor=tk.W
        )
        self.game_mode.pack(
            side=tk.TOP,
            padx=15
        )
        # end of mode

        # start of restrictions
        self.game_restrictions = tk.Label(
            self.side_information_frame,
            font=("Courier", 11, "bold"),
            width=30,
            anchor=tk.W
        )
        self.game_restrictions.pack(
            side=tk.TOP,
            pady=10
        )
        # end of restrictions

        # start of popularity
        self.game_popularity = tk.Label(
            self.side_information_frame,
            font=("Courier", 11, "bold"),
            bg=bg_color,
            fg="white",
            width=35,
            anchor=tk.W
        )
        self.game_popularity.pack(
            side=tk.TOP
        )
        # end of popularity
        # end of side information frame

        # start of requirements
        self.game_requirements = tk.Label(
            self.info_frame,
            bg="#000066",
            fg="white",
            font=("Courier", 10, "bold"),
            wraplength=900
        )
        self.game_requirements.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20,
            sticky="we"
        )
        # end of requirements

        self.update_info_frame()
        # end of current game information

        # start of button frame
        button_font = ("Courier", 15, "bold")

        self.button_frame = tk.Frame(
            self.mainframe,
            bg="black"
        )
        self.button_frame.grid(
            row=2,
            column=0
        )

        self.previous_button = tk.Button(
            self.button_frame,
            text="<",
            bg="darkgray",
            fg="black",
            font=button_font,
            activebackground="lightgray",
            activeforeground="blue",
            cursor="hand2",
            command=self.previous_button_action
        )
        self.previous_button.grid(
            row=0,
            column=0
        )

        self.add_button = tk.Button(
            self.button_frame,
            text="Add",
            bg="red",
            font=button_font,
            cursor="hand2",
            width=5,
            command=self.add_button_action
        )
        self.add_button.grid(
            row=0,
            column=1,
            padx=10
        )

        self.edit_button = tk.Button(
            self.button_frame,
            text="Edit",
            bg="red",
            font=button_font,
            cursor="hand2",
            width=5,
            command=self.edit_button_action
        )
        self.edit_button.grid(
            row=0,
            column=2,
            padx=10
        )

        self.next_button = tk.Button(
            self.button_frame,
            text=">",
            bg="darkgray",
            fg="black",
            font=button_font,
            cursor="hand2",
            activebackground="lightgray",
            activeforeground="blue",
            command=self.next_button_action
        )
        self.next_button.grid(
            row=0,
            column=3
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
        from EditAddGame import EditAddGame
        self.mainframe.destroy()
        EditAddGame(self.master, self.gamesdb_con, self.games[self.current_game]["id"])

    def add_button_action(self):
        from EditAddGame import EditAddGame
        self.mainframe.destroy()
        EditAddGame(self.master, self.gamesdb_con)

    def update_info_frame(self):
        self.game_title.config(
            text=str(self.games[self.current_game]["title"]) + " (" + str(self.games[self.current_game]["year"]) + ")"
        )
        self.game_title.bind(
            "<Button-1>", lambda e: webbrowser.open_new(self.games[self.current_game]["link"])
        )
        self.game_description.config(
            text="Description: " + self.games[self.current_game]["description"]
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
            text="Minimum Requirements: " + self.games[self.current_game]["requirements"]
        )
        self.game_popularity.config(
            text=self.games[self.current_game]["popularity"]
        )
        self.game_rating.config(
            text=str(self.games[self.current_game]["rating"]) + " (" +
            str(self.games[self.current_game]["ratingCount"]) +
            " ratings)"
        )
        creators = str(self.games[self.current_game]["creators"]).split(";")
        self.game_creators.config(state="normal")
        self.game_creators.delete(1.0, tk.END)
        self.game_creators.insert(tk.END, "By ")
        for creator in creators:
            self.game_creators.insert(tk.END, creator.strip() + "\n")
        self.game_creators.config(state="disabled")
