import tkinter


class controll_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="grey")

        self.controller_button = tkinter.Button(self, text="enable controller")
        self.set_pattern_button = tkinter.Button(self, text="set pattern")
        self.use_pattern_button = tkinter.Button(self, text="use pattern")


if(__name__ == "__main__"):
    pass