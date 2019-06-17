import numpy as np
import random
import time
from PIL import Image ,ImageEnhance
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap
from mostafa import Ui_Dialog
import sys
import qimage2ndarray
np.set_printoptions(threshold=np.nan)


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lbl_phantom.setGeometry(QtCore.QRect(170, 30, 256, 256))




        zero_array = np.zeros((256,256))
        zero_array[10:100,10:100] = 140
#        zero_array[random.randint(30,70):random.randint(180,250),random.randint(30,70):random.randint(180,250)] = 120
        
        zero_array1 = np.zeros((256,256))
        zero_array1[80:200,80:200] = 90
        xx=zero_array1+zero_array


        #zero_array[random.randint(30,70):random.randint(180,250),random.randint(30,70):random.randint(180,250)] = random.randint(0,256)
#        zero_array[random.randint(0,100):random.randint(110,256),random.randint(0,100):random.randint(110,256)] = random.randint(0,256)
        aaa=self.adding_image_to_lbl(xx)
        self.ui.lbl_phantom.setPixmap(aaa)

    def adding_image_to_lbl(self , aarray):
        mostafa = qimage2ndarray.array2qimage(aarray)
        mostafa.save("output2.jpg")
        pixmap = QPixmap("output2.jpg")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap
    
    

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
#
#for x in range(10):
#    print (random.randint(1,101))