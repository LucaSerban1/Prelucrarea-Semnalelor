import numpy as np
import matplotlib.pyplot as plt

f = 3

N = 1000
t = np.linspace(0, 1, N, endpoint = False)
x = np.sin(2 * np.pi * f * t)
y = x * np.exp(-2 * np.pi * 1j * t)


fig, ax = plt.subplots(3, 2)

ax[0,0].scatter(t, x, s = 1, c = np.abs(x), cmap='viridis', vmin=0, vmax=1)
ax[0,0].set_xlabel('Time [s]')
ax[0,0].set_ylabel('Amplitude')
ax[0,0].set_ylim(-1.1, 1.1)

ax[0,1].scatter(y.real, y.imag, s = 1, c=np.abs(y), cmap='viridis', vmin=0, vmax=1)
ax[0,1].set_xlabel('Real')
ax[0,1].set_ylabel('Imaginar')
ax[0,1].set_ylim(-1.1, 1.1)

omega = [3, 5, 9, 17]
z = []
for w in omega:
    z.append(x * np.exp(-2 * np.pi * 1j * w * t))


ax[1, 0].scatter(z[0].real, z[0].imag, s = 1, c=np.abs(z[0]), cmap='viridis', vmin=0, vmax=1)
ax[1, 0].set_xlabel('Real')
ax[1, 0].set_ylabel('Imaginar')
ax[1, 0].set_ylim(-1.1, 1.1)

ax[1, 1].scatter(z[1].real, z[1].imag, s = 1, c=np.abs(z[1]), cmap='viridis', vmin=0, vmax=1)
ax[1, 1].set_xlabel('Real')
ax[1, 1].set_ylabel('Imaginar')
ax[1, 1].set_ylim(-1.1, 1.1)

ax[2, 0].scatter(z[2].real, z[2].imag, s = 1, c=np.abs(z[2]), cmap='viridis', vmin=0, vmax=1)
ax[2, 0].set_xlabel('Real')
ax[2, 0].set_ylabel('Imaginar')
ax[2, 0].set_ylim(-1.1, 1.1)

ax[2, 1].scatter(z[3].real, z[3].imag, s = 1, c=np.abs(z[3]), cmap='viridis', vmin=0, vmax=1)
ax[2, 1].set_xlabel('Real')
ax[2, 1].set_ylabel('Imaginar')
ax[2, 1].set_ylim(-1.1, 1.1)

plt.tight_layout()
fig.savefig(fname = 'plots/Fourier cu frecventa de infasurare.pdf', format='pdf')
plt.show()