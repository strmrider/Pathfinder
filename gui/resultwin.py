from Tkinter import *

CONTINUE = 0
NEW_SETTINGS = 1
QUIT = 2

class ResultWindow:
    def __init__(self, path, time):
        self.window = Tk()
        self.window.geometry("270x140")
        self.path_len = "0"
        self.time = str(time)[:5]
        self.action=0
        if path:
            self.path_len = str(len(path))
            self.message = "Shortest path was found in " + self.time + " seconds\n and includes " + self.path_len +\
                           " blocks. You may continue\n with the current map, apply new settings\n or quit the program."
        else :
            self.message = "No path was found.\n Check if the given blocks/route are valid."
        self.result_message = Label(self.window, text=self.message)
        self.result_message.place(x=10, y=10)
        self.continue_button = Button(self.window, text="Continue", command= lambda: self.button_click(CONTINUE))
        self.new_map_button = Button(self.window, text="New settings", command= lambda: self.button_click(NEW_SETTINGS))
        self.quit_button = Button(self.window, text="Quit", command= lambda: self.button_click(QUIT))
        self.set_buttons()

    def set_buttons(self):
        self.continue_button.place(x=20,y=100)
        self.new_map_button.place(x=90, y=100)
        self.quit_button.place(x=190, y=100)

    def button_click(self, action):
        self.action = action
        self.window.destroy()

    def run(self):
        self.window.mainloop()
        return self.action