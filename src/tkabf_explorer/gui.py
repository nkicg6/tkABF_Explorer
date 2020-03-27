import tkinter as tk
from tkinter import ttk
import sys
from controlframe import ControlFrame
from plotframe import PlotFrame
from traceinfoframe import TraceInfoFrame
import pyabf

class TkAbfExplorer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"tkABF Viewer v0.1-dev")
        self.geometry("900x800")
        self.large_font = ("Verdana", 14)
        self.small_font = ("Verdana", 10)
        # parent frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=3)
        container.grid_rowconfigure(1, weight=2)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)
        # three main frames
        self.control_frame = ControlFrame(container, self)
        self.plot_frame = PlotFrame(container, self)
        self.trace_frame = TraceInfoFrame(container, self)
        # frame placement
        self.control_frame.grid(row=0,column=0, sticky="nsew")
        self.plot_frame.grid(row=0,column=1, sticky="nsew")
        self.trace_frame.grid(row=1,columnspan=2, sticky="nsew")
        # events
        self.bind("<Tab>", self.outer_test_method)#control_frame.get_list_of_files_scrollbox_selection)
        self.bind("q", sys.exit)
    def outer_test_method(self, event):
        self.control_frame.get_list_of_files_scrollbox_selection(event)
        print(f"current selected path is {self.control_frame.current_listbox_selected_path}")
        print(f"current short name is {self.control_frame.current_listbox_selected_path_short_name}")
        self.read_abf()
        #print(f"from parent, vars are: {container.current_listbox_selected_path}\n{container.current_listbox_selected_path_short_name}")
    def read_abf(self):
        try:
            abf = pyabf.ABF(self.control_frame.current_listbox_selected_path)
            self.plot_frame.x = abf.sweepX
            self.plot_frame.y = abf.sweepY
            self.plot_frame.c = abf.sweepC
            self.plot_frame.plot()
        except Exception as e:
            print(f"Not a valid abf, exception: {e}")


app = TkAbfExplorer()
app.mainloop()
print("Done")
