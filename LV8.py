import numpy as np
import matplotlib.pyplot as plt
br_uzoraka=200
M=30
Fc=15

def myFFT(x):
    X=[];
    for i in range(len(x)):
        s1=0
        s2=0
        w=4*i*np.pi/len(x)
        for k in range(round(len(x)/2)):
            s1=s1+x[2*k]*np.exp(-1j*k*w)
            s2=s2+x[2*k+1]*np.exp(-1j*k*w)
        s=s1+s2
        s=np.abs(s)/br_uzoraka
        X.append(s)
    return X


t=np.linspace(0,1,br_uzoraka)
m=np.linspace(0,br_uzoraka,br_uzoraka)
h=np.sin(2*np.pi*Fc*(m-M/2))/(np.pi*(m-M/2))
f=np.sin(10*np.pi*t)+6*np.sin(20*np.pi*t)+2*np.sin(40*np.pi*t)

F=myFFT(f)
plt.subplot(211)
plt.plot(t,f)
plt.xlabel('t')
plt.ylabel('f')
plt.title('ulaz')
plt.axis([0, 1, -8, 8])
plt.grid(True)
plt.show()

plt.subplot(212)
plt.stem(F)
plt.xlabel('t')
plt.ylabel('F')
plt.title('ulaz')
plt.axis([0, 50, 0, 5])
plt.grid(True)
plt.show()

H=myFFT(h)
plt.figure()
plt.subplot(211)
plt.plot(t,h)
plt.xlabel('t')
plt.ylabel('h')
plt.title('filter')
plt.axis([0, 1,min(h),max(h)])
plt.grid(True)
plt.show()

plt.subplot(212)
plt.stem(H)
plt.xlabel('t')
plt.ylabel('F')
plt.title('filter')
plt.axis([0, 50,min(H),max(H)])
plt.grid(True)
plt.show()


c=np.convolve(f,h,'same')
C=myFFT(c)
plt.figure()
plt.subplot(211)
plt.plot(t,c)
plt.xlabel('t')
plt.ylabel('h')
plt.title('izlaz')
plt.axis([0, 1,min(c),max(c)])
plt.grid(True)
plt.show()

plt.subplot(212)
plt.stem(C)
plt.xlabel('t')
plt.ylabel('C')
plt.title('izlaz')
plt.axis([0, 50,min(C),max(C)])
plt.grid(True)
plt.show()