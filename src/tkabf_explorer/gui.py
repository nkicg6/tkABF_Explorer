import tkinter as tk
from tkinter import ttk
import sys
from controlframe import ControlFrame
from plotframe import PlotFrame
from traceinfoframe import TraceInfoFrame
import pyabf

# get all input for plotting, trigger with tab

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
        self.plotable_items = ["Command waveform", "Channel 2"]

        ### events ###
        #self.bind("<Tab>", self.update_meta)#control_frame.get_list_of_files_scrollbox_selection)
        self.control_frame.list_of_files_scrollbox.bind('<<ListboxSelect>>',
                                                        self.update_meta)
        self.bind("q", sys.exit)

     ### methods ###
    def _get_abf_selection(self, event):
        """sets path_current_selection and short_name_current_selection"""
        self.path_current_selection, self.short_name_current_selection = self.control_frame.get_list_of_files_scrollbox_selection(event)

    def _make_metadata_dict(self):
        """creates dictionary of file metadata to populate gui frames"""
        abf = pyabf.ABF(self.path_current_selection, loadData=False)
        self.current_meta_dict = {}
        self.current_meta_dict['protocol_name'] = abf.protocol
        self.current_meta_dict['file_name'] = self.short_name_current_selection
        self.current_meta_dict['sampling_rate'] = abf.dataPointsPerMs
        self.current_meta_dict['sweepList'] = abf.sweepList
        self.current_meta_dict['plotable_items'] = self.plotable_items

    def update_meta(self, event):
        """create metadata and call update function in TraceInfoFrame"""
        self._get_abf_selection(event)
        self._make_metadata_dict()
        self.trace_frame.update_trace_info_frame(self.current_meta_dict)
        print(f"update meta called with event {event}")


app = TkAbfExplorer()
app.mainloop()
print("Done")
