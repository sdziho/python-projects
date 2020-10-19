import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('lena1.png')

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

def filt(B,r):
    mat=np.zeros((len(B), len(B[0])))
    for p in range(len(B)):
        for q in range(len(B[0])):
            if np.abs(B[p][q])<r:
                mat[p][q]=0
            else:
                mat[p][q]=B[p][q]
    return mat

B=DCT(img)
plt.figure()
plt.imshow(B,cmap='gray')
plt.title('DCT')


filtrirano=filt(B,0.5)

#plt.imshow(filtrirano,cmap='gray')

B=iDCT(filtrirano)
plt.figure()
plt.imshow(B,cmap='gray')
plt.title('filtirani iDCT')