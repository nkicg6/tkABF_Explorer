import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import RectangleSelector
from matplotlib.figure import Figure
from matplotlib import gridspec

# connecting handlers to get current x and y lims: https://stackoverflow.com/a/31491515/6032156
# use span selector to get the ROI to analyze from plot https://matplotlib.org/3.2.0/gallery/widgets/span_selector.html#sphx-glr-gallery-widgets-span-selector-py
# https://dalelane.co.uk/blog/?p=778 need to work on toolbar.
# https://stackoverflow.com/questions/23172916/matplotlib-tkinter-customizing-toolbar-tooltips
class PlotFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,padx=5,pady=5)
        # vars
        self.current_plot_options = {"x":[], "y1":[], "x_label":"x",
                                     "y1_label":"y", "y2":[], "y2_label":"y",
                                     "fontsize":16, "sweep_label":[], "linewidth":4,
                                     "y2_color":"black"}
        self.instructions_label = tk.Label(self,font=controller.large_font, text="Click and drag on the top plot to zoom.")
        self.instructions_label.pack(side=tk.BOTTOM)
        self._legend = None
        self.xlims = None
        self.ylims = None
        # basic plot setup
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.gs = gridspec.GridSpec(nrows=2, ncols=1, height_ratios=[2,1])
        self.ax1 = self.figure.add_subplot(self.gs[0,0])
        self.ax1.spines['right'].set_visible(False)
        self.ax1.spines['top'].set_visible(False)
        self.ax2 = self.figure.add_subplot(self.gs[1,0], sharex=self.ax1)
        self.ax2.spines['right'].set_visible(False)
        self.ax2.spines['top'].set_visible(False)
        self.figcanvas = FigureCanvasTkAgg(self.figure, self)
        self.update_plot()

    def reset_axis(self):
        self.xlims = None
        self.ylims = None
        self.update_plot()

    def boxzoom(self, eclick, erelease):
        print('startposition: (%f, %f)' % (eclick.xdata, eclick.ydata))
        print('endposition  : (%f, %f)' % (erelease.xdata, erelease.ydata))
        x = sorted([eclick.xdata, erelease.xdata])
        y = sorted([eclick.ydata, erelease.ydata])
        self.xlims = x
        self.ylims = y
        self.ax1.set_xlim(self.xlims)
        self.ax1.set_ylim(self.ylims)

    def update_plot(self):
        if self._legend:
            self._legend.remove()
            self._legend = None
        self.ax1.cla()
        self.ax2.cla()
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
        self.figcanvas._tkcanvas.pack(expand=True,fill=tk.BOTH)
        if self.xlims and self.ylims is not None:
            self.ax1.set_xlim(self.xlims)
            self.ax1.set_ylim(self.ylims)
        self.figcanvas.draw()
        self.RS = RectangleSelector(self.ax1, self.boxzoom,
                                    drawtype='box')

    def clear_plot(self, event):
        print("clearing plot called")
        self.current_plot_options = {"x":[], "y1":[], "x_label":"x",
                                     "y1_label":"y", "y2":[], "y2_label":"y",
                                     "fontsize":16, "sweep_label":[], "linewidth":4,
                                     "y2_color":"black"}
        self.xlims = None
        self.ylims = None
        self.update_plot()
