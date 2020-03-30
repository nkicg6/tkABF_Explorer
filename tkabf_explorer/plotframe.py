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
        self._default_plot_map = {"x":[], "y1":[[]], "x_label":"x", "y1_label":"y", "y2":[[]], "y2_label":"y",
                                     "fontsize":16, "sweep_label":[[]], "linewidth":4, "y2_color":"black"}
        self.current_plot_options = {}
        self._legend_list = []
        # basic plot setup
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2,1])
        self.ax1 = self.figure.add_subplot(self.gs[0,0])
        self.ax2 = self.figure.add_subplot(self.gs[1,0], sharex=self.ax1)
        self.figcanvas = FigureCanvasTkAgg(self.figure, self)
        self.toolbar = NavigationToolbar2Tk(self.figcanvas, self)
        self.toolbar.update()
        self.update_plot()

    def update_plot(self, plot_map=None):
        if plot_map == None:
            print("`update_plot` called with None")
            plot_map = self._default_plot_map
        self.ax1.plot(plot_map['x'], plot_map['y1'],
                      label=plot_map['sweep_label'],
                      lw=plot_map['linewidth'])
        self.ax1.set_ylabel(plot_map['y1_label'])
        self.ax2.plot(plot_map['x'], plot_map['y2'],
                      color=plot_map["y2_color"])
        self.ax2.set_ylabel(plot_map['y2_label'])
        self.ax2.set_xlabel(plot_map['x_label'])
        self._legend_list.append(self.figure.legend())
        self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1,padx=5,pady=5)
        self.figcanvas.draw()

    def clear_plot(self, event):
        print("clearing plot called")
        for i in self._legend_list:
            i.remove()
        self._legend_list = []
        self.ax1.clear()
        self.ax2.clear()
        self.update_plot(plot_map=None)
        self.toolbar.update()
        #self.figure.legend()
        #self.figcanvas.draw()
        #self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        #self.toolbar.update()
        #self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1)
