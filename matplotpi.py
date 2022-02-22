# matvis.py
# Uses matplot to draw stuff from the digits of PI
# this took way to long 😩 (first time using matplot)

import matplotlib.pyplot as plt
import matplotlib.colors as cl
import numpy as np


def main():
    SIZE = 300
    plt.style.use('_mpl-gallery')
    lotsofpi = open('10Kpi.txt').read()

    fig, ax = plt.subplots()
    x, y, z = [], [], []
    for i in range(SIZE**2):
        if lotsofpi[i] == lotsofpi[i+1]:
            n = int(lotsofpi[i])
            x += i % SIZE, i % SIZE + 1
            y += i // SIZE, i // SIZE
            z += n, n

    ax.scatter(x, y, s=5, c=z, cmap='hsv', alpha=1, edgecolor=None)

    ax.set(xlim=(0, SIZE), ylim=(0, SIZE))
    plt.show()


if __name__ == '__main__':
    main()
