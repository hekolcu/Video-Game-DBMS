import sqlite3
import tkinter as tk
from Games import Games


def fetchDB():
    gamesdb_con = sqlite3.connect("./gamesDB.db")
    gamesdb_con.row_factory = sqlite3.Row
    gamesdb_cursor = gamesdb_con.cursor()

    gamesdb_cursor.execute("DROP TABLE GAMES")
    gamesdb_cursor.execute("CREATE TABLE IF NOT EXISTS GAMES("
                           "id INTEGER PRIMARY KEY AUTOINCREMENT, "
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
                           "ratingCount"
                           ")"
                           )
    from VideoGamesData import games
    gamesdb_cursor.executemany("INSERT INTO GAMES("
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
                               "ratingCount"
                               ") VALUES("
                               ":title, "
                               ":description, "
                               ":year, "
                               ":genre, "
                               ":popularity, "
                               ":platform, "
                               ":mode, "
                               ":restrictions, "
                               ":requirements, "
                               ":link, "
                               ":creators, "
                               ":rating, "
                               ":ratingCount)", games)
    gamesdb_con.commit()
    return gamesdb_con


def main():
    root = tk.Tk()
    root.title("Video Games DBMS")
    root.resizable(False, False)
    Games(root, fetchDB())
    root.mainloop()


if __name__ == '__main__':
    main()
