import sys
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget , QApplication,QPushButton,QLabel,QInputDialog,QSpinBox,QFileDialog,QProgressBar
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
        self.spinb = ''
        self.fimg = ''
        self.layout()
        self.path = 'this is empyt pass'
        
        
        self.progress = 0
        
        
        #self.threadClass = ThreadClass()
        #self.threadClass.start()
        
        
    def layout(self):
        self.label()
        self.home()
        self.spinb = self.spinBox()
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
        sbox.setValue(8)
        sbox.move(350,10)
        return sbox
        
        
    def progressBar(self):
        progressBar = QProgressBar(self)
        progressBar.setGeometry(250,250,230,20)
        return progressBar
        
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
             self.fimg = fourierImage
             modifiedImage = self.convertArrayToImage(fourierImage)
             self.showArrayImage(modifiedImage,250,50)
             
             #thread2 = threading.Thread(target=self.showArrayImage, args=(modifiedImage,50,150,),daemon = True).start()
             self.convertButton()
             self.convertInOutButton()
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
       #im = Image.open(imagePath)
       #width, height = im.size
       label.show()
       
    def convertImageToArray(self,img):
         arr = np.asarray(img, np.uint8)
         #print('this is image pixel function')
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
    
    
    
    def convertInOutButton(self):
        btn = QPushButton("Convert InOut",self)
        btn.setToolTip('This is an example button')
        btn.move(390,350)
        #print('this is the convert in outbutton function')
        btn.show()
        btn.clicked.connect(self.zerosFromInToOut)
        
        
    
    
    def convertButton(self):
        btn = QPushButton("Convert Image",self)
        btn.setToolTip('This is an example button')
        btn.move(390,150)
        #print('this is the convert button function')
        btn.show()
        progressBar = self.progressBar()
        progressBar.show()
        self.progress = progressBar
        
        #threading.Thread(target=self.zerosFromOutToIn).start()
        #threading.Thread(target=btn.clicked.connect,args=(self.zerosFromOutToIn,)).start()

        
        btn.clicked.connect(self.startConverting)
        #threading.Thread(target=btn.clicked.connect, args=(self.zerosFromOutToIn,),daemon = True).start()
       # threading.Thread(target=btn.clicked.connect, args=(self.zerosFromInToOut,),daemon = True).start()
        #threading.Thread(target=btn.clicked.connect, args=(self.startConverting,),daemon = True).start()
        #btn.clicked.connect(self.zerosFromOutToIn)
        
        #btn.clicked.connect(self.zerosFromInToOut)
        
        
    def startConverting(self):
        for i in range (5):
        
            self.zerosFromOutToIn()
            self.zerosFromInToOut()
        
        
    def restoreOriginalImage(self) : 
        img = self.fimg
        mimg = self.convertArrayToImage(img)
        self.showArrayImage(mimg,10,200)
        
    def giveOriginalImage(self) : 
        img = self.fimg
        return img
        
    def zerosFromOutToIn(self):
        label = QLabel(self)
        
        #while 1 :
        fourierFImage = self.fourierTransform(self.path)
            
        #print(fourierImage)
        #value = self.spinb.value()
        value = 64
        step = 2
            #label = QLabel(self)
            #print('this is the mult ', 100/value)
        
        for i in range(64):
                #print('first run')
            upFrameZeros = self.upFrameZeros(fourierFImage,i)
            downFrameZeros = self.downFrameZeros(upFrameZeros,-1-i)
            img = Image.fromarray(downFrameZeros)
            img.save('my.png')
                
                #qimage = ImageQt(fsimg)
                #pixmap = QPixmap.fromImage(qimage)
            pixmap = QPixmap('my.png')
            pixmap = pixmap.scaled(int(pixmap.height()),int(pixmap.width()))
            label.setPixmap(pixmap)
            label.setGeometry(10,200,128,128)
            label.show()
            time.sleep(0.009)
                
                
            
                
            #fourierImage = self.convertArrayToImage(downRightFrameZeros)
                #self.showArrayImage(newimg,10,200)
            
            #threading.Thread(target=self.showArrayImage, args=(fsimg,10,200,),daemon = True).start()
                #self.showArrayImage(fsimg,10,200)
                #time.sleep(0.2)
            self.progress.setValue(i*(100/(value-1)))
        
        
        
        
                
        
    def upFrameZeros(self,img,position):
        #print('this is upFrameZeros')
        for i in range(128):
            for j in range(len(img[0][0])):
                img[position][i][j] = 0
                img[i][position][j] = 0
            
        return img
    
    def downFrameZeros(self,img,position):
        #print('this is downFrameZeros')
        for i in range(128):
            for j in range(len(img[0][0])):
                img[position][i][j] = 0
                img[i][position][j] = 0
            
        return img
    
    
    def zerosFromInToOut(self):
        label = QLabel(self)
    
        #while 1 :
        fourierFImage2 = self.fourierTransform(self.path)
        #print(fourierImage)
        #value = self.spinb.value()
        value = 64
        step = 2
            #label = QLabel(self)
            #print('this is the mult ', 100/value)
        
        for i in range(64):
                #print('first run')
            upLeftFrameZeros = self.upLeftFrameZeros(fourierFImage2,step,63-i)
            downRightFrameZeros = self.downRightFrameZeros(upLeftFrameZeros,step,64+i)
            img = Image.fromarray(downRightFrameZeros)
            img.save('my.png')
                
                #qimage = ImageQt(fsimg)
                #pixmap = QPixmap.fromImage(qimage)
            pixmap = QPixmap('my.png')
            pixmap = pixmap.scaled(int(pixmap.height()),int(pixmap.width()))
            label.setPixmap(pixmap)
            label.setGeometry(10,200,128,128)
            label.show()
            time.sleep(0.009)
            step = step + 2
                
                
            
                
            #fourierImage = self.convertArrayToImage(downRightFrameZeros)
                #self.showArrayImage(newimg,10,200)
            
            #threading.Thread(target=self.showArrayImage, args=(fsimg,10,200,),daemon = True).start()
                #self.showArrayImage(fsimg,10,200)
                #time.sleep(0.2)
            self.progress.setValue(i*(100/(value-1)))
        
            
            #fourierImage = self.convertArrayToImage(downRightFrameZeros)
            #self.showArrayImage(newimg,10,350)
            #threading.Thread(target=self.showArrayImage, args=(img,10,350,),daemon = True).start()
            
            
            #self.progress.setValue(i*(100/(value-1)))
       
    def upLeftFrameZeros(self,img,step,position):
        for i in range(step):
            for j in range(3):
                img[position][position+i][j] = 0
                img[(position+i)][position][j] = 0
        return img
        
    def downRightFrameZeros(self,img,step,position):
        for i in range(step):
            for j in range(len(img[0][0])):
                img[position][position-i][j] = 0
                img[(position-i)][position][j] = 0
        return img
        
    
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
