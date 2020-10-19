import numpy as np
import matplotlib.pyplot as plt

br_uzoraka=1000

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
f=np.sin(10*np.pi*t)+6*np.sin(20*np.pi*t)+2*np.sin(40*np.pi*t)
F=myDFT(f)

plt.subplot(211)
plt.plot(t,f)
plt.xlabel('t')
plt.ylabel('f')
plt.title('f')
plt.axis([0, 1, -8, 8])
plt.grid(True)
plt.show()

plt.subplot(212)
plt.stem(F)
plt.xlabel('t')
plt.ylabel('F')
plt.title('DFT')
plt.axis([0, 50, 0, 5])
plt.grid(True)
plt.show()