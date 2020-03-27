import tkinter as tk
from tkinter import ttk

class TraceInfoFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="red")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        # vars
        self.file_name = ""
        self.current_sweep = ""
        self.current_channel = ""
