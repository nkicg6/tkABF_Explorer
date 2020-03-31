import os
import tkinter as tk
from tkinter import ttk
DEBUG_DIR = "/Users/nick/Dropbox/lab_notebook/projects_and_data/mnc/analysis_and_data/extracellular_lfp/data/"

class ControlFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        # frame button/info layout
        self.grid_rowconfigure(0, weight=1) # choose dir button
        self.grid_rowconfigure(1, weight=1) # dir display
        self.grid_rowconfigure(2, weight=8) # other options
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1,weight=2)
        # vars
        self.starting_dir_for_selection = DEBUG_DIR#os.path.expanduser("~")
        self.current_dir_listbox = tk.Listbox(self, font = controller.small_font,
                                              width=25, height=1, bd=0,relief="flat")
        self.choose_dir_button = ttk.Button(self, text="Choose a directory",
                                            command=self.open_dir)
        self.abf_path_dict = {}
        # setup scrollbox for files
        self.list_of_files_scrollbox = tk.Listbox(self,width=25,height=25,
                                                  font=controller.large_font,
                                                  exportselection=False) #, selectmode=tk.MULTIPLE) # for future implementation
        self.list_of_files_scrollbox.insert(0,"No abf files found")
        self.list_of_files_scrollbar = tk.Scrollbar(self, orient="vertical")
        self.list_of_files_scrollbar.config(command=self.list_of_files_scrollbox.yview)
        self.list_of_files_scrollbox.config(yscrollcommand=self.list_of_files_scrollbar.set)
        # layout
        self.list_of_files_scrollbar.grid(row=2,column=1,sticky="ens")
        self.list_of_files_scrollbox.grid(row=2,column=0, sticky="ns",padx=5,pady=5)
        self.choose_dir_button.grid(row=0)
        self.current_dir_listbox.grid(row=1, sticky="ew", padx=5,pady=1)

    def get_list_of_files_scrollbox_selection(self):
        ind = self.list_of_files_scrollbox.curselection()
        sel = self.list_of_files_scrollbox.get(ind)
        try:
            print(f"abf path dict: {self.abf_path_dict}")
            return self.abf_path_dict[sel], sel
        except:
            print("couldn't find it")

    def add_files_to_listbox(self):
        self.list_of_files_scrollbox.delete(0,tk.END)
        keys_sorted = sorted([k for k in self.abf_path_dict.keys()])
        for abf_file in keys_sorted:
            self.list_of_files_scrollbox.insert(tk.END, abf_file)
        self.list_of_files_scrollbox.selection_set(0)

    def set_listbox_empty(self):
        self.list_of_files_scrollbox.delete(0,tk.END)
        self.list_of_files_scrollbox.insert(0, "No abf files found")
        self.abf_path_dict = {}

    def list_abfs(self):
        abf_list = [i for i in os.listdir(self.working_dir) if i.endswith(".abf")]
        for item in abf_list:
            self.abf_path_dict[item] = os.path.join(self.working_dir,item)
        if len(abf_list) ==0:
            self.set_listbox_empty()
        else:
            self.add_files_to_listbox()

    def set_choose_dir_listbox(self):
        self.current_dir_listbox.delete(0,tk.END)
        self.current_dir_listbox.insert(tk.END, self.working_dir)
        self.starting_dir_for_selection = self.working_dir

    def open_dir(self):
        if os.path.exists(self.starting_dir_for_selection):
            starting_dir = self.starting_dir_for_selection
        else:
            starting_dir = os.path.expanduser("~")
        self.working_dir = tk.filedialog.askdirectory(initialdir=starting_dir)
        self.list_abfs()
        self.set_choose_dir_listbox()
