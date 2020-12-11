import numpy as np
from tkinter import filedialog
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf

# Read a wav file and draw waveform
file_name = filedialog.askopenfilename()
rate, data = wf.read(file_name)

# Timing Axe
Time = np.linspace(0, 1000 * len(data) / rate, num=len(data))
plt.xlim(Time[0], Time[-1])
plt.ylim(np.min(data), np.max(data))
plt.fill_between(Time, np.min(data), np.max(data), color='k')
plt.plot(Time, data, color='#00E100')
plt.grid(color='w')
plt.xlabel('Time in ms')
plt.ylabel(u'Biên độ')
plt.title(file_name)
plt.show()
