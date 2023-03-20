import tkinter


class error_win(tkinter.Toplevel):
    def __init__(self, root, error_msg):
        super().__init__(root)

        error = tkinter.Label(self, text=error_msg, fg="red")
        error.pack()


if(__name__ == "__main__"):
    pass