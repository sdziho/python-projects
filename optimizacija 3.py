"""
Napravite proceduru kojoj je ulaz permutacija stupaca i otvoreni
tekst. Procedura vraća šifrat NAPRAVLJEN stupčastom transpozicijom.

Ulaze u vaš program je permutacija (npr. 4321) i otvoreni tekst (npr.
danas je lijep dana). A procedura vam vraća šifrat teksta danas je
lijep dana s obzirom na stupčastu transpoziciju s permutacsijim
stupaca 4321.
"""
import math
import numpy as np


permutacija_stupaca=input("Unesi permutaciju stupaca: ") #4312576
otvoren_tekst=input("Unesi otvoren tekst: ") #"KRIPTOGRAFIJAIKRIPTOANALIZAX"

broj_kolona=len(permutacija_stupaca)
broj_redova=math.ceil(len(otvoren_tekst)/broj_kolona)

matrica = []


for i in range(broj_redova):
    red_u_matrici=[]
    for j in range(broj_kolona):
        if(len(otvoren_tekst)>0):
            red_u_matrici.append(otvoren_tekst[0])
            otvoren_tekst=otvoren_tekst[1:]
        else:
            red_u_matrici.append('X')
    matrica.append(red_u_matrici)
    

matrica=np.array(matrica)
sifrirani_tekst=[]
for i in range(broj_kolona):
    index_kolone=int(permutacija_stupaca.index(str(i+1)))
    kolona=matrica[:,index_kolone]
    sifrirani_tekst.append(kolona)

      
print("Sifrirani tekst glasi: ")

for i in range(len(sifrirani_tekst)):
    for j in range(len(sifrirani_tekst[i])):
        print(sifrirani_tekst[i][j], end = '')