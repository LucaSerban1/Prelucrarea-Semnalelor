import numpy as np
import scipy
import sounddevice as sd

fs = 44100

t = np.linspace(0, 2, fs * 2)

semnal_1 = np.sin(2 * np.pi * 300 * t)
semnal_2 = np.sin(2 * np.pi * 942 * t)

semnal_total = np.concatenate((semnal_1, semnal_2))

sd.play(semnal_total, fs)
sd.wait()
scipy.io.wavfile.write(filename="./plots/semnal_total.wav", rate = fs, data = semnal_total.astype(np.float32))