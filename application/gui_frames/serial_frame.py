import tkinter


class serial_frame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="grey")


        self.baudrate = tkinter.IntVar()
        self.port = tkinter.StringVar()
        self.timeout = tkinter.IntVar()
        self.connectivity_var = root.Arm_state.is_port_open
        

        self.connectivity_label = tkinter.Label(self, text="Connection: ", bg="grey")
        self.connectivity = tkinter.Label(self, textvariable=self.connectivity_var, bg="grey")

        self.port_label = tkinter.Label(self, text="port: ", bg="grey")
        self.baudrate_label = tkinter.Label(self, text="baudrate: ", bg="grey")
        self.timeout_label = tkinter.Label(self, text="timeout: ", bg="grey")

        self.port_entry = tkinter.Entry(self, textvariable=self.port, width=15)
        self.baudrate_entry = tkinter.Entry(self, textvariable=self.baudrate, width=15)
        self.timeout_entry = tkinter.Entry(self, textvariable=self.timeout, width=15)

        self.connect_button = tkinter.Button(self, text="connect", command=lambda: root.Arm_state.init_serial(self.baudrate.get(), self.port.get(), self.timeout.get()))

        self.connectivity_label.grid(column=0, row=0)
        self.connectivity.grid(column=1, row=0, sticky="w")
        self.connect_button.grid(column=0, row=5, columnspan=2)
        self.port_label.grid(column=0, row=2, sticky="w")
        self.port_entry.grid(column=1, row=2)
        self.baudrate_label.grid(column=0, row=3, sticky="w")
        self.baudrate_entry.grid(column=1, row=3)
        self.timeout_label.grid(column=0, row=4, sticky="w")
        self.timeout_entry.grid(column=1, row=4)



if(__name__ ==  "__main__"):
    pass