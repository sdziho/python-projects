import numpy as np

def moduloInverz(a,d):
    for i in range(d):
        if (a*i)%d == 1:
            return i
    return 0

def kriptirajZnakAfino(znak,a,b):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if znak in abeceda:
        rotirano = abeceda[((abeceda.index(znak)*a)+b)%len(abeceda)]
    else:
        rotirano = znak
    return rotirano

def desifriraj(znak,a,b):
    abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if znak in abeceda:
        rotirano = abeceda[(moduloInverz(a,len(abeceda))*(abeceda.index(znak)-b))%len(abeceda)]
    else:
        rotirano = znak
    return rotirano
print ("Upiši parametre za afinu šifru")
a = int(input("Upiši faktor a: "))
while moduloInverz(a, 26) == 0:
    print ("Faktor a koji ste unijeli nema inverz za duljinu abecede od 27 znakova.")
    a = int(input("Upiši faktor a:"))
b = int(input("Upiši faktor b: "))
tekst = input("Upiši poruku koju želiš šifrirati: ").upper()

sifriranitekst= ""
for znak in tekst:  
    sifriranitekst += kriptirajZnakAfino(znak, a, b)

desifrirani=""   
for znak in sifriranitekst:  
    desifrirani += desifriraj(znak, a, b)
print("Sifrirani tekst:", sifriranitekst,"Desifrirani tekst:", desifrirani)

abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
novi_tekst=input("Unesi tekst nad kojim vrsimo kriptoanalizu: ").upper()
brojac=np.zeros(26)
for i in range(26):
    brojac[i]=novi_tekst.count(chr(i+65))

b=np.argmax(brojac)
brojac[np.argmax(brojac)]=0
drugo_najcesce=np.argmax(brojac)
a=-1
for i in range(26):
    if(8*i+b)%26==drugo_najcesce:
        a=i
        break
#PCNJWBNGPCQGPVCPCMQGFGNEXCYCIGWFURGTCIW
print("a =",a,"b =",b)
print("desifrirani tekst primjenom kriptoanalize glasi: ")
desif=""
for znak in novi_tekst:
    desif+= desifriraj(znak, a, b)
print(desif)