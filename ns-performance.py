import sys
import os
import time
from open_bci_ganglion import OpenBCIBoard
import numpy as np
import seaborn as sns

from matplotlib import pyplot as plt

eeg = []

def handle(sample):
    eeg.append(sample.channel_data)

board = OpenBCIBoard()

board.start_streaming(handle, 10)

eeg = np.array(eeg)
time = np.linspace(0, 10, eeg[:,0].size)

plt.plot(time, eeg)

plt.show()