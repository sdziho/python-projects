import numpy as np

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]



q=int(input("Unesi broj q: "))   
n=int(input("Unesi broj kolona: "))

G=[]
for i in range(q):
    print("Unesi elemete",i+1,"reda (enter za unos elementa):")
    matrix=[]
    for j in range(n):
        broj=int(input())
        matrix.append(broj)
    G.append(matrix)
      
G=np.array(G) 
print("Unesi poruku velicine ",q)
poruka=input()
x=[]
for i in range(0,len(poruka)):
    if int(poruka[i])<q:
        x.append(int(poruka[i]))
    else:
        print("Neispravan unos")
        exit()  

#G=np.array([[0,1,1],
#            [1,0,1]
#    ])
poruka=np.array(x)

brojevi=[]
for i in range(pow(q,2)):
    cifre=(numberToBase(i,q))
    for j in range(2-len(cifre)):
        cifre.insert(0,0)
    brojevi.append(cifre)

skup_K=[]

for i in range(len(brojevi)):
    suma=np.zeros(len(G[0]))
    for j in range(len(brojevi[i])):
        suma=np.add(suma,brojevi[i][j]*(G[j]))
    skup_K.append(suma)
    
for i in range(len(skup_K)):
    for j in range(len(skup_K[i])):
        skup_K[i][j]=skup_K[i][j]%q
        
        
print("Sve rijeci koda: ")
for i in range(len(skup_K)):
    print(skup_K[i])
print("Sve rijeci prostora koda: ")
for i in range(pow(q,n)):
    cifre=(numberToBase(i,q))
    for j in range(n-len(cifre)):
        cifre.insert(0,0)
    print(cifre)
    
kodirana_poruka=(np.matmul(poruka,G))
for i in range(len(kodirana_poruka)):
    kodirana_poruka[i]=kodirana_poruka[i]%q

print("kodirana poruka glasi:", kodirana_poruka)