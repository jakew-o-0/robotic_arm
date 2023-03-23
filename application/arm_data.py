import tkinter
import serial
from gui_toplevel_windows.error_window import error_win


class arm_state:
    def __init__(self, root) -> None:
        self.root = root

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


        # port data
        self.serial_port = serial.Serial()
        self.is_port_open = tkinter.StringVar()
        self.is_port_open.set("False")

    def init_serial(self, baudrate, port, timeout):
        try:
            self.serial_port.baudrate = baudrate
            self.serial_port.port = port
            self.serial_port.timeout = timeout
            
            self.serial_port.open()
            self.is_port_open.set(str(self.serial_port.is_open))
        except Exception as e:
            error_win(self.root, e)


    def use_controller_input(self):
        pass

    def use_pattern(self):
        pass

    def send_data(self):
        msg = 0xF100 & self.shoulder_base_iVar.get()
        self.serial_port.write(msg)

        msg = 0xF100 & self.shoulder_iVar.get()
        self.serial_port.write(msg)
        
        msg = 0xF100 & self.elbow_iVar.get()
        self.serial_port.write(msg)

        msg = 0xF100 & self.wrist_iVar.get()
        self.serial_port.write(msg)



if(__name__ == "__main__"):
    pass