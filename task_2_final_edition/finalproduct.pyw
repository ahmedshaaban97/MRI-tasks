import time
from PIL import Image
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap
from GUI import Ui_Dialog
import sys
import qimage2ndarray

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.button_function()
        self.style_hide()
        #global varaibles
        self.path=""
        self.stop="" 
        self.progress=""
        self.stop=0
        self.progress=0


        
        
    def button_function (self) :
        self.ui.btn_browse.clicked.connect(self.browse_clicked)
        self.ui.btn_convert.clicked.connect(self.convert_clicked)
        self.ui.btn_pause.clicked.connect(self.stop_clicked)
        self.ui.btn_start.clicked.connect(self.start_clicked)
        self.ui.btn_continue.clicked.connect(self.continue_clicked)




        
    def style_hide (self) :
        self.ui.btn_browse.hide()
        self.ui.btn_convert.hide()
        self.ui.btn_pause.hide()
        self.ui.lbl_fourier.hide()
        self.ui.lbl_fourier_2.hide()
        self.ui.lbl_inverse.hide()
        self.ui.lbl_inverse_2.hide()
        self.ui.lbl_origin.hide()
        self.ui.progressBar_2.hide()
        self.ui.spinBox.hide()
        self.ui.spinBox_2.hide()
        self.ui.btn_continue.hide()


    def start_clicked (self):
        self.ui.lbl_welcome.hide()
        self.ui.btn_start.hide()
        self.ui.btn_browse.show()
        self.ui.btn_convert.show()
        self.ui.btn_pause.show()
        self.ui.lbl_fourier.show()
        self.ui.lbl_fourier_2.show()
        self.ui.lbl_inverse.show()
        self.ui.lbl_inverse_2.show()
        self.ui.lbl_origin.show()
        self.ui.progressBar_2.show()
        self.ui.spinBox.show()
        self.ui.spinBox_2.show()
        

    def convert_image_to_array(self , path):
        img=Image.open(path).convert('L')
        img_array = np.asarray(img)
        return img_array

    def fourier_transform_of_the_array(self , array ):
        fourier=np.fft.fftn(array)
        fshift = np.fft.fftshift(fourier)
        loog = 20*np.log(np.abs(fshift))
        return loog 
    

    def fourier_inverse_of_the_array(self , arrray ):
        ifshift = np.fft.ifftshift(arrray)
        ifourier=np.fft.ifft2(ifshift)
        looog =(np.abs(ifourier))
        return looog


    
    
    def fourier_transform_of_the_array1(self , array ):
        fourier=np.fft.fft2(array)
        s_l_fourier = np.fft.fftshift(fourier)

        return s_l_fourier 
    
    def ansformation(self , array ):
        loog = 20*np.log(np.abs(array))
        return loog
    
       
    
    def delay(self):
        valu=11-self.ui.spinBox_2.value()
        time.sleep((valu*valu)/500)
#        self.completed = 0
#        while self.completed < (100):
#            self.completed += 50
#            self.ui.progressBar.setValue(self.completed)
            
            
            
    def adding_image_to_lbl(self , aarray):
        mostafa = qimage2ndarray.array2qimage(aarray)
        mostafa.save("output.jpg")
        pixmap = QPixmap("output.jpg")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap
        self.ui.lbl_fourier.setPixmap(pixmap)
        
#    def adding_image_to_lbl_fourier_2(self , aarray):
#        mostafa = qimage2ndarray.array2qimage(aarray)
#        mostafa.save("output.jpg")
#        pixmap = QPixmap("output.jpg")
#        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
#        self.ui.lbl_fourier_2.setPixmap(pixmap)
#        
#    def adding_image_to_lbl_inverse(self , aarray):
#        mostafa = qimage2ndarray.array2qimage(aarray)
#        mostafa.save("output1.jpg")
#        pixmap = QPixmap("output1.jpg")
#        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
#        self.ui.lbl_inverse.setPixmap(pixmap)
#        
#    def adding_image_to_lbl_inverse_2(self , aarray):
#        mostafa = qimage2ndarray.array2qimage(aarray)
#        mostafa.save("output1.jpg")
#        pixmap = QPixmap("output1.jpg")
#        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
#        self.ui.lbl_inverse_2.setPixmap(pixmap)


