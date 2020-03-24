import sys
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
# Implement the default Matplotlib key bindings.
#from matplotlib.backend_bases import key_press_handler

#import numpy as np
LARGE_FONT = ("Verdana", 12)

class TkAbfExplorer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"tkABF Viewer v0.1-dev")
        container = tk.Frame(self, bg="blue")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)
        container.example = "container example"
        control_frame = ControlFrame(container, self)
        plot_frame = PlotFrame(container, self)
        control_frame.grid(row=0,column=0, sticky="nsew")
        plot_frame.grid(row=0,column=1, sticky="nsew")


class ControlFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='red')
        label = tk.Label(self, text="controls", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        # in our case, container is "parent" and can be accessed like so:
        print(parent.example)


class PlotFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main plot", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #toolbar = NavigationToolbar2Tk(canvas, self)
        #toolbar.update()
        canvas._tkcanvas.pack()


app = TkAbfExplorer()
app.mainloop()
print("Done")
