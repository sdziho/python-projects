import numpy as np

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


prost_broj=int(input("Unesi prost broj: "))   
redova=int(input("Unesi broj redova: "))
kolona=int(input("Unesi broj kolona: "))

G=[]
for i in range(redova):
    print("Unesi elemete",i+1,"reda (enter za unos elementa):")
    matrix=[]
    for j in range(kolona):
        broj=int(input())
        if(broj>=prost_broj):
            print("Neispravan unos")
            exit()
        matrix.append(broj)
    G.append(matrix)
      
 
q=prost_broj
k=redova
n=kolona
#G=np.array([[1,0,1,1],
#            [0,1,0,1]
#    ])
Ink = np.zeros((n-k, n-k), int)
np.fill_diagonal(Ink, 1)

A=[]
for i in range(len(G)):
    matrix=[]
    for j in range(k,len(G[0])):
        matrix.append(G[i][j])
    A.append(matrix)



K = np.zeros(len(G[0]))
for i in range (0,pow(2,len(G[0]))):
    formati="{0:0"+str(len(G[0]))+"b}"
    b = formati.format(i)
    matrix=[]
    for j in range(len(G[0])):
        matrix.append(int(b[j]))
    rjesenja=np.matmul(G,matrix) 
    flag=True
    for z in range(len(A)):
        if rjesenja[z]%q!=0:
            flag=False
            break
    if(flag==True):
        K = np.vstack([K, matrix])
        
K = np.delete(K, 0, 0)
print("Rijeci dualnog koda:\n",K)

AT=np.array(-np.transpose(A))
H=[]

for i in range(len(AT)):
    matrix=[]
    for j in range(len(AT[i])):
        matrix.append(int(AT[i][j]))
    for j in range(len(Ink[i])):
        matrix.append(int(Ink[i][j]))
    H.append(matrix)
    
print("\nH = ")
for i in range(len(H)):
    print(H[i])


brojevi=[]
for i in range(pow(q,n)):
    brojevi.append(numberToBase(i,q))
        
minimum=10000
for i in range(len(brojevi)):
    suma_jedinica=0
    for j in range(len(brojevi[i])):
        if brojevi[i][j]==1:
            suma_jedinica=suma_jedinica+1
    if(suma_jedinica<minimum and suma_jedinica!=0):
        minimum=suma_jedinica
        
d=minimum
print("\n[n,n-k,d] =",n,n-k,d)
    
