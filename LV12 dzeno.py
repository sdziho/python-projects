import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def racunaj_elem_matrica(idx,idy,Ix,Iy,It):
    A11,A12,A21,A22,B11,B21 = 0,0,0,0,0,0
    for i in range(idx-15,idx+16):
        for j in range(idy-15,idy+16):
            A11+=Ix[i][j]**2
            A12+=Ix[i][j]*Iy[i][j]
            A21+=Ix[i][j]*Iy[i][j]
            A22+=Iy[i][j]**2
            B11+=Ix[i][j]*It[i][j]
            B21+=Iy[i][j]*It[i][j]
    B11=B11*(-1)
    B21=B21*(-1)
    return [A11,A12,A21,A22,B11,B21]

def lucas_kanade(slika1, slika2, prozor):

    X = []
    Y = []
    Vx = []
    Vy = []
    cc = (slika1+slika2)/2
    Ix, Iy = np.gradient(cc)  
    It = (slika2-slika1)/1 
    A = np.zeros((2,2))
    B = np.zeros((2,1))

    for i in range (15,345,31):
        for j in range (15,405,31):
            [A11,A12,A21,A22,B11,B21] = racunaj_elem_matrica(i,j,Ix,Iy,It)
            A[0][0], A[0][1], A[1][0], A[1][1], B[0], B[1] = A11,A12,A21,A22,B11,B21
            X.append(i)
            Y.append(j)
            Ainv = np.linalg.pinv(A)
            TEMP = np.dot(Ainv,B)
            Vx.append(TEMP[0])
            Vy.append(TEMP[1])
                
                
    plt.imshow(slika1)
    plt.quiver(Y, X, Vy, Vx)
    plt.show()
    
  
    
    
slika1=mpimg.imread("data/Teddy/frame10.png")
slika2=mpimg.imread("data/Teddy/frame11.png")

lucas_kanade(slika1, slika2, 20)
    
    
    
    
    
    
    
    