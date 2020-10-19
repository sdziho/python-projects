import matplotlib.pyplot as plt
import numpy as np

N=80
x=np.linspace(0,10,1000)
f=np.ones(1000)*(3/4) #a0=3/4
omega=1

for i in range(1,N):
    a=(1/np.pi)*((np.sin(np.pi*i)/i)+np.sin((np.pi/2)*i)/i)
    b=(1/np.pi)*((np.cos(np.pi*i))/i+np.cos(np.pi*i/2)/i-2/i)
    f=f+(a*np.cos(i*omega*x)+b*np.sin(i*omega*x))
    

plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksimacija funkcije f2 Fourijeovim redom')
plt.axis([np.min(x), np.max(x), np.min(f), np.max(f)])
plt.grid(True)
plt.show()