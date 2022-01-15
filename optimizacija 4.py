import numpy as np

def numberToBase(n, b):#broj n pretvaramo u bazu b
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

n=int(input("Unesi n: "))
polinom=[]#koeficijenti polinoma, od onog uz nulti clan do onog uz najveci clan
r=int(input("Unesi broj koeficijenata polinoma: "))
for i in range(r):
    print("Unesi",i+1,". koeficijent")
    kf=int(input())
    polinom.append(kf)

#polinom=(1,1,0,1,1)
polinom2=[] #x na 2 -1
for i in range(n+1):    #pravimo keficijente polinoma tako da:
    if(i==0):           #na najvecoj potenciji se nalazi 1
        polinom2.append(1)
    elif (i==n):        #najmanjoj potenciji se nalazi -1
        polinom2.append(-1)
    else:               #na ostalim 0
        polinom2.append(0)
#dobijemo polinom x na n -1
  
# djelimo polinome, qx rezultat, rx ostatak
qx, rx = np.polynomial.polynomial.polydiv(polinom, polinom2)
  
if(rx.all()==0): #ako je ostatak nula
    print("polinom je paritetni")
  
kodovi=[]   #ubacivamo sve moguće binarne kodove koji mogu biti rjesenja hx+gx=0(mod x na n -1)
for i in range(pow(2,n-r+1)):
    cifre=numberToBase(i,2) #posto dobivamo 2 na n decimalnih brojeva, prebacimo ih u bazu 2
    for j in range(n-r+1-len(cifre)):
        cifre.insert(0,0)   #dodajemo nula ispred da dobijemo kod koji ima tacno n cifara
    kodovi.append(np.convolve(polinom,cifre)) #mnozimo polinom sa mogucim rjesenjem

print("\nKodovi:")  
for i in kodovi  :
    qx, rx = np.polynomial.polynomial.polydiv(i, polinom2) #dijelimo gore pomnozene kodove sa x na n -1
    if(rx.all()==0): #ako je ostatak pri djeljenju nula, ispisi ih
       print(i)
    
