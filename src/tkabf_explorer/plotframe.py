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
        self.x = []
        self.y = []
        self.c = []
        # basic plot setup
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2,1])
        self.ax1 = self.figure.add_subplot(self.gs[0,0])
        self.ax2 = self.figure.add_subplot(self.gs[1,0])
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.plot()
    def plot(self):
        self.ax1.plot(self.x, self.y)
        self.ax2.plot(self.x, self.c)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1,
                                         padx=5, pady=5)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.BOTTOM,expand=1)
    def clear_plot(self):
        self.ax1.clear()
        self.ax2.clear()
