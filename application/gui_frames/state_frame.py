import tkinter


class state_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root, bg="grey")


        self.title_label = tkinter.Label(self, text="Arm State", bg="grey")
        self.shoulder_base_state = tkinter.Label(self, text=f"shoulder_base: ", bg="grey")
        self.shoulder_state = tkinter.Label(self, text=f"shoulder: ", bg="grey")
        self.elbow_state = tkinter.Label(self, text=f"elbow: ", bg="grey")
        self.wrist_state = tkinter.Label(self, text=f"wrist: ", bg="grey")

        self.shoulder_base_data = tkinter.Label(self, textvariable=root.Arm_state.shoulder_base_iVar, bg="grey")
        self.shoulder_data = tkinter.Label(self, textvariable=root.Arm_state.shoulder_iVar, bg="grey")
        self.elbow_data = tkinter.Label(self, textvariable=root.Arm_state.elbow_iVar, bg="grey")
        self.wrist_data = tkinter.Label(self, textvariable=root.Arm_state.wrist_iVar, bg="grey")

        self.title_label.grid(column=0, row=0, columnspan=2)
        self.shoulder_base_state.grid(column=0, row=1, sticky="w")
        self.shoulder_state.grid(column=0, row=2, sticky="w")
        self.elbow_state.grid(column=0, row=3, sticky="w")
        self.wrist_state.grid(column=0, row=4, sticky="w")
        self.shoulder_base_data.grid(column=1, row=1, sticky="w")
        self.shoulder_data.grid(column=1, row=2, sticky="w")
        self.elbow_data.grid(column=1, row=3, sticky="w")
        self.wrist_data.grid(column=1, row=4, sticky="w")


if(__name__ == "__main__"):
    pass