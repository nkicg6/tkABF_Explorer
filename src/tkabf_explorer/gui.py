import os
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
        self.geometry("800x600")
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


class ControlFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        # frame button/info layout
        self.grid_rowconfigure(0, weight=1) # choose dir button
        self.grid_rowconfigure(1, weight=2) # dir display
        self.grid_rowconfigure(2, weight=1) # other options
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1,weight=2)
        self.label = ttk.Label(self, text="test option", font = LARGE_FONT)
        self.main_dir_button = ttk.Button(self, text="Choose a directory",
                                          command=self.open_dir)
        # setup scrollbox for files
        self.list_of_files = tk.Listbox(self)
        self.list_of_files.insert(0,"No abf files found")
        self.scrollbar = tk.Scrollbar(self, orient="vertical")
        self.scrollbar.config(command=self.list_of_files.yview)
        self.list_of_files.config(yscrollcommand=self.scrollbar.set)
        self.entry_text = ttk.Entry(self)
        # layout
        self.scrollbar.grid(row=1,column=1,sticky="ns")
        self.list_of_files.grid(row=1,column=0, sticky="ns",padx=5)
        self.label.grid(row=2, column=2)
        self.main_dir_button.grid(row=0)
        self.entry_text.grid(row=2)

    def on_button(self, event):
        gotvar = self.entry_text.get()
        self.label.config(text=gotvar)

    def add_files_to_listbox(self):
        self.list_of_files.delete(0,tk.END)
        keys_sorted = sorted([k for k in self.abf_list_dict.keys()])
        for abf_file in keys_sorted:
            self.list_of_files.insert(tk.END, abf_file)

    def set_listbox_empty(self):
        self.list_of_files.delete(0,tk.END)
        self.list_of_files.insert(0, "No abf files found")
        self.abf_list_dict = {}

    def list_abfs(self):
        abf_list = [i for i in os.listdir(self.working_dir) if i.endswith(".abf")]
        self.abf_list_dict = {}
        for item in abf_list:
            self.abf_list_dict[item] = os.path.join(self.working_dir,item)
        if len(abf_list) ==0:
            self.set_listbox_empty()
        else:
            self.add_files_to_listbox()

    def open_dir(self):
        self.working_dir = tk.filedialog.askdirectory()
        self.list_abfs()


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
