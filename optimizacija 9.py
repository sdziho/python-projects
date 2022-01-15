import numpy as np
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

#unos
r=int(input("Unesi r: "))
n=int(input("Unesi n: "))
q=int(input("Unesi q: "))
print("Unesi koeficijente polinoma: ")
koef=[]
for i in range(r+1):
    print("Unesi",i,". koeficijent")
    kf=int(input())
    koef.append(kf)
    #koef=(1,1,0,1) #duzine r+1
pomnozeni=[]
for i in range(pow(q,n-r)):
    cifre=(numberToBase(i,q))
    for j in range(n-r-len(cifre)):
        cifre.insert(0,0)
    pomnozeni.append(np.convolve(koef,cifre))

for i in range(len(pomnozeni)):
    for j in range(len(pomnozeni[i])):
        pomnozeni[i][j]=pomnozeni[i][j]%q

for i in pomnozeni:
    print(i)

G=[]
for i in range(n-r):
    stepen=numberToBase(2**i,2)
    G.append(np.convolve(koef,stepen))
    
    
maxlen=len(G[-1])

for i in range(len(G)):
    G[i]=G[i].tolist()
    for j in range(maxlen-len(G[i])):
        G[i].insert(0,0)
nova_G=[]
for i in reversed(G):       
   nova_G.append(i)

print("Matrica G:")
for i in nova_G:
    print(i)
        