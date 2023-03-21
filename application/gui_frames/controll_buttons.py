import tkinter
from gui_toplevel_windows.set_pattern_window import set_pattern


class controll_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="grey")

        self.controller_button = tkinter.Button(self, text="enable controller", command=lambda: root.Arm_state.use_controller_input())
        self.set_pattern_button = tkinter.Button(self, text="set pattern", command=lambda: set_pattern(root))
        self.use_pattern_button = tkinter.Button(self, text="use pattern", command=lambda: root.Arm_state.use_pattern())

        self.controller_button.pack()
        self.set_pattern_button.pack()
        self.use_pattern_button.pack()


if(__name__ == "__main__"):
    pass