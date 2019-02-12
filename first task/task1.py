import sys
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget , QApplication,QPushButton,QLabel,QInputDialog,QSpinBox,QFileDialog
from PyQt5.QtCore import QSize,pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import numpy as np
from numpy import array
from PIL.ImageQt import ImageQt



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,500,500,300)
        self.layout()
        
        
    def layout(self):
        self.label()
        self.home()
        self.spinBox()
        self.show()
        
        
    def label(self):
        li = QLabel(self)
        li.setText('Numer Of Zeros')
        li.move(250,10)
        
    
    def home(self):
        btn = QPushButton("Select image",self)
        btn.setToolTip('This is an example button')
        btn.clicked.connect(self.on_click)
        btn.move(10,10)
        
    def spinBox(self):
        sbox = QSpinBox(self)
        sbox.move(350,10)
        
    @pyqtSlot()
    def on_click(self):
        name = QFileDialog()
        imgPath = name.getOpenFileName(self,'open file','','Image files (*.jpg *.png *.jpeg)')
        self.checkImage(imgPath[0])
        
    
    def checkImage(self,path):
         im = Image.open(path)
         width, height = im.size
         if width > 128 or height > 128 :
             print('invalid pic')
             self.imgFalseMsg()
         else :
             self.openImage(path)
             fourierImage = self.fourierTransform(path)
             array = self.convertImageToArray(fourierImage)
             imageArray = self.convertArrayToImage(array)
             self.showArrayImage(imageArray)
        
        
    def imgFalseMsg(self):
        li = QLabel(self)
        li.setText('Invalid Photo size \n Photo must be \n 128*128')
        li.setGeometry(10,30,128,128)
        li.show()
        
        
    def openImage(self,imagePath):
       label = QLabel(self)
       pixmap = QPixmap(imagePath)
       label.setPixmap(pixmap)
       label.setGeometry(10,50,128,128)
       im = Image.open(imagePath)
       width, height = im.size
       label.show()
       
    def convertImageToArray(self,img):
         arr = array(img)
         print('this is image pixel function')
         print("this is the array")
         arr[0][0][0] = 0
         arr[0][0][1] = 0
         arr[0][0][2] = 0
         arr[0][1][0] = 0
         arr[0][5][0] = 0
         return arr
         
         
    def convertArrayToImage(self,arr):
        img = Image.fromarray(arr)
        return img
        
        
    def showArrayImage(self,img):
        label = QLabel(self)
        qimage = ImageQt(img)
        pixmap = QPixmap.fromImage(qimage)
        label.setPixmap(pixmap)
        label.setGeometry(300,100,128,128)
        label.show()
        
    def fourierTransform(self,path):
        img = Image.open(path)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f) 
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        return magnitude_spectrum
       
     
        
        
        
        
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
