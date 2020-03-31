import tkinter as tk
from tkinter import ttk
import sys
from controlframe import ControlFrame
from plotframe import PlotFrame
from traceinfoframe import TraceInfoFrame
import pyabf
import numpy as np

import plotting

# TODO handle case when there is not a channel 1. (patch recordings)
# TODO add default viewport options
# TODO prettier/better plot formatting

class TkAbfExplorer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,"tkABF Viewer v0.1-dev")
        self.geometry("950x800")
        self.testvar = "I am a parent test var"
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
        self.plotable_items = {"Command waveform":"c", "Channel 2":1}
        self.path_current_selection = None
        self.short_name_current_selection = None

        ### events ###
        self.bind("<Tab>", self.update_plot)
        self.bind("c", self.plot_frame.clear_plot)
        self.control_frame.list_of_files_scrollbox.bind('<<ListboxSelect>>',
                                                        self.update_meta)
        self.bind("q", sys.exit)

     ### methods ###
    def _get_abf_selection(self):
        """sets path_current_selection and short_name_current_selection"""
        return self.control_frame.get_list_of_files_scrollbox_selection()

    def _make_metadata_dict(self):
        """creates dictionary of file metadata to populate gui frames"""
        curr_selection_short, curr_selection_full_path = self._get_abf_selection()
        abf = pyabf.ABF(curr_selection_full_path, loadData=False)
        self.current_meta_dict = {}
        self.current_meta_dict['protocol_name'] = abf.protocol
        self.current_meta_dict['file_name'] = curr_selection_short
        self.current_meta_dict['file_path'] = curr_selection_full_path
        self.current_meta_dict['sampling_rate'] = abf.dataPointsPerMs
        self.current_meta_dict['sweepList'] = abf.sweepList
        self.current_meta_dict['plotable_items'] = self.plotable_items.keys() #TODO get rid of hardcoded var here

    def update_meta(self, event):
        """create metadata and call update function in TraceInfoFrame"""
        self._make_metadata_dict()
        self.trace_frame.update_trace_info_frame(self.current_meta_dict)
        self.current_meta_dict = self.trace_frame.get_plot_options(self.current_meta_dict)
        print(f"event [{event}] triggered `update_meta` call")

    def _build_plot_map(self):
        return plotting.build_plot_map(self.current_meta_dict, self.plot_frame.current_plot_options)

    def update_plot_options(self):
        self.plot_frame.current_plot_options = _build_plot_map(self)

    def update_plot(self, event):
        if self.path_current_selection is not None:
            self.update_meta("")
            self._build_plot_map()
            self.plot_frame.update_plot()
        else:
            print("Nothing selected, error")


app = TkAbfExplorer()
app.mainloop()
print("Done")
