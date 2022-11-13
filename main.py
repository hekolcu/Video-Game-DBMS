import tkinter as tk
from Games import Games


def main():
    from VideoGamesData import games
    root = tk.Tk()
    Games(root, games)
    root.mainloop()


if __name__ == '__main__':
    main()
