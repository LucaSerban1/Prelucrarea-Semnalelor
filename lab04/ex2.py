import numpy as np
import matplotlib.pyplot as plt


f0 = 200
fs = 130
f1 = f0 - fs
f2 = f0 + fs
durata = 0.05

t = np.linspace(0, durata, 5000)

n = np.arange(0, int(durata * fs) + 1)
tn = n / fs

def semnal(f, timp):
    return np.sin(2 * np.pi * f * timp)

fig, ax = plt.subplots(4, 1, figsize=(8, 7))

ax[0].plot(t, semnal(f0, t))

ax[1].plot(t, semnal(f0, t))
ax[1].plot(tn, semnal(f0, tn), 'o')

ax[2].plot(t, semnal(f2, t))
ax[2].plot(tn, semnal(f2, tn), 'o')

ax[3].plot(t, semnal(f1, t))
ax[3].plot(tn, semnal(f1, tn), 'o')

titluri = [f'{f0} Hz', f'{f0} Hz esantionat la fs = {fs} Hz',
           f'{f2} Hz', f'{f1} Hz']

for a, titlu in zip(ax, titluri):
    a.set_xlim(0, durata)
    a.set_ylim(-1.1, 1.1)
    a.set_title(titlu, fontsize=9)
ax[-1].set_xlabel('Timp (s)')

plt.tight_layout()
plt.savefig('plots/Semnale_sub_Nyquist.pdf', format='pdf')
plt.show()