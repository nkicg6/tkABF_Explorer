import tkinter as tk
from tkinter import ttk

class TraceInfoFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller_ref = controller # expose parent for clear and plot buttons.
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=100)
        self.grid_columnconfigure(2, weight=100)
        self.grid_columnconfigure(3, weight=25)
        self.grid_columnconfigure(4, weight=50)
        # vars
        self.label_width = 10
        self.label_height = 10
        self.plot_mean_sweeps_option = tk.BooleanVar()
        self.plot_mean_sweeps_option.set(False)
        self.top_plot_canvas = tk.Canvas(self, bg="white", width=self.label_width,
                                         height=self.label_height)
        self.top_plot_canvas.create_text(8,25,angle=90, anchor="e",
                                         text="top",font=controller.medium_font)
        self.bottom_plot_canvas = tk.Canvas(self, bg="white", width=self.label_width,
                                            height=self.label_height)
        self.bottom_plot_canvas.create_text(8,12,angle=90, anchor="e",
                                         text="bottom",font=controller.medium_font)
        self.plot_options_frame = tk.Frame(self, bg="white")

        # TODO! add commands for these buttons
        self.plot_options_frame_mean_checkbox = tk.Checkbutton(self.plot_options_frame, text="Plot mean of sweeps?", width=20,
                                                               var=self.plot_mean_sweeps_option, onvalue=True, offvalue=False,
                                                               font=controller.large_font, command=self._toggle_mean, anchor="center")
        self.plot_options_frame_clear_plot_button = tk.Button(self.plot_options_frame, text="Clear plot\n('c')", width=20,
                                                              command=self.clear_plot, anchor="center", font=controller.large_font)
        self.plot_options_frame_update_plot_button = tk.Button(self.plot_options_frame, text="Update plot\n('tab')", width=20, height=4,
                                                               command=self.update_plot, anchor="center", font=controller.large_font)

        self.top_plot_listbox = tk.Listbox(self,width=5,height=3,
                                           font=controller.small_font,
                                           exportselection=False)
        self.bottom_plot_listbox = tk.Listbox(self,width=5,height=3,
                                              font=controller.small_font,
                                              exportselection=False)
        self.sweep_listbox = tk.Listbox(self, width=5,height=6,
                                        font=controller.large_font,
                                        exportselection=False)
        self.trace_vars_frame = tk.Frame(self, bg="white")

        self.trace_vars_frame_protocol_label = tk.Label(self.trace_vars_frame,
                                                        text="Protocol: ", width=20, height=1,
                                                        font=controller.large_font, anchor="e")
        self.trace_vars_frame_protocol_text = tk.Label(self.trace_vars_frame,
                                                        text="None selected", width=20,height=1,
                                                       font=controller.large_font, anchor="w")
        self.trace_vars_frame_file_label = tk.Label(self.trace_vars_frame,
                                                        text="File: ", width=20,height=1,
                                                        font=controller.large_font, anchor="e")
        self.trace_vars_frame_file_text = tk.Label(self.trace_vars_frame,
                                                        text="None selected", width=20,height=1,
                                                       font=controller.large_font, anchor="w")
        self.trace_vars_frame_sampling_rate_label = tk.Label(self.trace_vars_frame,
                                                        text="Sampling rate (kHz): ", width=20, height=1,
                                                             font=controller.large_font, anchor="e")
        self.trace_vars_frame_sampling_rate_text = tk.Label(self.trace_vars_frame,
                                                        text="None selected", width=20,height=1,
                                                            font=controller.large_font, anchor="w")

        # trace_vars_canvas setup
        self.trace_vars_frame.grid_columnconfigure(0,weight=1)
        self.trace_vars_frame.grid_rowconfigure(0,weight=1)
        self.trace_vars_frame.grid_columnconfigure(1,weight=1)
        self.trace_vars_frame.grid_rowconfigure(1,weight=1)
        self.trace_vars_frame.grid_rowconfigure(2,weight=1)
        self.trace_vars_frame.grid_rowconfigure(3,weight=1)
        self.plot_options_frame.grid_rowconfigure(0,weight=1)
        self.plot_options_frame.grid_rowconfigure(1,weight=1)
        self.plot_options_frame.grid_rowconfigure(1,weight=2)
        self.plot_options_frame.grid_columnconfigure(0,weight=1)

        # layout
        self.top_plot_canvas.grid(row=0,column=0, sticky="nsew")
        self.bottom_plot_canvas.grid(row=1,column=0, sticky="nsew")
        self.top_plot_listbox.grid(row=0,column=1, sticky="nsew")
        self.bottom_plot_listbox.grid(row=1,column=1, sticky="nsew")
        self.sweep_listbox.grid(column=2, row=0,rowspan=2, sticky="nsew")
        self.plot_options_frame.grid(column=3,row=0,rowspan=2, sticky="nsew")

        self.trace_vars_frame.grid(column=4,rowspan=2,row=0, sticky="nsew")

        self.trace_vars_frame_file_label.grid(column=0,row=0,sticky="w")
        self.trace_vars_frame_file_text.grid(column=1,row=0,sticky="ew")
        self.trace_vars_frame_protocol_label.grid(column=0,row=1,sticky="w")
        self.trace_vars_frame_protocol_text.grid(column=1,row=1,sticky="ew")

        self.trace_vars_frame_sampling_rate_label.grid(column=0,row=2,sticky="w")
        self.trace_vars_frame_sampling_rate_text.grid(column=1,row=2,sticky="ew")
        self.plot_options_frame_mean_checkbox.grid(column=0,row=0,sticky="nsew")
        self.plot_options_frame_clear_plot_button.grid(column=0,row=1, sticky="nsew")
        self.plot_options_frame_update_plot_button.grid(column=0,row=2, sticky="nsew")

    def clear_plot(self):
        print("clear plot pressed")
        print(f"val of parent testvar is {self.controller_ref.testvar}")

    def update_plot(self):
        print("update plot called")

    def _toggle_mean(self):
        print(f"the value of the toggle is {self.plot_mean_sweeps_option.get()}\n")

    def _populate_plot_listboxes(self, items):
        self.top_plot_listbox.delete(0,tk.END)
        self.top_plot_listbox.insert(tk.END, "\n")
        self.top_plot_listbox.insert(tk.END, "Choose what you want in the")
        self.top_plot_listbox.insert(tk.END, "small plot below")
        self.top_plot_listbox.insert(tk.END, "\n")
        self.bottom_plot_listbox.delete(0,tk.END)
        for item in items:
            self.bottom_plot_listbox.insert(tk.END, item)
        self.bottom_plot_listbox.selection_set(1)

    def _add_sweeps_to_listbox(self, sweeplist):
        self.sweep_listbox.delete(0,tk.END)
        for sweep in sorted(sweeplist):
            self.sweep_listbox.insert(tk.END, "Sweep: "+ str(sweep))
        self.sweep_listbox.selection_set(0)

    def _update_protocol_name(self, protocol_name):
        self.trace_vars_frame_protocol_text.config(text=protocol_name)

    def _update_file_name(self, file_name):
        self.trace_vars_frame_file_text.config(text=file_name)

    def _update_sampling_rate(self, sampling_rate):
        self.trace_vars_frame_sampling_rate_text.config(text=sampling_rate)

    def update_trace_info_frame(self, update_dict):
        self._update_protocol_name(update_dict['protocol_name'])
        self._update_file_name(update_dict['file_name'])
        self._update_sampling_rate(update_dict['sampling_rate'])
        self._add_sweeps_to_listbox(update_dict['sweepList'])
        self._populate_plot_listboxes(update_dict['plotable_items'])

    def _get_bottom_plot_listbox_selection(self):
        pass

    def _get_sweep_listbox_selection(self):
        pass

    def _get_plot_mean_sweeps_option_state(self):
        pass

    def get_plot_options(self):
        """composed function returns a map of options for master to plot"""
        plot_options = {}
        plot_options["bottom_plot"] = self._get_bottom_plot_listbox_selection()
        plot_options["sweep"] = self._get_sweep_listbox_selection()
        plot_options["plot_mean_state"] = self._get_plot_mean_sweeps_option_state()
        return plot_options

        pass
    def get_bottom_plot_selection(self):
        if not self.bottom_plot_listbox.curselection():
            print("get_bottom_plot_selection nothing selected")
            return None
        return self.bottom_plot_listbox.curselection()

    def get_sweep_selection(self):
        return self.sweep_listbox.curselection()
