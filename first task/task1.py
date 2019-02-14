import sys
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget , QApplication,QPushButton,QLabel,QInputDialog,QSpinBox,QFileDialog
from PyQt5.QtCore import QSize,pyqtSlot,QTimer,QThread
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import numpy as np
from numpy import array
from PIL.ImageQt import ImageQt
import time
import threading
 




class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,500,500,500)
        self.layout()
        self.path = 'this is empyt pass'
        self.img = ''
        
        
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
             self.path = path
             self.openImage(path)
             fourierImage = self.fourierTransform(path)
             modifiedImage = self.convertArrayToImage(fourierImage)
             self.showArrayImage(modifiedImage,250,50)
             
             #thread2 = threading.Thread(target=self.showArrayImage, args=(modifiedImage,50,150,),daemon = True).start()
             self.convertButton()
             #threading.Thread(target=self.convertButton).start()
             
        
        
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
         arr = np.asarray(img, np.uint8)
         print('this is image pixel function')
         return arr
         
         
    def convertArrayToImage(self,arr):
        img = Image.fromarray(arr)
        return img
        
        
    def showArrayImage(self,img,x,y):
        label = QLabel(self)
        qimage = ImageQt(img)
        pixmap = QPixmap.fromImage(qimage)
        label.setPixmap(pixmap)
        label.setGeometry(x,y,128,128)
        label.show()
        
    def fourierTransform(self,path):
        img = Image.open(path).convert('RGB')
        arrayImage = self.convertImageToArray(img)
        fourierImage = np.fft.fft2(arrayImage,axes=(0,1))
        fourierImage = np.fft.fftshift(fourierImage)
        magnitude_spectrum = 20*np.log(np.abs(fourierImage))
        magnitude_spectrum = np.uint8(magnitude_spectrum)
        return magnitude_spectrum
    
    
    def convertButton(self):
        btn = QPushButton("Convert Image",self)
        btn.setToolTip('This is an example button')
        btn.move(390,150)
        print('this is the convert button function')
        btn.show()
        threading.Thread(target=self.zerosFromOutToIn).start()
        #btn.clicked.connect(self.zerosFromOutToIn)
        
    def zerosFromOutToIn(self):
        fourierImage = self.fourierTransform(self.path)
        for i in range(70):
            upFrameZeros = self.upFrameZeros(fourierImage,i)
            downFrameZeros = self.downFrameZeros(upFrameZeros,-1-i)
            img = self.convertArrayToImage(downFrameZeros)
            thread1 = threading.Thread(target=self.showArrayImage, args=(img,10,200,),daemon = True).start()
            
            #self.showArrayImage(img,10,200)
            
        
            
            
        
        
    def upFrameZeros(self,img,position):
        for i in range(128):
            for j in range(len(img[0][0])):
                img[position][i][j] = 0
                img[i][position][j] = 0
        return img
    
    def downFrameZeros(self,img,position):
        for i in range(128):
            for j in range(len(img[0][0])):
                img[position][i][j] = 0
                img[i][position][j] = 0
        return img
    
        
    
       
     
        
        
        
        
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
