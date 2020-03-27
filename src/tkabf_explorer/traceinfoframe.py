import tkinter as tk
from tkinter import ttk

class TraceInfoFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=100)
        self.grid_columnconfigure(2, weight=100)
        self.grid_columnconfigure(3, weight=50)
        self.grid_columnconfigure(4, weight=25)
        # vars
        self.file_name = "none selected"
        self.protocol_name = "none selected"
        self.current_sweep = tk.IntVar()
        self.current_channel = tk.IntVar()
        self.label_width = 10
        self.label_height = 10
        self.top_plot_canvas = tk.Canvas(self, bg="white", width=self.label_width,
                                         height=self.label_height)
        self.top_plot_canvas.create_text(8,25,angle=90, anchor="e",
                                         text="top",font=controller.medium_font)
        self.bottom_plot_canvas = tk.Canvas(self, bg="white", width=self.label_width,
                                            height=self.label_height)
        self.bottom_plot_canvas.create_text(8,12,angle=90, anchor="e",
                                         text="bottom",font=controller.medium_font)
        self.plot_options_frame = tk.Frame(self, bg="yellow")
        self.top_plot_listbox = tk.Listbox(self,width=5,height=3,
                                           font=controller.small_font,
                                           exportselection=False)
        self.bottom_plot_listbox = tk.Listbox(self,width=5,height=3,
                                              font=controller.small_font,
                                              exportselection=False)
        self.sweep_listbox = tk.Listbox(self, width=5,height=6,
                                        font=controller.large_font,
                                        exportselection=False)
        self.trace_vars_frame = tk.Frame(self, bg="green")

        self.trace_vars_frame_protocol_label = tk.Label(self.trace_vars_frame,
                                                        text="Protocol: ", width=12,height=1, font=controller.large_font)
        self.trace_vars_frame_protocol_text = tk.Label(self.trace_vars_frame,
                                                        text=self.protocol_name, width=25,height=1, font=controller.large_font)
        # trace_vars_canvas setup
        self.trace_vars_frame.grid_columnconfigure(0,weight=1)
        self.trace_vars_frame.grid_rowconfigure(0,weight=1)
        self.trace_vars_frame.grid_columnconfigure(1,weight=1)
        self.trace_vars_frame.grid_rowconfigure(1,weight=1)
        self.trace_vars_frame.grid_rowconfigure(2,weight=1)
        self.trace_vars_frame.grid_rowconfigure(3,weight=1)

        # layout
        self.top_plot_canvas.grid(row=0,column=0, sticky="nsew")
        self.bottom_plot_canvas.grid(row=1,column=0, sticky="nsew")
        self.top_plot_listbox.grid(row=0,column=1, sticky="nsew")
        self.bottom_plot_listbox.grid(row=1,column=1, sticky="nsew")
        self.sweep_listbox.grid(column=2, row=0,rowspan=2, sticky="nsew")
        self.plot_options_frame.grid(column=3,row=0,rowspan=2, sticky="nsew")

        self.trace_vars_frame.grid(column=4,rowspan=2,row=0, sticky="nsew")
        self.trace_vars_frame_protocol_label.grid(column=0,row=0,sticky="w")
        self.trace_vars_frame_protocol_text.grid(column=1,row=0,sticky="ew")

    def populate_plot_listboxes(self, items):
        self.top_plot_listbox.delete(0,tk.END)
        self.top_plot_listbox.insert(tk.END, "\n")
        self.top_plot_listbox.insert(tk.END, "Choose what you want in the small plot below")
        self.top_plot_listbox.insert(tk.END, "\n")
        self.bottom_plot_listbox.delete(0,tk.END)
        for item in items:
            self.bottom_plot_listbox.insert(tk.END, item)
        self.bottom_plot_listbox.selection_set(1)

    def add_sweeps_to_listbox(self, sweeplist):
        self.sweep_listbox.delete(0,tk.END)
        for sweep in sweeplist:
            self.sweep_listbox.insert(tk.END, "Sweep: "+ str(sweep))
        self.sweep_listbox.selection_set(0)

    def update_trace_name(self, trace_name):
        self.protocol_name = trace_name
        self.trace_vars_frame_protocol_text.config(text=trace_name)
