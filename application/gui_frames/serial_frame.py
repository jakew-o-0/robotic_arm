import tkinter


class serial_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="grey")

        self.connectivity_label = tkinter.Label(self, text="Serial Connection: ", bg="grey")
        self.connectivity = tkinter.Label(self, textvariable=None, bg="grey")
        self.connect_button = tkinter.Button(self, text="connect", command=lambda:self.connect())

        self.connectivity_label.grid(column=0, row=0)
        self.connectivity.grid(column=1, row=0)
        self.connect_button.grid(column=0, row=1, columnspan=2)

    def connect(self):
        pass


if(__name__ ==  "__main__"):
    pass