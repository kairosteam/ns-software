import sys
import os
import time
from open_bci_ganglion import OpenBCIBoard
import numpy as np
import seaborn as sns

eeg = []

def handle_sample(sample):
    eeg.append(sample.channel_data)

#Establish connection with the board
board = OpenBCIBoard()

#Stream data for 10 seconds
board.start_streaming(handle_sample, 10)

eeg = np.array(eeg)
time = np.linspace(0, 10, eeg[:,0].size)
sns.plt.plot(time, eeg[:,0], color=(0.3, 0.3, 0.3))
sns.plt.xlabel('Time')
sns.plt.ylabel('Voltage')
sns.plt.show()
