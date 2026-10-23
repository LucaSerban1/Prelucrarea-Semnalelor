import numpy as np
import matplotlib.pyplot as plt

fs = 1000

t = np.linspace(0, 1, fs)

semnal = np.sin(2 * np.pi * 200 * t)
semnal_2 = semnal[::4]
semnal_3 = semnal[1::4]

fig, axs1 = plt.subplots(3)

for ax in axs1.flat:
    ax.set_xlim([0, 0.1])

axs1[0].plot(t, semnal)
axs1[1].plot(t[::4], semnal_2) 
axs1[2].plot(t[1::4], semnal_3)

fig.savefig(fname='./plots/Semnal decimat.pdf', format = 'pdf')
plt.show()