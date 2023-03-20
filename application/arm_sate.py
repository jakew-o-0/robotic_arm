import tkinter


class arm_state:
    def __init__(self, root) -> None:
        # create data strucure
        self.shoulder_base_iVar = tkinter.IntVar()
        self.shoulder_iVar = tkinter.IntVar()
        self.elbow_iVar = tkinter.IntVar()
        self.wrist_iVar = tkinter.IntVar()

        # set initial data
        self.elbow_iVar.set(50)
        self.shoulder_iVar.set(60)
        self.shoulder_base_iVar.set(90)
        self.wrist_iVar.set(90)


if(__name__ == "__main__"):
    pass