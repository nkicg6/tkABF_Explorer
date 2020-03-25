import tkinter as tk
from tkinter import ttk

from controlframe import ControlFrame
from plotframe import PlotFrame


class TkAbfExplorer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"tkABF Viewer v0.1-dev")
        self.geometry("800x600")
        self.large_font = ("Verdana", 14)
        # parent frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)
        # class vars
        container.example = "container example"
        # two main frames
        control_frame = ControlFrame(container, self)
        plot_frame = PlotFrame(container, self)
        # frame placement
        control_frame.grid(row=0,column=0, sticky="nsew")
        plot_frame.grid(row=0,column=1, sticky="nsew")
        # events
        self.bind("<Tab>", control_frame.on_button)
    def print_v(self, event):
        print(f"pressed ")

app = TkAbfExplorer()
app.mainloop()
print("Done")
