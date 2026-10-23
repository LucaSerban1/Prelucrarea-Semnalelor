import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi/2, np.pi/2, 10000)

sin = np.sin(t)
pade = (t - (7 * t**3) /60)/(1 + (t**2)/20)

eroare_sin_t = np.abs(sin - t)
eroare_sin_pade = np.abs(sin - pade)
eroare_t_pade = np.abs(t - pade)


fig, axs = plt.subplots(3)
fig1, axs1 = plt.subplots(3)
fig2, axs2 = plt.subplots(3)

for ax in axs.flat:
    ax.set_xlim([-np.pi/2, np.pi/2])

for ax in axs1.flat:
    ax.set_xlim([-np.pi/2, np.pi/2])

axs[0].plot(t, t)
axs[0].plot(t, sin)
axs[0].set_title('t vs Sin')
axs[0].legend(['t', 'Sin'])

axs[1].plot(t, pade)
axs[1].plot(t, sin)
axs[1].set_title('Pade vs Sin')
axs[1].legend(['Pade', 'Sin'])

axs[2].plot(t, sin)
axs[2].plot(t, pade)
axs[2].set_title('Pade vs t')
axs[2].legend(['Pade', 't'])


axs1[0].plot(t,eroare_sin_t)
axs1[0].set_title('Eroare t vs Sin')

axs1[1].plot(t, eroare_sin_pade)
axs1[1].set_title('Eroare Pade vs Sin')

axs1[2].plot(t, eroare_t_pade)
axs1[2].set_title('Eroare Pade vs t') 

axs2[0].plot(t, eroare_sin_t)
axs2[0].set_yscale('log')
axs2[0].set_title('Sin vs t')


axs2[1].plot(t,eroare_sin_pade)
axs2[1].set_yscale('log')
axs2[1].set_title('Eroare Pade vs Sin (log)')

axs2[2].plot(t, eroare_t_pade)
axs2[2].set_yscale('log')
axs2[2].set_title('Eroare Pade vs t (log)')

fig.tight_layout()
fig1.tight_layout()
fig2.tight_layout()

fig.savefig(fname='./plots/Aproximari.pdf', format = 'pdf')
fig1.savefig(fname='./plots/Eroare.pdf', format = 'pdf')
fig2.savefig(fname='./plots/Eroare log.pdf', format = 'pdf')

plt.show()