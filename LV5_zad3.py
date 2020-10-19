import matplotlib.pyplot as plt
import numpy as np

N=80
x=np.linspace(0,10,1000)
f=np.ones(1000)*(2/np.pi)
omega=1

for i in range(1,N):
    if i==1:                                
        a=0
        b=1
    else:
        a=(1/np.pi)*((-2*np.cos(np.pi*i)-2)/(i*i-1))
        b=(1/np.pi)*((-2*np.sin(np.pi*i))/(i*i-1))
    f=f+(a*np.cos(i*omega*x)+b*np.sin(i*omega*x))
    

plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksimacija funkcije f3 Fourijeovim redom')
plt.axis([np.min(x), np.max(x), np.min(f), np.max(f)])
plt.grid(True)
plt.show()
