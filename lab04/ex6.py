import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


fs, x = wavfile.read('./wav/Vocale.wav')

x = x[:, 0]

n = len(x)
l = n // 100
pas = l // 2

grupuri = [x[i : i + l] for i in range(0, n - l + 1, pas)]

print(len(grupuri))

spectre = [np.abs(np.fft.fft(grup)[ : pas]) for grup in grupuri]
X = np.array(spectre).T

print(X.shape)

X = 20 * np.log10(X + 1e-6)

plt.figure(figsize=(10, 6))
plt.imshow(X,
    aspect="auto",
    extent=(0, len(x) / fs, 0, fs / 2),
    origin="lower",
    cmap="magma",
    vmin=0,
    vmax=100,
) 

plt.colorbar(label="Amplitudine (dB)")
plt.xlabel("Timp (s)")
plt.ylabel("Frecvență (Hz)")

plt.savefig('plots/Spectograma_Vocale.pdf', format='pdf')
plt.show()