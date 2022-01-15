import numpy as np
import math

def numberToBase(n, b): #pretvara broj iz dekatske baze u bazu n
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

n=4;#broj bita
q=3;# 0 1 2
r=int(math.log2(n*(q-1)+1))
k=n-r

#paritetna matrica:
H=[]
for i in range (1,pow(2,r)):
    formati="{0:0"+str(r)+"b}"
    b = formati.format(i)
    matrix=[]
    for j in range(r):
        matrix.append(int(b[j]))
    H.append(matrix)
    


A=np.array(H);
A=np.transpose(A)
print("matrica H:",A)
sistem=[]
for i in range(pow(q,len(A[0]))):
    cifre=(numberToBase(i,q)) #pretvaramo broj u bazu q
    for j in range(len(A[0])-len(cifre)):
        cifre.insert(0,0)   #ako dobijemo broj npr 10, moramo dodati nule naprijed da dobijemo broj od len(A[0])) bitova
    matrix=np.array(cifre); #numpy matrica
    rjesenja=np.matmul(A,matrix) #mnozimo sve moguce kombinacije rjesenja sa matricom A
    flag=True
    for k in range(len(A)):
        if rjesenja[k]%q!=0:    #ako vektor rijesenja jednak nuli da to rjesenje dodamo u varijablu sistem
            flag=False
            break
    if(flag==True):
        sistem.append(matrix)   #dodajemo to rjesnje

print("Rjesnjea jednacine HxT=0: ")   
for i in range(len(sistem)):   
    print(sistem[i])
    
#zbog obimnosti algoritma (predugog izvrsavanja) izbacit cemo linearno nezavisne elemente
#koji se samo mogu dobiti zbirom neka dva vektora rjesenja jednacine HxT
generirajuca=sistem   
for i in range(len(generirajuca)):
    if(i>=len(sistem)):
        break;
    matrix=[]
    for j in range(i+1,len(generirajuca)):
        matrix=(generirajuca[i]+generirajuca[j]); #trazimo zbir svaka 2 elementa
    for z in range(len(matrix)):
        matrix[z]=matrix[z]%q; #ako je zbir prekoracio broj q, trazimo mu modul po q
    for k in range(len(generirajuca)):
        if(k>=len(generirajuca)):
            break;
        if str(matrix)==str(generirajuca[k]):   
            generirajuca.pop(k); #ako postoji red u matrici koji zavisi od zbira neka dva elementa, izbacujemo ga
            i=i-2;
            break;
print("Generirajuca matrica:")
for i in range(len(generirajuca)):           
    print(generirajuca[i])
            


        
