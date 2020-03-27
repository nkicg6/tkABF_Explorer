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
        self.geometry("950x800")
        self.large_font = ("Verdana", 14)
        self.medium_font = ("Verdana", 12)
        self.small_font = ("Verdana", 10)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        # parent frame
        container = tk.Frame(self)
        container.grid(row=0,column=0,sticky="nsew")
        container.grid_rowconfigure(0, weight=4)
        container.grid_rowconfigure(1, weight=1)
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
        self.plottable_items = ["Digital in", "Channel 2"]

        # events
        self.bind("<Tab>", self.outer_test_method)#control_frame.get_list_of_files_scrollbox_selection)
        self.bind("q", sys.exit)

    def outer_test_method(self, event):
        self.control_frame.get_list_of_files_scrollbox_selection(event)
        self.read_abf()

    def add_plottable(self):
        self.trace_frame.populate_plot_listboxes(self.plottable_items)

    def read_abf(self):
        try:
            abf = pyabf.ABF(self.control_frame.current_listbox_selected_path)
            self.plot_frame.x = abf.sweepX
            self.plot_frame.y = abf.sweepY
            self.plot_frame.c = abf.sweepC
            self.plot_frame.plot()
            self.parse_abf_set_vars()
            self.add_plottable()
        except Exception as e:
            print(f"Not a valid abf, exception: {e}")

    def parse_abf_set_vars(self):
        self.current_abf = pyabf.ABF(self.control_frame.current_listbox_selected_path)
        self.trace_frame.update_trace_name(self.current_abf.protocol)
        self.trace_frame.add_sweeps_to_listbox(self.current_abf.sweepList)
        print(self.trace_frame.protocol_name)


app = TkAbfExplorer()
app.mainloop()
print("Done")
