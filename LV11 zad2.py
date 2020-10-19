#----------------ZADATAK 2------------------


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


plt.subplot(331)
plt.title('Original')
plt.imshow(img,cmap='gray') 

jedan=DCT(img[0:16,0:16].copy())
dva=DCT(img[0:16,16:32].copy())
tri=DCT(img[16:32,0:16].copy())
cetiri=DCT(img[16:32,16:32].copy())

prazna=np.zeros((32,32))
prazna[0:16,0:16]=(jedan) 
prazna[0:16,16:32]=(dva)    
prazna[16:32,0:16]=(tri) 
prazna[16:32,16:32]=(cetiri)
plt.subplot(332)
plt.title('DCT')
plt.imshow(prazna,cmap='gray')

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(jedan) 
prazna[0:16,16:32]=iDCT(dva)    
prazna[16:32,0:16]=iDCT(tri) 
prazna[16:32,16:32]=iDCT(cetiri)
plt.subplot(333)
plt.title('iDCT')
plt.imshow(prazna,cmap='gray')

M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    mat1[0][i] = jedan[0][i]
mat2=np.zeros((M,M))
for i in range(M):
    mat2[0][i] = dva[0][i]   
mat3=np.zeros((M,M))
for i in range(M):
    mat3[0][i] = tri[0][i]
mat4=np.zeros((M,M))
for i in range(M):
    mat4[0][i] = cetiri[0][i]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(334)
plt.title('Prvi red')
plt.imshow(prazna,cmap='gray')


M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    mat1[i][0] = jedan[i][0]
mat2=np.zeros((M,M))
for i in range(M):
    mat2[i][0] = dva[i][0]  
mat3=np.zeros((M,M))
for i in range(M):
    mat3[i][0] = tri[i][0]
mat4=np.zeros((M,M))
for i in range(M):
    mat4[i][0] = cetiri[i][0]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(335)
plt.title('Prva kolona')
plt.imshow(prazna,cmap='gray')


M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    mat1[i][i] = jedan[i][i]
mat2=np.zeros((M,M))
for i in range(M):
    mat2[i][i] = dva[i][i]  
mat3=np.zeros((M,M))
for i in range(M):
    mat3[i][i] = tri[i][i]
mat4=np.zeros((M,M))
for i in range(M):
    mat4[i][i]= cetiri[i][i]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(336)
plt.title('Dijagonala')
plt.imshow(prazna,cmap='gray')


M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<3 and j<3:
            mat1[i][j] = jedan[i][j]
mat2=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<3 and j<3:
            mat2[i][j] = dva[i][j]  
mat3=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<3 and j<3:
            mat3[i][j] = tri[i][j]
mat4=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<3 and j<3:
            mat4[i][j] = cetiri[i][j]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(337)
plt.title('9 baznih')
plt.imshow(prazna,cmap='gray')


M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<5 and j<5:
            mat1[i][j] = jedan[i][j]
mat2=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<5 and j<5:
            mat2[i][j] = dva[i][j]  
mat3=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<5 and j<5:
            mat3[i][j] = tri[i][j]
mat4=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<5 and j<5:
            mat4[i][j] = cetiri[i][j]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(338)
plt.title('25 baznih')
plt.imshow(prazna,cmap='gray')


M=len(jedan)
mat1=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<8 and j<8:
            mat1[i][j] = jedan[i][j]
mat2=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<8 and j<8:
            mat2[i][j] = dva[i][j]  
mat3=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<8 and j<8:
            mat3[i][j] = tri[i][j]
mat4=np.zeros((M,M))
for i in range(M):
    for j in range(M):
        if i<8 and j<8:
            mat4[i][j] = cetiri[i][j]

prazna=np.zeros((32,32))
prazna[0:16,0:16]=iDCT(mat1) 
prazna[0:16,16:32]=iDCT(mat2)    
prazna[16:32,0:16]=iDCT(mat3) 
prazna[16:32,16:32]=iDCT(mat4)            
plt.subplot(339)
plt.title('64 baznih')
plt.imshow(prazna,cmap='gray')