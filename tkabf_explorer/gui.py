import sys
import tkinter as tk
from tkinter import ttk

import pyabf
import numpy as np

from controlframe import ControlFrame
from plotframe import PlotFrame
import plotting
from traceinfoframe import TraceInfoFrame

# TODO minimize state! State is most important for plotting, and it should ALL be contianed in one variable (a map) HERE. All other classes should be for layout and getters which are called from here to update the state model. Use Elm architechture as a guide.
# popup window plugin for analysis options https://blog.furas.pl/python-tkinter-how-to-create-popup-window-or-messagebox-gb.html

# TODO simplify api
# can you make a popup frame for analysis?
# TODO if one item in plottable list, select first. Otherwise, select the second by default
# always getting errors from plotting.py when plotting patch clamp files. why?


class TkAbfExplorer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "tkABF Viewer v0.1-dev")
        self.geometry("950x800")
        self.large_font = ("Verdana", 14)
        self.medium_font = ("Verdana", 12)
        self.small_font = ("Verdana", 10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # parent frame
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=4)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=3)
        # three main frames
        self.control_frame = ControlFrame(container, self)
        self.plot_frame = PlotFrame(container, self)
        self.trace_frame = TraceInfoFrame(container, self)
        # frame placement
        self.control_frame.grid(row=0, column=0, sticky="nsew")
        self.plot_frame.grid(row=0, column=1, sticky="ew")
        self.trace_frame.grid(row=1, columnspan=2, sticky="nsew")
        self.plotable_items = {"Command waveform": "c", "Channel 2": 1}
        self.path_current_selection = None
        self.short_name_current_selection = None

        ### events ###
        self.bind("<Tab>", self.update_plot_main)
        self.bind("c", self.plot_frame.clear_plot)
        self.control_frame.list_of_files_scrollbox.bind(
            "<<ListboxSelect>>", self.update_meta
        )
        self.bind("q", sys.exit)

    def show_error(self):
        tk.messagebox.showerror(
            "Plotting error",
            "Sorry, you tried to plot things with different axis lengths. Try clearing the plot (push 'c') and plot again.",
        )

    def _get_plottable_items(self, abf):
        if abf.channelCount == 1:
            return ["Command waveform"]
        if abf.channelCount == 2:
            return ["Command waveform", "Channel 2"]
        else:
            print(f"Only two channels supported, this file has: {abf.channelCount}")
            return []

    ### methods ###
    def _get_abf_selection(self):
        """sets path_current_selection and short_name_current_selection"""
        print(
            f"called from `_get_abf_selection` {self.control_frame.get_list_of_files_scrollbox_selection()}"
        )
        return self.control_frame.get_list_of_files_scrollbox_selection()

    def _make_metadata_dict(self):
        """creates dictionary of file metadata to populate gui frames"""
        curr_selection_full_path, curr_selection_short = self._get_abf_selection()
        print(
            f"returned by `self._get_abf_selection`: {curr_selection_short} and {curr_selection_full_path}"
        )
        abf = pyabf.ABF(curr_selection_full_path, loadData=False)
        self.current_meta_dict = {}
        self.current_meta_dict["protocol_name"] = abf.protocol
        self.current_meta_dict[
            "plot_mean_state"
        ] = self.trace_frame.plot_mean_sweeps_option.get()
        self.current_meta_dict[
            "sweep"
        ] = self.trace_frame._get_sweep_listbox_selection()
        self.current_meta_dict["file_name"] = curr_selection_short
        self.current_meta_dict["file_path"] = curr_selection_full_path
        self.current_meta_dict["sampling_rate"] = abf.dataPointsPerMs
        self.current_meta_dict["sweepList"] = abf.sweepList
        self.current_meta_dict[
            "bottom_plot"
        ] = self.trace_frame._get_bottom_plot_listbox_selection()
        self.current_meta_dict["plotable_items"] = self._get_plottable_items(
            abf
        )  # self.plotable_items.keys() #TODO get rid of hardcoded var here

    def update_meta(self, event):
        """create metadata and call update function in TraceInfoFrame"""
        self._make_metadata_dict()
        self.trace_frame.update_trace_info_frame(self.current_meta_dict)
        self.current_meta_dict = self.trace_frame.get_plot_options(
            self.current_meta_dict
        )
        print(f"event [{event}] triggered `update_meta` call")

    def _build_plot_map(self):
        try:
            updated_map = plotting.build_plot_map(
                self.current_meta_dict, self.plot_frame.current_plot_options
            )
            return updated_map
        except IndexError as e:
            self.show_error()
            return self.plot_frame.current_plot_options

    def update_plot_options(self):
        self.plot_frame.current_plot_options = _build_plot_map(self)

    def update_plot_main(self, event):
        self._make_metadata_dict()
        if self.current_meta_dict["file_path"] is not None:
            self._build_plot_map()
            self.plot_frame.update_plot()
        else:
            print("Nothing selected, error")
            print(f"self.current_meta_dict is: {self.current_meta_dict}")


app = TkAbfExplorer()
app.mainloop()
print("Done")
