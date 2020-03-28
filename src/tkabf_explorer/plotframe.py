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
        self.topy_label = "y"
        self.legend_list = []
        self.x_label = "x"
        self.sweep_label = ""
        self.top_plot_label = ""
        self.smallplot_y_label = ""
        self.x = []
        self.y = []
        self.smallplot_y = []
        # basic plot setup
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2,1])
        self.ax1 = self.figure.add_subplot(self.gs[0,0])
        self.ax2 = self.figure.add_subplot(self.gs[1,0], sharex=self.ax1)
        self.figcanvas = FigureCanvasTkAgg(self.figure, self)
        #self.canvas.grid(column=0,row=0,sticky="nsew")
        self.toolbar = NavigationToolbar2Tk(self.figcanvas, self)
        self.update_plot()

    def update_plot(self):
        self.figure.suptitle(self.top_plot_label, fontsize=16)
        self.ax1.plot(self.x, self.y, label=self.sweep_label)
        self.ax1.set_ylabel(self.topy_label)
        self.ax2.plot(self.x, self.smallplot_y, color="black")
        self.ax2.set_ylabel(self.smallplot_y_label)
        self.ax2.set_xlabel(self.x_label)
        self.legend_list.append(self.figure.legend())
        self.figcanvas.draw()
        self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        self.toolbar.update()
        self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1)

    def clear_plot(self, event):
        print("clearing plot called")
        for i in self.legend_list:
            i.remove()
        self.legend_list = []
        self.ax1.clear()
        self.ax2.clear()
        self.figure.legend()
        self.figcanvas.draw()
        self.figcanvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,padx=5, pady=5)
        self.toolbar.update()
        self.figcanvas._tkcanvas.pack(side=tk.BOTTOM,expand=1)
