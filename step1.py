"""
===========
Simple Step Plot
===========

Create a simple step plot.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def step3(x):
    if x<0.3:
        return 0.0
    else:
        return 1.0

def simple1():
    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    #s = 1 + np.sin(2 * np.pi * t)
    s =  np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)
    ax.plot(t, 0.2 *t)
    #
    #plt.plot(range(5), range(5), linestyle='--', drawstyle='steps')
    plt.plot([0,0.06,0.22,0.55,0.7,1.0], [-1,-1,1,-1,1,-1], linestyle='--', drawstyle='steps')

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    #fig.savefig("test.png")
    plt.show()
    return fig

    #############################################################################
    #
    # ------------
    #
    # References
    # """"""""""
    #
    # The use of the following functions and methods is shown in this example:

#matplotlib.axes.Axes.plot
#matplotlib.pyplot.plot
#matplotlib.pyplot.subplots
#matplotlib.figure.Figure.savefig
