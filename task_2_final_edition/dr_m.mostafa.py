import numpy as np
import matplotlib.pyplot as plt
#phantom =[[256,200,100],[120,10,200],[160,200,100]]

#t1 =np.array([[20,100,150,200,125,200],[20,100,150,200,125,200],[150,20,200,100,125,200],[125,150,20,200,100,200],[125,150,100,20,200,200],[125,150,100,200,20,200]])
#t2 =np.array([[5,10,15,17,12,17],[5,10,15,17,12,17],[15,5,17,10,12,17],[12,15,5,17,10,17],[12,15,10,5,17,17],[12,15,10,17,5,17]])
t1=





tr=10000
te=20
k_space=np.zeros((6,6), dtype = np.complex)

signal = np.ones((6,6))

for kspacerow in range(6):
    

    signal = signal * np.exp(-te/t2)
    
    for kspacecol in range(6):
        GX= 2*np.pi*kspacerow / 6
        GY= 2*np.pi*kspacecol / 6
                
        for i in range(6):
            for j in range(6):
                total_theta=(GX*i+GY*j)
                k_space[kspacerow, kspacecol] += signal[i,j]*np.exp(-1j*total_theta)
                
    signal = 1 - np.exp(-tr/t1)
            
            
            
test1 = np.absolute(np.fft.ifft2(k_space))
print(t1)
plt.imshow(t1, cmap='gray')
plt.show()
print(test1)
plt.imshow(test1, cmap='gray')
plt.show()

        

                


