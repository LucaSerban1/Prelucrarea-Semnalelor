import numpy as np
import matplotlib.pyplot as plt

n = 1000
t = np.linspace(0, 1, n, endpoint=False)
x = np.sin(2 * np.pi * 3 * t) + 0.5 * np.sin(2 * np.pi * 7 * t) + 0.2 * np.sin(2 * np.pi * 17 * t)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

ax[0].plot(t, x)
ax[0].set_title('Semnal original')
ax[0].set_xlabel('Timp (s)')

transformata = np.zeros(n, dtype=complex)
for m in range(n):
    for k in range(n):
        transformata[m] += x[k] * np.exp(-2j * np.pi * m * k / n)

frecvente = np.arange(n)
ax[1].stem(frecvente, np.abs(transformata))
ax[1].set_title('Transformata Fourier')
ax[1].set_ylabel(' | X(w) |')
ax[1].set_xlabel('Frecvență (Hz)')
ax[1].set_xlim(0, 50)

omega = [3, 7 , 17]

transformata_w : dict[float, np.complex128] = {}
zw = []

for w in omega:
        zw.append([x[i] * np.exp(-2 * np.pi * 1j * w * i / len(x)) for i in range(len(x))])

for i, val in enumerate(zw):
     transformata_w[omega[i]] = np.sum(val)

ax[2].stem(list(transformata_w.keys()), np.abs(list(transformata_w.values())))
ax[2].set_title('Transformata Fourier in omega')
ax[2].set_xlim(0,50)
ax[2].set_ylabel(' | X(w) | ')
ax[2].set_xlabel('Frecvență (Hz)')


plt.tight_layout()
fig.savefig(fname = 'plots/Transformata Fourier.pdf' , format = 'pdf')
plt.show()