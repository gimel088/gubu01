import os
import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import pygubu


class Plot02App:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        uifile = os.path.join(os.path.dirname(__file__),"plot02.ui")
        builder.add_from_file(uifile)

        self.mainwindow = builder.get_object('mainwindow')
        
        # Container for the matplotlib canvas and toolbar classes
        fcontainer = builder.get_object('fcontainer')
        
        # Setup matplotlib canvas
        self.figure = fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = canvas = FigureCanvasTkAgg(fig, master=fcontainer)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Setup matplotlib toolbar (optional)
        self.toolbar = NavigationToolbar2Tk(canvas, fcontainer)
        self.toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Connect button callback
        builder.connect_callbacks(self)
        self.tk_ent_1 = self.builder.get_object('ent_1')
        self.tk_label_1 = self.builder.get_object('Label_1')

    def run(self):
        self.mainwindow.mainloop()
        
    def on_plot_clicked(self):
        v1 = self.tk_ent_1.get()
        print('ent_1=', v1)
        echo_label = self.builder.get_variable('ent_1')
        echo_label.set(v1)

        self.tk_label_1.config(text="config text")
        e2 = self.builder.get_object('ent_2')
        e2.config(text=v1)
        self.mainwindow.update()
        a = self.figure.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.canvas.draw()

    def on_quit_clicked(self):
         self.mainwindow.destroy()
         #self.mainwindow.quit()

def main():
    #if __name__ == '__main__':
    app = Plot02App()
    app.run()
