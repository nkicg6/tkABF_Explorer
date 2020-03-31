import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import gridspec

class PlotFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)
        # vars
        # __default_plot_map is never edited.
        self._default_plot_options = {"x":[], "y1":[], "x_label":"x", "y1_label":"y", "y2":[], "y2_label":"y",
                                  "fontsize":16, "sweep_label":[], "linewidth":4, "y2_color":"black"}
        self.current_plot_options = {"x":[], "y1":[], "x_label":"x", "y1_label":"y", "y2":[], "y2_label":"y",
                                  "fontsize":16, "sweep_label":[], "linewidth":4, "y2_color":"black"}
        self._legend = None
        # basic plot setup
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2,1])
        self.ax1 = self.figure.add_subplot(self.gs[0,0])
        self.ax2 = self.figure.add_subplot(self.gs[1,0], sharex=self.ax1)
        self.figcanvas = FigureCanvasTkAgg(self.figure, self)
        self.toolbar = NavigationToolbar2Tk(self.figcanvas, self)
        self.toolbar.update()
        self.update_plot()

    def update_plot(self):
        if self._legend:
            self._legend.remove()
            self._legend = None
        print(f"current_plot_options is {self.current_plot_options}")
        self.ax1.cla()
        self.ax2.cla()
        #self.ax1.get_legend().remove()
        for y1,y2,sweep_label in zip(self.current_plot_options['y1'], self.current_plot_options['y2'], self.current_plot_options['sweep_label']):
            self.ax1.plot(self.current_plot_options['x'], y1, label=sweep_label,
                          lw=self.current_plot_options['linewidth'])
            self.ax2.plot(self.current_plot_options['x'], y2, color=self.current_plot_options['y2_color'],
                          lw=self.current_plot_options['linewidth'])
        self.ax1.set_ylabel(self.current_plot_options['y1_label'])
        self.ax2.set_ylabel(self.current_plot_options['y2_label'])
        self.ax2.set_xlabel(self.current_plot_options['x_label'])
        self._legend = self.figure.legend()
        self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1,padx=5,pady=5)
        self.figcanvas.draw()
        self.toolbar.update()

    def clear_plot(self, event):
        print("clearing plot called")
        self.current_plot_options = {"x":[], "y1":[], "x_label":"x", "y1_label":"y", "y2":[], "y2_label":"y",
                                  "fontsize":16, "sweep_label":[], "linewidth":4, "y2_color":"black"}
        print(f"current_plot_options is {self.current_plot_options}")
        self.update_plot()
        #self.figure.legend()
        #self.figcanvas.draw()
        #self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        #self.toolbar.update()
        #self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1)
