import numpy as np
import matplotlib.pyplot as plt

# a)
# Daca semnalul a fost eșantionat in fiecare ora, frecventa de esantionare este de 1 esantion pe ora, 
# ceea ce inseamna ca frecventa de esantionare (fs) este 1/3600 Hz (deoarece o ora are 3600 secunde).

# b)
# Avem 18,288 de esantioane, luate o data pe ora (24 esantionae pe zi).
# 18288 / 24 = 762 zile (2 ani si o luna).

# c) Avem fs = 1/3600 Hz.
# fs = 2 * fmax 
# fmax = fs / 2 = (1/3600) / 2 = 1/7200 Hz.

x = np.genfromtxt('Set_date/Train.csv', delimiter = ',', skip_header=1, usecols=2)
N = len(x)
fs = 1/3600

#d)
X = np.abs(np.fft.fft(x) / N)
X = X[:N//2]
f = fs * np.arange(N//2) / N

fig, ax = plt.subplots()

ax.set_yscale('log')
ax.set_xscale('log')
ax.plot(f, X)
ax.set_xlabel('Frecventa (Hz)')
ax.set_ylabel('|X(f)|')
plt.savefig('./plots/FFT.pdf', format = 'pdf')

#e
x_centrat = x - np.mean(x)
if np.mean(x_centrat) == 0:
    print("Functia centrată are media zero.")
else:
    print("Functia centrată:", np.mean(x_centrat))
    X_centrat = np.abs(np.fft.fft(x_centrat) / N)
    X_centrat = X_centrat[:N//2]


plt.figure()
plt.plot(x_centrat)
plt.title('Semnalul fara componenta continua')
plt.xlabel('Esantion (ore)')
plt.ylabel('Nr masini - media')
plt.savefig('./plots/Semnal fara componenta continua.pdf')

#f
idx = np.argsort(X_centrat)[-4:][::-1]

for i in idx:
    T_ore = 1 / f[i] / 3600
    print(f"|X| = {X_centrat[i]:.2f}  f = {f[i]:.3e} Hz  "
          f"Timp: {T_ore / 24:.1f} zile")

#g
saptamani = x[:N // 168 * 168].reshape(-1, 7, 24)
trafic_pe_zi = saptamani.sum(axis=2).mean(axis=0)

start = 1056
luna = 30 * 24                       

plt.figure(figsize=(12, 4))
plt.plot(np.arange(start, start + luna), x[start:start + luna])
plt.xlabel('Esantion (ore)')
plt.ylabel('Nr masini')
plt.title('O luna de trafic, incepand de luni')
plt.savefig('./plots/Trafic_lunar.pdf')

#h
# Abordare:
#        - Ora: facem media traficului pe fiecare din cele 24 de ore ale zilei.
#            Minimul apare noaptea (~3-5), deci aflam ce ora corespunde primului esantion.
#        - Ziua saptamanii: facem media traficului pe fiecare din cele 7 zile ale saptamanii.
#            Cele 2 zile consecutive cu trafic minim sunt weekendul, deci aflam in ce zi a inceput inregistrarea.
#        - Data: cautam zile cu trafic anormal de mic (sarbatori cu data fixa: Craciun, Anul Nou).
#            Daca ziua k e 25 decembrie, calculam inapoi data de start.
#            Ziua saptamanii in care cade sarbatoarea ne ajuta sa restrangem anul.
#            Indiciu in plus: trecerea la ora de vara muta tiparul zilnic cu o ora.
# Probleme:
#        - Nu stim tara, deci nici sarbatorile sau regulile pentru ora de vara.
#        - Zgomotul si outlierii pot imita sau ascunde o sarbatoare.
#        - Calendarul se repeta dupa cativa ani, deci anul poate ramane ambiguu.
#        - Depinde de durata si de nivelul traficului:
#            * 1 an sau mai mult: putem afla si data (daca se vede o sarbatoare)


#i
tart = 1056                       
luna = 28 * 24
semnal_luna = x[start:start + luna]

procent = 0.95                       

X_luna = np.fft.fft(semnal_luna)
modul = np.abs(X_luna)
prag = np.percentile(modul, procent * 100)   

X_luna[modul <= prag] = 0                    
semnal_filtrat = np.real(np.fft.ifft(X_luna))

idx = np.arange(start, start + luna)
plt.figure(figsize=(12, 4))
plt.plot(idx, semnal_luna, linewidth=0.8, label='semnal original')
plt.plot(idx, semnal_filtrat, linewidth=2, label='semnal filtrat')
plt.xlabel('Esantion (ore)')
plt.ylabel('Nr masini')
plt.legend()
plt.savefig('./plots/Semnal Filtrat.pdf')

plt.show() 

