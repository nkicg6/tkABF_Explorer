import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
import pyabf

class PlotFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Main plot", font=controller.large_font)
        self.label.pack(pady=10, padx=10)
        self.x = []
        self.y = []
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.ax1 = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.plot()
    def plot(self):
        self.ax1.clear()
        self.ax1.plot(self.x, self.y)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.toolbar.update()
        self.canvas._tkcanvas.pack()
