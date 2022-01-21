import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib import pylab


def plotNormal(x, y):
    """
    Plots the Data
    :param x:
    :param y:
    :return:
    """
    plt.bar(x, y)
    plt.show()


def plotTrendLine(x, y):
    """
    Plots the Data with a Trend Line
    :param x:
    :param y:
    :return:
    """
    pylab.bar(x, y)
    x = mdates.date2num(x)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    pylab.plot(x, p(x), "r--")
    plt.show()

