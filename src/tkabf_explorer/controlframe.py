import os
import tkinter as tk
from tkinter import ttk

class ControlFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        # frame button/info layout
        self.grid_rowconfigure(0, weight=1) # choose dir button
        self.grid_rowconfigure(1, weight=1) # dir display
        self.grid_rowconfigure(2, weight=3) # other options
        self.grid_rowconfigure(3, weight=1) # other options
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1,weight=2)
        self.label = ttk.Label(self, text="test option")
        self.current_dir_label = ttk.Label(self, text="current dir",
                                           font = controller.large_font)
        self.choose_dir_button = ttk.Button(self, text="Choose a directory",
                                            command=self.open_dir)
        # setup scrollbox for files
        self.list_of_files_scrollbox = tk.Listbox(self)
        self.list_of_files_scrollbox.insert(0,"No abf files found")
        self.list_of_files_scrollbar = tk.Scrollbar(self, orient="vertical")
        self.list_of_files_scrollbar.config(command=self.list_of_files_scrollbox.yview)
        self.list_of_files_scrollbox.config(yscrollcommand=self.list_of_files_scrollbar.set)

        self.entry_text = ttk.Entry(self)
        # layout

        self.list_of_files_scrollbar.grid(row=2,column=1,sticky="ns")
        self.list_of_files_scrollbox.grid(row=2,column=0, sticky="ns",padx=5)
        self.label.grid(row=3, column=2)
        self.choose_dir_button.grid(row=0)
        self.current_dir_label.grid(row=1, sticky="nsew", padx=5)
        self.entry_text.grid(row=3)

    def on_button(self, event):
        gotvar = self.entry_text.get()
        self.label.config(text=gotvar)

    def add_files_to_listbox(self):
        self.list_of_files_scrollbox.delete(0,tk.END)
        keys_sorted = sorted([k for k in self.abf_list_dict.keys()])
        for abf_file in keys_sorted:
            self.list_of_files_scrollbox.insert(tk.END, abf_file)

    def set_listbox_empty(self):
        self.list_of_files_scrollbox.delete(0,tk.END)
        self.list_of_files_scrollbox.insert(0, "No abf files found")
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
