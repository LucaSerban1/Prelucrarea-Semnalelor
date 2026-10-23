import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 250)
semnal_sin = np.sin(2 * np.pi * 240 * t)

semnal_sawthooth = np.mod(240 * t, 1)

fig, axs1 = plt.subplots(3)
axs1[0].plot(t, semnal_sin)
axs1[0].set_title('Semnal sinusoidal')

axs1[1].plot(t, semnal_sawthooth)
axs1[1].set_title('Semnal dinte')

y = semnal_sin + semnal_sawthooth
axs1[2].plot(t, y)
axs1[2].set_title('Semnal compus')

fig.savefig(fname = './plots/Semnal Compus.pdf', format = 'pdf')
plt.show()

