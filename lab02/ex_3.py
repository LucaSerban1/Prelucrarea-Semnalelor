import numpy as np
import sounddevice as sd
import scipy.io.wavfile

fs = 44100
t = np.linspace(0, 2, fs * 2)
# a)
semnal_a = np.sin(2 * np.pi * 400 * t)

# b)
semnal_b = np.sin(2 * np.pi * 800 * t)

# c)
semnal_c = (np.mod(240 * t , 1))
semnal_c = ( semnal_c - np.min(semnal_c)) / (np.max(semnal_c) - np.min(semnal_c)) * 2 - 1

# d)
semnal_d = np.sign(np.sin(2 * np.pi * 300 * t))


for i, semnal in enumerate([semnal_a, semnal_b, semnal_c, semnal_d], start=1):
    sd.play(semnal, fs)
    sd.wait()

scipy.io.wavfile.write(filename="./plots/semnal_a.wav", rate = fs, data = semnal_a.astype(np.float32))
rate, date = scipy.io.wavfile.read("./plots/semnal_a.wav")
print(f"Semnal a: rate = {rate}, date = {date[:10]}")