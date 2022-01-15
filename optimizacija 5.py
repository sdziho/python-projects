import numpy as np

redova=int(input("Unesi broj redova: "))
kolona=int(input("Unesi broj kolona: "))
A=[]
for i in range(redova):
    print("Unesi elemete",i+1,"reda (enter za unos elementa):")
    matrix=[]
    for j in range(kolona):
        broj=int(input())
        if(broj!=0 and broj!=1):
            print("Neispravan unos")
            exit()
        matrix.append(broj)
    A.append(matrix)
      

A=np.array(A)
poruka=(input("Unesi poruku: "))
x=[]
for i in range(0,len(poruka)):
    if int(poruka[i])==0 or int(poruka[i])==1:
        x.append(int(poruka[i]))
    else:
        print("Neispravan unos")
        exit()  
        
x=np.array(x)
rezultat=[]

b=np.zeros(len(A))
sindrom=np.matmul(A, np.transpose(x)) 
K=[]
K = np.zeros(len(A[0]))
#print (sindrom)
for i in range (0,pow(2,len(A[0]))): 
    formati="{0:0"+str(len(A[0]))+"b}"
    b = formati.format(i)
    matrix=[]
    for j in range(len(A[0])):
        matrix.append(int(b[j])) 
    rjesenja=np.matmul(A,matrix) 
    flag=True
    for k in range(len(A)):
        if rjesenja[k]%2!=0:
            flag=False
            break
    if(flag==True):
        K = np.vstack([K, matrix])
        
K = np.delete(K, 0, 0)


sve_rijeci=[]
for i in range (0,pow(2,len(A[0]))): 
    formati="{0:0"+str(len(A[0]))+"b}"
    b = formati.format(i)
    matrix=[]
    for j in range(len(A[0])):
        matrix.append(int(b[j]))
    D=matrix+K
    lista=[]
    for j in range(len(D)):
        lista.append(D[j])
    sve_rijeci.append(lista)

for i in range (0,len(sve_rijeci)):
    for j in range (0,len(sve_rijeci[0])):
        for k in range (0,len(sve_rijeci[i][j])):
            if(sve_rijeci[i][j][k]==2): 
                sve_rijeci[i][j][k]=0

binarni=[]
for i in range (0,pow(2,len(A[0]))):
    formati="{0:0"+str(len(A[0]))+"b}"
    binarni.append(formati.format(i))
    
for i in range (0,len(sve_rijeci)):
    if(i>=len(sve_rijeci)):
        break
    for j in range(0,len(sve_rijeci[0])):
        rijec=sve_rijeci[i][0]
        for k in range (i+1,len(sve_rijeci)):
            if(k>=len(sve_rijeci)):
                break
            for z in range (0,len(sve_rijeci[0])):
                if(sve_rijeci[k][z]==rijec).all():
                    del sve_rijeci[k]
                    del binarni[k]
                    k=k-2
                    break

for i in range (0,len(sve_rijeci)):
    minimalni=1000
    index=0
    for j in range(0,len(sve_rijeci[0])):
        if (np.sum(sve_rijeci[i][j])<minimalni):
            minimalni=np.sum(sve_rijeci[i][j])
            index=j
    provjera=np.matmul(A, np.transpose(sve_rijeci[i][index]))
    if(provjera==sindrom).all(): 
        matrix=[]
        for j in range(len(A[0])):
            matrix.append(int(binarni[i][j]))
        rezultat=(matrix-x)
    
for i in range(len(rezultat)):
    if rezultat[i]==-1:
        rezultat[i]=1

print("Poslana rijec je",rezultat)
        
                

                    