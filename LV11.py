#KOD JE PODJELJAN NA ZADATAK 1 I ZADATAK 2
#ZADATAK 2 POCINJE OD KOMENATARA ZA ZADATAK 2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('LV11.png')

def DCT(A):
    M=len(A)
    N=len(A[0])
    B=np.zeros((M, N))
    alfap=0
    alfaq=0
    for p in range(M):
        for q in range(N):
            suma=0
            for m in range(M):
                for n in range(N):
                    suma+=A[m][n]*np.cos(np.pi*(2*m+1)*p/(2*M))*np.cos(np.pi*(2*n+1)*q/(2*N))
                    
            if p!=0:
                alfap=np.sqrt(2/M)
            else:
                alfap=1/(np.sqrt(M))
                
            if q!=0:
                alfaq=np.sqrt(2/N)
            else:
                alfaq=1/np.sqrt(N)
                
            B[p][q]=alfap*alfaq*suma
    return B

def iDCT(B):
    M=len(B)
    N=len(B[0])
    A=np.zeros((M, N))
    alfap=0
    alfaq=0
    for m in range(M):
        for n in range(N):
            suma=0
            for p in range(M):
                for q in range(N):
                    if p!=0:
                        alfap=np.sqrt(2/M)
                    else:
                        alfap=1/(np.sqrt(M))
                        
                    if q!=0:
                        alfaq=np.sqrt(2/N)
                    else:
                        alfaq=1/np.sqrt(N)
                    suma+=alfap*alfaq*B[p][q]*np.cos(np.pi*(2*m+1)*p/(2*M))*np.cos(np.pi*(2*n+1)*q/(2*N))
            
            A[m][n]=suma
    return A


B=DCT(img)
M=len(B)
N=len(B[0])


plt.subplot(331)
plt.title('Original')
plt.imshow(img,cmap='gray') 

plt.subplot(332)
plt.title('DCT')
plt.imshow(B,cmap='gray')

plt.subplot(333)
plt.title('IDCT')
plt.imshow(iDCT(B),cmap='gray')


mat=np.zeros((M,N))
for i in range(M):
    mat[0][i] = B[0][i]
plt.subplot(334)
plt.title('Prvi red')
plt.imshow(iDCT(mat),cmap='gray')

mat=np.zeros((M,N))
for i in range(M):
    mat[i][0] = B[i][0]
plt.subplot(335)
plt.title('Prva kolona')
plt.imshow(iDCT(mat),cmap='gray')

mat=np.zeros((M,N))
for i in range(M):
    mat[i][i] = B[i][i]
plt.subplot(336)
plt.title('Dijagonala')
plt.imshow(iDCT(mat),cmap='gray')

mat=np.zeros((M,N))
for i in range(M):
    for j in range(N):
        if i<3 and j<3:
            mat[i][j] = B[i][j]
plt.subplot(337)
plt.title('9 baznih')
plt.imshow(iDCT(mat),cmap='gray')

mat=np.zeros((M,N))
for i in range(M):
    for j in range(N):
        if i<8 and j<8:
            mat[i][j] = B[i][j]
plt.subplot(338)
plt.title('64 bazne')
plt.imshow(iDCT(mat),cmap='gray')

mat=np.zeros((M,N))
for i in range(M):
    for j in range(N):
        if i<16 and j<16:
            mat[i][j] = B[i][j]
plt.subplot(339)
plt.title('256 baznih')
plt.imshow(iDCT(mat),cmap='gray')