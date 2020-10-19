string='BABAABBACABABB'   
            
rijecnik = list()
for i in range(65,91):
    rijecnik.append(chr(i))
#kod je dat kao index_slova+1
S=string[0]
ispis=list()
for i in range(len(string)-1):
    C=string[i+1]
    if S+C in rijecnik:
        S=S+C
    else:
        ispis.append(rijecnik.index(S)+1)
        rijecnik.append(S+C)
        S=C
    
if S!='':
    ispis.append(rijecnik.index(S)+1)
    



#---------dekodiranje--------
    

rijecnik = list()
for i in range(65,91):
    rijecnik.append(chr(i))
#kod je dat kao index_slova+1
S=''
dekomp=list()
for i in range(len(ispis)):
    K=ispis[i]
    P=rijecnik[K-1]
    dekomp.append(P)
    if S!='':
        rijecnik.append(S+P[0])
    S=P

broj_bita=0
pow2=1
while True:
    if pow2>len(rijecnik):
        break;
    else:
        pow2*=2
        broj_bita+=1

stri='{:0'+str(broj_bita)+'b}'    
print(broj_bita)    
    
print ("Izvorna recenica: " +string)
print("Kompletirani rjecnik:")
print("Simbol | Binarni kod | Decimalna vrijednost")
for i in range(len(rijecnik)):
    print("%6s | %12s | %8r" % (rijecnik[i], stri.format(i+1), i+1) )
       
print("Rezultat kompresije: ",end=' ')
for i in ispis:
    print (i,end=' ')
print("")   
print("Napisano binarno:", end=' ')
for i in ispis:
    print (stri.format(i),end=' ')
print("")       
print("Rezultat nakon dekompresije: ", end=' ')
for i in dekomp:
    print(i,end='')
print("")            
print("Stepen kompresije: " +str(8*len(string)/(len(dekomp)*broj_bita)))
    