import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def lucas_kanade(slika1, slika2, prozor):
    X=list()
    Y=list()
    vx=list()
    vy=list()
    sl=(slika1+slika2)/2
    ix,iy=np.gradient(sl)  
    it=slika2-slika1
    A=np.zeros((2,2))
    B=np.zeros((2,1))
    for i in range (15,345,31):
        for j in range (15,405,31):
            A=np.zeros((2,2))
            B=np.zeros((2,1))
            for m in range(i-15,i+16):
                for n in range(j-15,j+16):
                    A[0][0]+=(ix[m][n]**2)
                    A[0][1]+=ix[m][n]*iy[m][n]
                    A[1][0]+=ix[m][n]*iy[m][n]
                    A[1][1]+=(iy[m][n]**2)
                    B[0]+=ix[m][n]*it[m][n]
                    B[1]+=iy[m][n]*it[m][n]
            B[0]*=-1
            B[1]*=-1
            X.append(i)
            Y.append(j)
            inv=np.linalg.pinv(A)
            vx.append(np.dot(inv,B)[0])
            vy.append(np.dot(inv,B)[1])
                
                
    plt.imshow(slika1)
    plt.quiver(Y, X, vy, vx)
    plt.show()
    
  
    
    
slika1=mpimg.imread("data/Teddy/frame10.png")
slika2=mpimg.imread("data/Teddy/frame11.png")
lucas_kanade(slika1, slika2, 20)
