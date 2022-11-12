import tkinter as tk


class FirstFrame:

    def __init__(self, master: tk.Tk, games):
        self.games = games
        self.master = master
        self.mainframe = tk.Frame(
            self.master,
            bg="red"
        )
        self.mainframe.grid()

        self.title = tk.Label(
            self.mainframe,
            text="Video Games",
            font=("Courier", 20, "bold"),
            bg="red"
        )
        self.title.grid(
            row=0,
            column=0,
            columnspan=3
        )

        self.button = tk.Button(
            self.mainframe,
            text="Switch",
            bg="darkred",
            command=self.switch
        )
        self.button.grid(
            row=3,
            column=3
        )

        self.info_frame = tk.Frame(
            self.master,
            bg="yellow"
        )
        self.info_frame.grid(
            row=1,
            column=0,
            columnspan=3
        )

        self.next_button = tk.Button(
            self.mainframe,
            text=">",
            bg="blue",
            command=self.next_button_action
        )
        self.next_button.grid(
            row=2,
            column=3
        )

        self.previous_button = tk.Button(
            self.mainframe,
            text="<",
            bg="blue",
            command=self.previous_button_action
        )
        self.previous_button.grid(
            row=2,
            column=0
        )

        self.more_detail_button = tk.Button(
            self.mainframe,
            text="Show",
            bg="green",
            command=self.more_detail_button_action
        )

    def switch(self):
        self.mainframe.destroy()
        SecondFrame(self.master, self.games)

    def next_button_action(self):
        print(self, "next")  # yet to be added

    def previous_button_action(self):
        print(self, "prev")  # yet to be added

    def more_detail_button_action(self):
        print(self, "show")  # yet to be added


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
