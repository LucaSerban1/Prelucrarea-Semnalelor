import numpy as np
import matplotlib.pyplot as plt

# a)
fig1, axs1 = plt.subplots()
fig1.suptitle('Semnal a')
semnal_a = np.sin(2 * np.pi * 1 * 400 * np.linspace(0, 1, 1600))
axs1.stem(np.linspace(0, 1, 1600), semnal_a, label='Semnal a')

fig1.savefig(fname = './plots/semnal_2a.pdf', format = 'pdf')

# b)
fig2, axs2 = plt.subplots()
fig2.suptitle('Semnal b')
semnal_b = np.sin(2 * np.pi * 1 * 800 * np.linspace(0, 3, 800))
axs2.stem(np.linspace(0, 3, 800), semnal_b, label='Semnal b')

fig2.savefig(fname = './plots/semnal_2b.pdf', format = 'pdf')

# c)
fig3, axs3 = plt.subplots()
fig3.suptitle('Semnal c')
t_c = np.linspace(0, 0.6, 1000000)
semnal_c = np.mod(0.1 * 240 * t_c , 1)
axs3.plot(t_c, semnal_c, label='Semnal c')

fig3.savefig(fname = './plots/semnal_2c.pdf', format = 'pdf')

# d)
fig4, axs4 = plt.subplots()
fig4.suptitle('Semnal d') 
t_d = np.linspace(0, 1000, 10000)
semnal_d = np.sign(np.sin(2 * np.pi * 1 * 300 * t_d))
axs4.plot(t_d, semnal_d, label='Semnal d')

fig4.savefig(fname = './plots/semnal_2d.pdf', format = 'pdf')

# e)
fig5, axs5 = plt.subplots()
fig5.suptitle('Semnal e')
t_e = np.random.rand(128,128)
im = axs5.imshow(t_e, cmap='gray')
axs5.set_title('Semnal e')

fig5.savefig(fname = './plots/semnal_2e.pdf', format = 'pdf')

# f)
fig6, axs6 = plt.subplots()
fig6.suptitle('Semnal f')
t_f = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        t_f[i][j] = (i//16 + j//16) % 2

axs6.imshow(t_f, cmap='binary')
axs6.set_title('Semnal f')

plt.show()