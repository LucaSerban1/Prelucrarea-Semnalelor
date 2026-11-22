import numpy as np
import matplotlib.pyplot as plt
import time
import math

def dft(semnal):
    lung = len(semnal)
    transformata = np.zeros(lung, dtype=complex)
    for k in range(lung):         
        for m in range(lung):     
            transformata[k] += semnal[m] * np.exp(-2j * np.pi * m * k / lung)
    

fig, ax = plt.subplots()

fs = 1000
N = [128, 256, 512, 1024, 2048, 4096, 8192]
fft_time = []
dft_time = []


for n in N:
    t  = np.arange(n) / fs 
    semnal = np.sin(2 * np.pi * 60 * t)

    start_fft = time.perf_counter()
    np.fft.fft(semnal)
    end_fft = time.perf_counter()

    fft_time.append(end_fft - start_fft)

    start_dft = time.perf_counter()
    dft(semnal)
    end_dft = time.perf_counter()
    dft_time.append(end_dft - start_dft)
    print(f"N = {n}: DFT {dft_time[-1]:.3f} s, FFT {fft_time[-1]:.2e} s")

plt.title("Diferenta timp")
ax.plot(N, dft_time)
ax.plot(N, fft_time)
ax.set_yscale("log")
ax.set_xlabel("N (Esantioane)")
ax.set_ylabel("Timp")

fig.savefig(fname = "plots/Diferenta de timp.pdf", format = 'pdf')
plt.show()

