import numpy as np
def vrati_kod(A):
    kodovi=[]
    for i in range (0,pow(2,len(A))):
        formati="{0:0"+str(len(A))+"b}"
        b = formati.format(i)
        matrix=[]
        for j in range(len(A)):
            matrix.append(int(b[j]))
        kodovi.append(matrix)
    print(kodovi)
    kodirano=[]
    for i in range(len(kodovi)):
        vektor=(np.array(kodovi[i]))
        suma=(np.matmul(vektor,A))
        for k in range (len(suma)):
            suma[k]=suma[k]%2
        
        kodirano.append(suma)
        
    for i in range(len(kodirano)):
        for j in range(len(kodirano[0])):
            kodirano[i][j]=kodirano[i][j]%2
    return kodirano            
        

A = np.array([
    [1,0,0,0,1,1,0], 
    [0,1,0,0,0,1,1],
    [0,0,1,0,1,1,1],
    [0,0,0,1,1,0,1]
])
kodovi=vrati_kod(A)
for i in range (len(kodovi)):
    print("kod",i+1,": ",kodovi[i])
for i in range(len(A)):
    
    sum_max=len(A[0])
    index=0
    for j in range(len(kodovi)):
        razlika=A[i]-kodovi[j]
        for k in range(len(razlika)):
            if (razlika[k]==-1):
                razlika[k]=1
        #print(np.sum(razlika))
        suma=np.sum(razlika)
        if(suma<sum_max):
            sum_max=suma
            index=j
    print("rijeci ",A[i]," najbliza rijec u kodu je", kodovi[index])