import numpy as np
import matplotlib.pyplot as plt

fig1, axs = plt.subplots(3)
fig1.suptitle('Semnal continuu')

# a)
t = np.linspace(0, 0.03 , 60)

# b)
x_t = np.cos(520 * np.pi * t + np.pi / 3)
y_t = np.cos(280 * np.pi * t - np.pi / 3)
z_t = np.cos(120 * np.pi * t + np.pi / 3)

axs[0].plot(t, x_t, label='x(t)')
axs[1].plot(t, y_t, label='y(t)')
axs[2].plot(t, z_t, label='z(t)')
fig1.savefig(fname = 'plots/xyz_semnal_continuu.pdf', format = 'pdf')

# c)
t_2 = np.linspace(0, 0.03, 200)

x_t_2 = np.cos(520 * np.pi * t_2 + np.pi / 3)
y_t_2 = np.cos(280 * np.pi * t_2 - np.pi / 3)
z_t_2 = np.cos(120 * np.pi * t_2 + np.pi / 3)

fig2, axs2 = plt.subplots(3)
fig2.suptitle('Semnal discret')

axs2[0].stem(t_2, x_t_2, label='x(t)')
# axs2[0].vlines(t_2,0, x_t_2, color='r', linestyles='-', alpha=0.5)
# axs2[0].plot(t_2, x_t_2, 'ro', label=f'x(t)[{len(x_t_2)}]')

axs2[1].stem(t_2, y_t_2, label='y(t)')
# axs2[1].vlines(t_2,0, y_t_2, color='r', linestyles='-', alpha=0.5)
# axs2[1].plot(t_2, y_t_2, 'ro', label=f'y(t)[{len(y_t_2)}]')

axs2[2].stem(t_2, z_t_2, label='z(t)')
# axs2[2].vlines(t_2,0, z_t_2, color='r', linestyles='-', alpha=0.5)
# axs2[2].plot(t_2, z_t_2, 'ro', label=f'z(t)[{len(z_t_2)}]')
fig2.savefig(fname = 'plots/xyz_semnal_discret.pdf', format = 'pdf')

plt.show()

# cand am semnale care variaza mult afiseaza numai o parte mica din el (pe o secunda)
# cand generezi stem uri, poti pune functia ca sa te verifici (trebuie stem ul sa pice functia)