import tkinter


class set_pattern(tkinter.Toplevel):
    def __init__(self, root):
        super().__init__(root)

        
        self.shoulder_base_label = tkinter.Label(self, text="shoulder base: ")
        self.shoulder_label = tkinter.Label(self, text="shoulder: ")
        self.elbow_label = tkinter.Label(self, text="elbow: ")
        self.wrist_label = tkinter.Label(self, text="wrist: ")

        self.shoulder_base_iVar = tkinter.IntVar()
        self.shoulder_iVar = tkinter.IntVar()
        self.elbow_iVar = tkinter.IntVar()
        self.wrist_iVar = tkinter.IntVar()

        self.shoulder_base_entry = tkinter.Entry(self, textvariable=self.shoulder_base_iVar, width=8)
        self.shoulder_entry = tkinter.Entry(self, textvariable=self.shoulder_iVar, width=8)
        self.elbow_entry = tkinter.Entry(self, textvariable=self.elbow_iVar, width=8)
        self.wrist_entry = tkinter.Entry(self, textvariable=self.wrist_iVar, width=8)

        self.set_button = tkinter.Button(self, text="add step")
        self.remove_button = tkinter.Button(self, text="remove step")
        self.save_button = tkinter.Button(self, text="save pattern")


        self.shoulder_base_label.grid(column=0, row=1, sticky="e")
        self.shoulder_label.grid(column=0, row=2, sticky="e")
        self.elbow_label.grid(column=0, row=3, sticky="e")
        self.wrist_label.grid(column=0, row=4, sticky="e")
        self.shoulder_base_entry.grid(column=1, row=1)
        self.shoulder_entry.grid(column=1, row=2)
        self.elbow_entry.grid(column=1, row=3)
        self.wrist_entry.grid(column=1, row=4)
        self.set_button.grid(column=2, row=1)
        self.remove_button.grid(column=2, row=2)
        self.save_button.grid(column=2, row=3)


if(__name__ == "__main__"):
    pass