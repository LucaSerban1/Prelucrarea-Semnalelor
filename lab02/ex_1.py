import numpy as np
import matplotlib.pyplot as plt

fig1, axs = plt.subplots(2)
fig1.suptitle("Exercitiul 1: Sin vs Cos")

t = np.linspace(0, 1, 100)
semnal_sin = np.sin(2 * np.pi * 400 * t)
semnal_cos = np.cos((2 * np.pi * 400 * t) - (np.pi / 2))

axs[0].plot(t, semnal_sin, label = 'Semnal Sin')
axs[1].plot(t, semnal_cos, label = 'Semnal Cos')

fig1.savefig(fname = './plots/Sin vs Cos.pdf', format = 'pdf')
plt.show()