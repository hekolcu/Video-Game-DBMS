import sqlite3
import tkinter as tk
from Games import Games


class EditGame:

    def __init__(self, master, current_game_id: int, gamesdb_con: sqlite3.Connection):
        self.gamesdb_con = gamesdb_con
        self.game = self.gamesdb_con.cursor().execute("SELECT * FROM GAMES WHERE id = ?", [current_game_id]).fetchone()
        self.current_game_id = current_game_id
        print(self.game["title"])
        print(self.current_game_id)
        self.master = master

        self.mainframe = tk.Frame(
            self.master,
            bg="black"
        )
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 25, "bold"),
            bg="black",
            fg="white"
        )
        self.title.grid(
            row=0,
            column=0,
            columnspan=2
        )

        # start of game frame
        bg_game_frame = "black"
        fg_game_frame = "white"
        font_game_frame = ("Courier", 15, "bold")

        self.game_frame = tk.Frame(
            self.mainframe,
            bg=bg_game_frame
        )
        self.game_frame.grid(
            row=1,
            column=0,
            columnspan=2
        )

        # start of title
        self.title_label = tk.Label(
            self.game_frame,
            text="Title:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.title_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_title = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=3,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_title.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        # end of title

        # start of description
        self.description_label = tk.Label(
            self.game_frame,
            text="Description:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.description_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_description = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=6,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_description.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )
        # end of description

        # start of year
        self.year_label = tk.Label(
            self.game_frame,
            text="Year:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.year_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_year = tk.Entry(
            self.game_frame,
            cursor="arrow",
            width=40,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_year.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )
        # end of year

        # start of genre
        self.genre_label = tk.Label(
            self.game_frame,
            text="Genre:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.genre_label.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_genre = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=4,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_genre.grid(
            row=3,
            column=1,
            padx=5,
            pady=5
        )
        # end of genre

        # start of popularity
        self.popularity_label = tk.Label(
            self.game_frame,
            text="Popularity:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.popularity_label.grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_popularity = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_popularity.grid(
            row=4,
            column=1,
            padx=5,
            pady=5
        )
        # end of popularity

        # start of platform
        self.platform_label = tk.Label(
            self.game_frame,
            text="Platform:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.platform_label.grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_platform = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_platform.grid(
            row=5,
            column=1,
            padx=5,
            pady=5
        )
        # end of platform

        # start of mode
        self.mode_label = tk.Label(
            self.game_frame,
            text="Mode:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.mode_label.grid(
            row=6,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_mode = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_mode.grid(
            row=6,
            column=1,
            padx=5,
            pady=5
        )
        # end of mode

        # start of restrictions
        self.restrictions_label = tk.Label(
            self.game_frame,
            text="Restrictions:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.restrictions_label.grid(
            row=7,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_restrictions = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_restrictions.grid(
            row=7,
            column=1,
            padx=5,
            pady=5
        )
        # end of restrictions

        # start of requirements
        self.requirements_label = tk.Label(
            self.game_frame,
            text="Requirements:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.requirements_label.grid(
            row=8,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_requirements = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_requirements.grid(
            row=8,
            column=1,
            padx=5,
            pady=5
        )
        # end of requirements

        # start of link
        self.link_label = tk.Label(
            self.game_frame,
            text="Link:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.link_label.grid(
            row=9,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_link = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_link.grid(
            row=9,
            column=1,
            padx=5,
            pady=5
        )
        # end of link

        # start of creators
        self.creators_label = tk.Label(
            self.game_frame,
            text="Creators:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.creators_label.grid(
            row=10,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_creators = tk.Text(
            self.game_frame,
            cursor="arrow",
            width=30,
            height=2,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_creators.grid(
            row=10,
            column=1,
            padx=5,
            pady=5
        )
        # end of creators

        # start of rating
        self.rating_label = tk.Label(
            self.game_frame,
            text="Rating:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.rating_label.grid(
            row=11,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_rating = tk.Entry(
            self.game_frame,
            cursor="arrow",
            width=40,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_rating.grid(
            row=11,
            column=1,
            padx=5,
            pady=5
        )
        # end of rating

        # start of rating
        self.rating_count_label = tk.Label(
            self.game_frame,
            text="Rating Count:",
            bg=bg_game_frame,
            fg=fg_game_frame,
            font=font_game_frame
        )
        self.rating_count_label.grid(
            row=12,
            column=0,
            padx=10,
            pady=10,
            sticky=tk.E
        )

        self.game_rating_count = tk.Entry(
            self.game_frame,
            cursor="arrow",
            width=40,
            bg=bg_game_frame,
            fg=fg_game_frame
        )
        self.game_rating_count.grid(
            row=12,
            column=1,
            padx=5,
            pady=5
        )
        # end of ratingCount
        # end of game frame

        self.add_button = tk.Button(
            self.mainframe,
            text="Add",
            bg="black",
            fg="white",
            command=self.add
        )
        self.add_button.grid(
            row=2,
            column=0
        )

        self.back_button = tk.Button(
            self.mainframe,
            text="Back",
            bg="black",
            fg="white",
            command=self.back_to_brief
        )
        self.back_button.grid(
            row=2,
            column=1
        )

    def add(self):
        if len(self.game_title.get("1.0", "end-1c")) > 0 and \
                len(self.game_description.get("1.0", "end-1c")) > 0 and \
                self.game_year.get().isdigit() and \
                len(self.game_genre.get("1.0", "end-1c")) > 0 and \
                len(self.game_popularity.get("1.0", "end-1c")) > 0 and \
                len(self.game_platform.get("1.0", "end-1c")) > 0 and \
                len(self.game_mode.get("1.0", "end-1c")) > 0 and \
                len(self.game_restrictions.get("1.0", "end-1c")) > 0 and \
                len(self.game_requirements.get("1.0", "end-1c")) > 0 and \
                len(self.game_link.get("1.0", "end-1c")) > 0 and \
                len(self.game_creators.get("1.0", "end-1c")) > 0 and \
                isfloat(self.game_rating.get()) and \
                self.game_rating_count.get().isdigit():
            self.gamesdb_con.cursor().execute(
                "INSERT INTO GAMES("
                "title, "
                "description, "
                "year, "
                "genre, "
                "popularity, "
                "platform, "
                "mode, "
                "restrictions, "
                "requirements, "
                "link, "
                "creators, "
                "rating, "
                "ratingCount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [
                    self.game_title.get("1.0", "end-1c"),
                    self.game_description.get("1.0", "end-1c"),
                    int(self.game_year.get()),
                    self.game_genre.get("1.0", "end-1c"),
                    self.game_popularity.get("1.0", "end-1c"),
                    self.game_platform.get("1.0", "end-1c"),
                    self.game_mode.get("1.0", "end-1c"),
                    self.game_restrictions.get("1.0", "end-1c"),
                    self.game_requirements.get("1.0", "end-1c"),
                    self.game_link.get("1.0", "end-1c"),
                    self.game_creators.get("1.0", "end-1c"),
                    float(self.game_rating.get()),
                    int(self.game_rating_count.get())
                ]
            )
            self.gamesdb_con.commit()

    def back_to_brief(self):
        self.mainframe.destroy()
        Games(self.master, self.gamesdb_con, 0)


def isfloat(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
