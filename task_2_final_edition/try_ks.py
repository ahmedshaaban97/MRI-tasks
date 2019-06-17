import time
from PIL import Image ,ImageEnhance , ImageFilter
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap
from nnnnn import Ui_MainWindow
import sys
import qimage2ndarray
import pyqtgraph as pg
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt
#phantom =[[256,200,100],[120,10,200],[160,200,100]]




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        t1,test1=self.K_Space()
        maxi=np.max(test1)
        mini=np.min(test1)
        test1=((test1-mini))*(255/(maxi-mini))
        pixmap=self.adding_image_to_lbl(t1)
        self.ui.label.setPixmap(pixmap)    
        pixmap=self.adding_image_to_lbl(test1)
        self.ui.label_2.setPixmap(pixmap)             

        



    def K_Space (self):
        t1 =np.array([[20,100,150,200,125,200,20,100,150,200,125,200],[20,100,150,200,125,200,20,100,150,200,125,200],[150,20,200,100,125,200,20,100,150,200,125,200],[125,150,20,200,100,200,20,100,150,200,125,200],[125,150,100,20,200,200,20,100,150,200,125,200],[125,150,100,200,20,200,20,100,150,200,125,200],[20,100,150,200,125,200,20,100,150,200,125,200],[20,100,150,200,125,200,20,100,150,200,125,200],[150,20,200,100,125,200,20,100,150,200,125,200],[125,150,20,200,100,200,20,100,150,200,125,200],[125,150,100,20,200,200,20,100,150,200,125,200],[125,150,100,200,20,200,20,100,150,200,125,200]])
        t2 =np.array([[5,10,15,17,12,17,5,10,15,17,12,17],[5,10,15,17,12,17,5,10,15,17,12,17],[15,5,17,10,12,17,5,10,15,17,12,17],[12,15,5,17,10,17,5,10,15,17,12,17],[12,15,10,5,17,17,5,10,15,17,12,17],[12,15,10,17,5,17,5,10,15,17,12,17],[5,10,15,17,12,17,5,10,15,17,12,17],[5,10,15,17,12,17,5,10,15,17,12,17],[15,5,17,10,12,17,5,10,15,17,12,17],[12,15,5,17,10,17,5,10,15,17,12,17],[12,15,10,5,17,17,5,10,15,17,12,17],[12,15,10,17,5,17,5,10,15,17,12,17]])
        tr=5000
        te=1500
        k_space=np.zeros((12,12), dtype = np.complex)
        
        signal = np.ones((12,12))
        
        for kspacerow in range(12):
            
        
            signal = signal * np.exp(-te/t2)
            
            for kspacecol in range(12):
                GX= 2*np.pi*kspacerow / 12
                GY= 2*np.pi*kspacecol / 12
                        
                for i in range(12):
                    for j in range(12):
                        total_theta=(GX*i+GY*j)
                        k_space[kspacerow, kspacecol] += signal[i,j]*np.exp(-1j*total_theta)
                        
            signal = 1 - np.exp(-tr/t1)
                    
                    
                    
        test1 = np.absolute(np.fft.ifft2(k_space))
        return t1 , test1
        
        
        
#print(t1)
#plt.imshow(t1, cmap='gray')
#plt.show()
#print(test1)
#plt.imshow(test1, cmap='gray')
#plt.show()

        

     
    def adding_image_to_lbl(self , aarray):
        mostafa = qimage2ndarray.array2qimage(aarray)
        mostafa.save("output.jpg")
        pixmap = QPixmap("output.jpg")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap
    
    


def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


