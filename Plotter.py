import matplotlib.pyplot as plt
import numpy as np


def toArray(dict):
    x = np.zeros(len(dict))
    y = np.zeros(len(dict))
    for i, date in enumerate(dict):
        x[i] = date
        y[i] = dict[date]
    plt.bar(x, y)
    plt.show()
    return x, y

#xpoints = np.array([0, 6])
#ypoints = np.array([100, 250])

#plt.bar(xpoints, ypoints)
#plt.show()
