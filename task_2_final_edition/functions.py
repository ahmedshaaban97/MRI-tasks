import numpy as np

def drawcurves(self,unitVector, delta_t , t1 , t2 , theta , alpha):
    theta = ((theta * np.pi )/180)
    rotationx = [[1,0,0],[0,np.cos(theta),np.sin(theta)],[0,-np.sin(theta),np.cos(theta)]]
    rotationxy = [[np.cos(alpha),-np.sin(alpha),0],[-(np.sin(alpha)),np.cos(alpha),0],[0,0,1]]
    decayRecoveryArray = [[np.exp(-(range(delta_t))/t2),0,0], [0,np.exp(-(range(delta_t))/t2),0],[0,0,np.exp((range(delta_t))/t1)]]
    finaldrArray = [[0],[0],[(1-(np.exp(delta_t/t1)))]]
    rotatedVector = np.matmul(rotationx,unitVector)
    rotatedVector = np.matmul(rotationxy,rotatedVector)
    rotatedVector = np.matmul(decayRecoveryArray,rotatedVector)
    rotatedVector = np.add(finaldrArray,rotatedVector)
        


