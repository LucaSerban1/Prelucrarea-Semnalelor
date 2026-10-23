import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4)
fig.suptitle('4 Semnale cu faza diferite')
fig1, axs1 = plt.subplots(4)
fig1.suptitle('4 SNR uri pe 1 semnal')

n = 400
t = np.linspace(0, 1 , n)
semnal_1 = np.sin(2 * np.pi * 400 * t)
semnal_2 = np.sin(2 * np.pi * 400 * t + np.pi)
semnal_3 = np.sin(2 * np.pi * 400 * t + np.pi/2)
semnal_4 = np.sin(2 * np.pi * 400 * t + np.pi/3)

axs[0].plot(t, semnal_1)
axs[1].plot(t, semnal_2)
axs[2].plot(t, semnal_3)
axs[3].plot(t, semnal_4)

SNRs = [0.1 , 1, 10, 100]

z = np.random.normal(size = n)

for i, SNR in enumerate(SNRs):    
    y = np.sqrt((np.linalg.norm(semnal_1) ** 2) / (SNR * (np.linalg.norm(z) ** 2)))
    semnal_zgomot = semnal_1 + y * z
    axs1[i].plot(t, semnal_zgomot)    

fig.savefig(fname = './plots/4 Semnale cu faza diferite.pdf', format = 'pdf')
fig1.savefig(fname = './plots/4 SNR uri pe 1 semnal.pdf', format = 'pdf')
plt.show()