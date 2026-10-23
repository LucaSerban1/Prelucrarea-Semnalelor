import numpy as np
import matplotlib.pyplot as plt

fs = 1000

t = np.linspace(0, 1, fs)

#semnal = np.sin(2 * np.pi * fs * t)
semnal_a = np.sin(2 * np.pi * fs/2 * t)
semnal_b = np.sin(2 * np.pi * fs/4 * t)
semnal_c = np.sin(2 * np.pi * 0 * t)
#semnal_d = semnal_a + semnal_b + semnal_c

fig, axs1 = plt.subplots(3)

#fig2, axs2 = plt.subplots(2)

axs1[0].plot(t, semnal_a)
axs1[1].plot(t, semnal_b)
axs1[2].plot(t, semnal_c)

#axs2[0].plot(t, semnal)
#axs2[1].plot(t, semnal_d)

fig.savefig(fname='./plots/Semnal fundamental.pdf', format = 'pdf')
plt.show()

