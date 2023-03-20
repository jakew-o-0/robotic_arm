import tkinter
from arm_sate import arm_state
from gui_frames.state_frame import state_frame
from gui_frames.set_state_frame import set_state_frame





class gui(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("robotic arm controller application")
        self.resizable(False,False)

        self.Arm_state = arm_state(self)
        
        State_frame = state_frame(self)
        Set_state_frame = set_state_frame(self)

        State_frame.grid(column=0, row=0, padx=10, pady=5, sticky="w")
        Set_state_frame.grid(column=0, row=1, padx=10, pady=5, ipadx=2)

        

if(__name__ == "__main__"):
    Gui = gui()
    Gui.mainloop()