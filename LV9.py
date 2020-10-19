import numpy as np
import matplotlib.pyplot as plt
from typing import List
from numpy import sin
from numpy import pi
import random
def funkcija_sa_sumom(t: List[float]):
    return [3 * sin(2 * pi * 5 * x) + random.randint(-200, 300) / 100 for x in t]
def funkcija_sa_sumom_2(t: List[float]):
    return [3 * sin(2 * pi * 5 * x) + 0.3 * sin(2 * pi * 80 * x) for x in t]

br_uzoraka=1000
M=50
Fc=20

def myDFT(x):
    X=list();
    for i in range(len(x)):
        dodaj=0
        w=i*2*np.pi/len(x)
        for k in range(len(x)):
            dodaj=dodaj+x[k]*np.exp(-1j*k*w)
        dodaj=np.abs(dodaj)/br_uzoraka
        X.append(dodaj)
    return X


t=np.linspace(0,1,br_uzoraka)
m=np.linspace(0,br_uzoraka,br_uzoraka)
h=np.sin(2*np.pi*Fc*(m-M/2))/(np.pi*(m-M/2))
f=funkcija_sa_sumom(t)
f2=funkcija_sa_sumom_2(t)
F=myDFT(f)
F2=myDFT(f2)

plt.subplot(231)
plt.plot(t,f)
plt.xlabel('t')
plt.ylabel('f')
plt.title('ulaz')
plt.axis([0, 1, -8, 8])
plt.grid(True)
plt.show()

plt.subplot(234)
plt.stem(F)
plt.xlabel('t')
plt.ylabel('F')
plt.title('ulaz')
plt.axis([0, 50, 0, 5])
plt.grid(True)
plt.show()

H=myDFT(h)

plt.subplot(232)
plt.plot(t,h)
plt.xlabel('t')
plt.ylabel('h')
plt.title('filter')
plt.axis([0, 1,min(h),max(h)])
plt.grid(True)
plt.show()

plt.subplot(235)
plt.stem(H)
plt.xlabel('t')
plt.ylabel('H')
plt.title('filter')
plt.axis([0, 50,min(H),max(H)])
plt.grid(True)
plt.show()


H=H/max(H) 
C=H*F
c=np.fft.ifft(C)*br_uzoraka

plt.subplot(233)
plt.plot(t,c)
plt.xlabel('t')
plt.ylabel('c')
plt.title('izlaz')
plt.axis([0, 1,min(c),max(c)])
plt.grid(True)
plt.show()

plt.subplot(236)
plt.stem(C)
plt.xlabel('t')
plt.ylabel('C')
plt.title('izlaz')
plt.axis([0, 50,min(C),max(C)])
plt.grid(True)
plt.show()

plt.figure()
plt.subplot(231)
plt.plot(t,f2)
plt.xlabel('t')
plt.ylabel('f2')
plt.title('ulaz')
plt.axis([0, 1, -8, 8])
plt.grid(True)
plt.show()

plt.subplot(234)
plt.stem(F2)
plt.xlabel('t')
plt.ylabel('F2')
plt.title('ulaz')
plt.axis([0, 50, 0, 5])
plt.grid(True)
plt.show()

H=myDFT(h)

plt.subplot(232)
plt.plot(t,h)
plt.xlabel('t')
plt.ylabel('h2')
plt.title('filter')
plt.axis([0, 1,min(h),max(h)])
plt.grid(True)
plt.show()

plt.subplot(235)
plt.stem(H)
plt.xlabel('t')
plt.ylabel('H2')
plt.title('filter')
plt.axis([0, 50,min(H),max(H)])
plt.grid(True)
plt.show()


H=H/max(H) 
C=H*F2
c=np.fft.ifft(C)*br_uzoraka

plt.subplot(233)
plt.plot(t,c)
plt.xlabel('t')
plt.ylabel('c2')
plt.title('izlaz')
plt.axis([0, 1,min(c),max(c)])
plt.grid(True)
plt.show()

plt.subplot(236)
plt.stem(C)
plt.xlabel('t')
plt.ylabel('C2')
plt.title('izlaz')
plt.axis([0, 50,min(C),max(C)])
plt.grid(True)
plt.show()