#form out to in
    def zeros_of_fourier (self , array , index):
        zero_array = np.zeros((128,128))
        zero_array[index:-index,index:-index] = 1
        fourier_array= np.multiply(array,zero_array)
        return fourier_array

    def ones_of_fourier (self , array , index):
        one_array = np.ones((128,128))
        one_array[index:-index,index:-index] = 0
        fourier_array= np.multiply(array,one_array)
        return fourier_array
    
        
    
  

    
    def browse_clicked(self):  # single responsibility principle
        try:
            self.ui.lbl_fourier.hide()
            self.ui.lbl_inverse.hide()
            self.stop=1
            fileName, _filter = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.bmp *.png *.gif *.jpg)")
            self.path = fileName
            if fileName:
                array = self.convert_image_to_array(fileName)
                if (not len(array) == 128):
                
                    QMessageBox.about(self, "Warning" , "invalid image size, please browse 128*128 image" )            
                    self.continue_clicked ()
                    self.ui.lbl_fourier.show()
                    self.ui.lbl_inverse.show()
                
            
                else:
                    print(fileName)
                    print(_filter)
                    pixmap = QPixmap(fileName)
                    pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
                    self.ui.lbl_origin.setPixmap(pixmap)

                    image_array = self.convert_image_to_array(self.path)
                    fourier_array = self.fourier_transform_of_the_array(image_array)
                    pixmap=self.adding_image_to_lbl(fourier_array)
                    self.ui.lbl_fourier_2.setPixmap(pixmap)
                    
                    
                    fourier_array1 = self.fourier_transform_of_the_array1(image_array)
                    inverse_Array=self.fourier_inverse_of_the_array(fourier_array1 )        
                    pixmap=self.adding_image_to_lbl( inverse_Array)
                    self.ui.lbl_inverse_2.setPixmap(pixmap)


        except:
            QMessageBox.about(self, "Warning" , "This file isnt image, please DOT PLAY WITH ME" )            
            self.continue_clicked ()
            self.ui.lbl_fourier.show()
            self.ui.lbl_inverse.show()
                
                
    def stop_clicked (self):
        self.ui.btn_pause.hide()
        self.ui.btn_continue.show()
        self.stop=1
        return self.stop
    


    def continue_clicked (self):
        self.ui.btn_continue.hide()
        self.ui.btn_pause.show()
        self.stop=0  
        

        
        
    def convert_clicked(self):
        self.ui.btn_continue.hide()
        self.ui.btn_pause.show()
        self.stop=0
        self.ui.lbl_fourier.show()
        self.ui.lbl_inverse.show()  
        self.progress=0
        self.ui.progressBar_2.setValue(self.progress)

        image_array = self.convert_image_to_array(self.path)
        fourier_array = self.fourier_transform_of_the_array1(image_array)
        while 1:
            valu=self.ui.spinBox.value()
            for x in range (1, 64 ,valu ):
                fourierarray1 = self.zeros_of_fourier (fourier_array , x)
                fourierarray2 = self.ansformation(fourierarray1)
                pixmap=self.adding_image_to_lbl(fourierarray2)
                self.ui.lbl_fourier.setPixmap(pixmap)
                inverseArray=self.fourier_inverse_of_the_array(fourierarray1 )
                pixmap=self.adding_image_to_lbl( inverseArray)
                self.ui.lbl_inverse.setPixmap(pixmap)
                self.delay()
                self.progress=self.progress+((100/64)*valu)
                self.ui.progressBar_2.setValue(self.progress)
                while (self.stop==1):
                    QApplication.processEvents()
                    pass
                QApplication.processEvents()

            self.progress=0
            
            
#            QApplication.processEvents()
#fourier_array _ untillllllllllllllllllllll shifttttttttttttttttttttt
            
            
            
            valu=self.ui.spinBox.value()
            for x in range (64 , 1  , -valu): 
                fourierarray1 = self.ones_of_fourier (fourier_array , x)
                fourierarray2 = self.ansformation(fourierarray1)
                pixmap=self.adding_image_to_lbl(fourierarray2)
                self.ui.lbl_fourier.setPixmap(pixmap)
                inverseArray=self.fourier_inverse_of_the_array(fourierarray1 )
                pixmap=self.adding_image_to_lbl( inverseArray)
                self.ui.lbl_inverse.setPixmap(pixmap)
                self.delay()
                self.progress=self.progress+((100/64)*valu)
                self.ui.progressBar_2.setValue(self.progress)
                while (self.stop==1):
                    QApplication.processEvents()
                    pass
                QApplication.processEvents()

            self.progress=0



def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
