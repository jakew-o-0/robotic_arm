import tkinter
from error_window import error_win


class set_state_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root, background="grey")

        self.title_label = tkinter.Label(self, text="Set Arm State", bg="grey")
        self.shoulder_base_label = tkinter.Label(self, text="shoulder_base: ", bg="grey")
        self.shoulder_label = tkinter.Label(self, text="shoulder: ", bg="grey")
        self.elbow_label = tkinter.Label(self, text="elbow: ", bg="grey")
        self.wrist_label = tkinter.Label(self, text="wrist: ", bg="grey")

        self.shoulder_base_iVar = tkinter.IntVar()
        self.shoulder_iVar = tkinter.IntVar()
        self.elbow_iVar = tkinter.IntVar()
        self.wrist_iVar = tkinter.IntVar()

        self.shoulder_base_entry = tkinter.Entry(self, textvariable=self.shoulder_base_iVar)
        self.shoulder_entry = tkinter.Entry(self, textvariable=self.shoulder_iVar)
        self.elbow_entry = tkinter.Entry(self, textvariable=self.elbow_iVar)
        self.wrist_entry = tkinter.Entry(self, textvariable=self.wrist_iVar)

        self.set_button = tkinter.Button(self, text="Set State", command=lambda: self.update_state(root))


        self.title_label.grid(column=0, row=0, columnspan=2)
        self.shoulder_base_label.grid(column=0, row=1)
        self.shoulder_label.grid(column=0, row=2)
        self.elbow_label.grid(column=0, row=3)
        self.wrist_label.grid(column=0, row=4)
        self.shoulder_base_entry.grid(column=1, row=1)
        self.shoulder_entry.grid(column=1, row=2)
        self.elbow_entry.grid(column=1, row=3)
        self.wrist_entry.grid(column=1, row=4)
        self.set_button.grid(column=0, row=5, columnspan=2, pady=3)

    def update_state(self, root):
        try:
            root.Arm_state.shoulder_base_iVar.set(self.shoulder_base_iVar.get())
            root.Arm_state.shoulder_iVar.set(self.shoulder_iVar.get())
            root.Arm_state.elbow_iVar.set(self.elbow_iVar.get()) 
            root.Arm_state.wrist_iVar.set(self.wrist_iVar.get())
            root.update()

        except(ValueError):
            error_win(self, "invalid input, input must be a number")


if(__name__ == "__main__"):
    pass