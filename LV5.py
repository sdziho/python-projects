import matplotlib.pyplot as plt
import numpy as np

N=80
x=np.linspace(0,10,1000)
f=np.ones(1000)*0.5
omega=1

for i in range(1,N):
    if (i-1)%4==0:
        a=2/(np.pi*i)
        f=f+a*np.cos(i*omega*x)
for i in range(3,N):
    if (i-3)%4==0:
        a=-2/(np.pi*i)
        f=f+a*np.cos(i*omega*x)
        
plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksimacija funkcije f1 Fourijeovim redom')
plt.axis([np.min(x), np.max(x), np.min(f), np.max(f)])
plt.grid(True)
plt.show()

