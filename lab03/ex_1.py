import numpy as np
import matplotlib.pyplot as plt

N = 8

F = np.outer(np.arange(N), np.arange(N))
F = np.exp(F * 1j * -2 *np.pi /N)

fig, ax = plt.subplots(N, 1)

for i in range(N):
    ax[i].plot(F[i].real)
    ax[i].plot(F[i].imag, linestyle = 'dashed')

plt.show()
fig.savefig(fname = './plots/Matrice_Fourier.pdf', format = 'pdf')

FH = F.conj().T

product = FH @ F

print(np.allclose(N * np.eye(N), product))
print(np.linalg.norm(product - N * np.eye(N)))