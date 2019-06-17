import time
from PIL import Image
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap
from mostafa import Ui_Dialog
import sys
import qimage2ndarray
np.set_printoptions(threshold=np.nan)


#self.lbl_phantom.setGeometry(QtCore.QRect(20, 20, 256, 256))



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_logan.clicked.connect(self.logan_clicked)
        self.ui.btn_browse.clicked.connect(self.browse_clicked)
        self.path=""
        
#        self.ui.lbl_phantom.setGeometry(QtCore.QRect(20, 20, 512, 512))
        
    def logan_clicked (self ):
        x=self.convert_image_to_array(self.path)
        phantom_array,t1_array=self.genrate_total_phantom (x) 
        while 1:
            if self.ui.comboBox.currentText()== "phantom" :
                array=phantom_array
            elif self.ui.comboBox.currentText()== "T1 effect" :
                array=t1_array

                
            aaa=self.adding_image_to_lbl(array)
            self.ui.lbl_phantom.setPixmap(aaa)
            QApplication.processEvents()

        

    def genrate_total_phantom (self , phantom_array ):
        t1_array = np.ones((256,256))

        for i in range (0 , 255) :
            for j in range (0,255):
                if phantom_array[i][j]< 256 and phantom_array[i][j] >80 :
                    t1_array[i][j]=int (phantom_array[i][j]*(.2))


                elif phantom_array[i][j]< 100 and phantom_array[i][j] >20 :
                    t1_array[i][j]=int (phantom_array[i][j]*3)


                else :
                    t1_array[i][j]=60+(phantom_array[i][j])

        return phantom_array,t1_array

    
    def convert_image_to_array(self , path):
        img=Image.open(path).convert('L')
        img_array = np.asarray(img)
        return img_array


    def adding_image_to_lbl(self , aarray):
        mostafa = qimage2ndarray.array2qimage(aarray)
        mostafa.save("output.jpg")
        pixmap = QPixmap("output.jpg")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap



    def browse_clicked(self):  # single responsibility principle
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.bmp *.png *.gif *.jpg)")
        if fileName:
            self.path = fileName
            self.logan_clicked ( )



        
        



def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        

