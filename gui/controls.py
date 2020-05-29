from Tkinter import *

labels = ["Set start point - S + Mouse over",
          "Set end point -  E + Mouse over",
          "Set block/route -  Left click + mouse over",
          "Remove block/route: Right click + mouse over",
          "Clear map -  C",
          "Track path -  T",
          "Set new settings -  N",
          "Display instructions - I"
          ]


class ControlsWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x200")
        self.window.title("Controls")
        self.set_labels()
        self.close_button = Button(self.window, text="Close", command=self.close)
        self.close_button.pack()

    def run(self):
        self.window.mainloop()

    def set_labels(self):
        for index, label in enumerate(labels):
            Label(self.window, text=label).pack()

    def close(self):
        self.window.destroy()
        self.window.quit()
