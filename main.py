import tkinter as tk
from BriefGame import BriefGame


def main():
    from VideoGamesData import games
    root = tk.Tk()
    BriefGame(root, games)
    root.mainloop()


if __name__ == '__main__':
    main()
