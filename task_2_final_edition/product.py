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





class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_logan.clicked.connect(self.logan_clicked) 
        self.ui.lbl_phantom.hide()
        self.ui.lbl_phantom.mousePressEvent = self.getPixel
        self.ui.btn_browse.clicked.connect(self.browse_clicked)

        self.size=""
        
#        


    def getPixel (self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(x,y)
        
        
        
    def browse_clicked (self ):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.bmp *.png *.gif *.jpg)")
        self.path = fileName
        if fileName:
            if self.ui.CBox_size.currentText()== "128*128" :
                self.size=128
            elif self.ui.CBox_size.currentText()== "256*256" :
                self.size=256
            elif self.ui.CBox_size.currentText()== "512*512" :
                self.size=512
            self.phantom_choose (self.size , fileName)   
            
            
    def logan_clicked (self):
        if self.ui.CBox_size.currentText()== "128*128" :
            self.size=128
            path="phantom128.png"
        elif self.ui.CBox_size.currentText()== "256*256" :
            self.size=256
            path="phantom256.png"
        elif self.ui.CBox_size.currentText()== "512*512" :
            self.size=512
            path="phantom512.png"
        self.phantom_choose (self.size , path)   
         
    def phantom_choose (self , lbl_size , path):
        self.ui.lbl_phantom.setGeometry(QtCore.QRect(170, 30, self.size, self.size))
        self.ui.lbl_phantom.show()
        array=self.convert_image_to_array(path)
        phantom_array,t1_array,t2_array,pd_array=self.genrate_total_phantom (array)

        while 1:
            if self.ui.comboBox.currentText()== "phantom" :
                array=phantom_array
            elif self.ui.comboBox.currentText()== "T1 effect" :
                array=t1_array
            elif self.ui.comboBox.currentText()== "T2 effect" :
                array=t2_array
            elif self.ui.comboBox.currentText()== "PD effect" :
                array=pd_array
            aaa=self.adding_image_to_lbl(array)
            self.ui.lbl_phantom.setPixmap(aaa)
            QApplication.processEvents()

        

    def genrate_total_phantom (self , phantom_array ):
        t1_array = np.ones((self.size,self.size))
        t2_array = np.ones((self.size,self.size))
        pd_array = np.ones((self.size,self.size))
        phantom_arrray = np.ones((self.size,self.size))
        for i in range (0 , self.size) :
            for j in range (0,self.size):
                if phantom_array[i][j]< 256 and phantom_array[i][j] >80 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=int (phantom_array[i][j]*(.2))
                    t2_array[i][j]=256-t1_array[i][j]
                    pd_array[i][j]=0

                elif phantom_array[i][j]< 100 and phantom_array[i][j] >20 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=int (phantom_array[i][j]*3)
                    t2_array[i][j]=256-t1_array[i][j]
                    pd_array[i][j]=100

                else :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=60+(phantom_array[i][j])
                    t2_array[i][j]=40+(phantom_array[i][j])
                    pd_array[i][j]=200
            aaa=self.adding_image_to_lbl(phantom_arrray)
            self.ui.lbl_phantom.setPixmap(aaa)
            QApplication.processEvents()
        

        return phantom_array,t1_array,t2_array,pd_array

    
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




        
        



def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
