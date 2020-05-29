from Tkinter import *
import controls

class SettingsWindow:
    def __init__(self, settings):
        self.settings = settings
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title("Settings controller")
        self.window.geometry('200x200')

        self.set_components()

    def run(self):
        self.window.mainloop()

    def set_components(self):
        self.set_size_input()
        self.set_edges_input()
        self.set_mode_selection()
        self.set_checkboxes()
        self.start_button = Button(self.window, text="Load map", command=self.load_map)
        self.controls = Button(self.window, text="Controls", command=self.display_controls)
        self.start_button.place(x=20, y=165)
        self.controls.place(x=100, y=165)

    def display_controls(self):
        controls.ControlsWindow().run()

    def set_size_input(self):
        self.size_content = StringVar()
        self.size_label = Label(self.window, text="Map size (x,y)")
        self.size_input = Entry(self.window, width=10, textvariable=self.size_content)
        self.size_input.insert(END, "500,500")
        self.size_label.place(x=0, y=0)
        self.size_input.place(x=80,y=0)


    def set_edges_input(self):
        self.start_label = Label(self.window, text="Start (x,y)")
        self.start_input_content = StringVar()
        self.start_input = Entry(self.window, width=10, textvariable=self.start_input_content)
        self.start_label.place(x=0, y=25)
        self.start_input.place(x=60,y=25)

        self.end_label = Label(self.window, text="End (x,y)")
        self.end_input_content = StringVar()
        self.end_input = Entry(self.window, width=10, textvariable=self.end_input_content )
        self.end_label.place(x=0, y=50)
        self.end_input.place(x=60, y=50)

    def set_mode_selection(self):
        self.var = IntVar()
        self.mode_label = Label(self.window, text="Select mode:")
        self.block_mode = Radiobutton(self.window, text='Block', variable=self.var, value=0)
        self.route_mode = Radiobutton(self.window, text='Route', variable=self.var, value=1)
        self.mode_label.place(x=0, y=75)
        self.block_mode.place(x=0, y=95)
        self.route_mode.place(x=60, y=95)

    def set_checkboxes(self):
        self.show_route_checked = IntVar()
        self.show_time_checked = IntVar()
        self.show_route = Checkbutton(self.window, text='Show details', variable=self.show_route_checked)
        self.show_route.place(x=0,y=130)

    def load_map(self):
        self.settings.size = self.settings.string_to_pair(self.size_content.get())
        self.settings.start_point = self.settings.string_to_pair(self.start_input_content.get())
        self.settings.end_point = self.settings.string_to_pair(self.end_input_content.get())
        self.settings.mode = self.var.get()
        self.settings.show_details =  self.show_route_checked.get()

        self.window.destroy()