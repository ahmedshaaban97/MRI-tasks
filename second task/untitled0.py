import sys
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget , QApplication,QPushButton,QInputDialog,QSpinBox,QFileDialog,QProgressBar,QMessageBox
from PyQt5.QtCore import QSize,pyqtSlot,QTimer,QThread
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import numpy as np
from numpy import array
from PIL.ImageQt import ImageQt
import time
import threading
from scipy.fftpack import ifft
import cv2


#class hiThread(QThread):
#
#    def __init__(self,name):
#        QThread.__init__(self)
#        
#
#    def __del__(self):
#        self.wait() 
#        
#    
#    def stopConverting(self):
#        btn = QPushButton("Convert InOut",self)
#        btn.setToolTip('This is an example button')
#        btn.move(390,200)
#        #print('this is the convert in outbutton function')
#        btn.show()
#        #threading.Thread(target=btn.clicked.connect,args=(self.changeConvertStatus,)).start()
#        btn.clicked.connect(self.changeConvertStatus)
#        
#    def hello(self):
#        while 1 :
#            
#            print('hello ')
#            time.sleep(1)
#            
#    def run(self):
#        self.hello()
#
#    
        
        
 



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,500,500,500)
        self.spinb = ''
        self.fimg = ''
        self.pause = 0
        self.allowconvert = 0
        self.path = 'this is empyt pass'
        self.progress = 0
        self.layout()
        
        #self.threadClass = ThreadClass()
        #self.threadClass.start()
        
        
    def layout(self):
        self.label()
        self.home()
        self.spinb = self.spinBox()
        self.show()
        
        
    def label(self):
        li = QLabel(self)
        li.setText('Conversion Speed')
        li.setGeometry(145,100,120,20)
        #li.move(145,100)
        
    def label1(self):
        li1 = QLabel(self)
        return li1
        
        
    def label2(self):
        li2 = QLabel(self)
        return li2
        
        
    
    def home(self):
        btn = QPushButton("Select image",self)
        btn.setToolTip('This is an example button')
        btn.clicked.connect(self.on_click)
        btn.move(140,10)
        

        
    def spinBox(self):
        sbox = QSpinBox(self)
        sbox.setValue(1)
        sbox.move(255,100)
        sbox.setMaximum(64)
        return sbox
        
        
    def progressBar(self):
        progressBar = QProgressBar(self)
        progressBar.setGeometry(5,380,500,20)
        progressBar.setValue(0)
        
        return progressBar
        
    @pyqtSlot()
    def on_click(self):
        name = QFileDialog()
        imgPath = name.getOpenFileName(self,'open file','','Image files (*.jpg *.png *.jpeg)')
        self.checkImage(imgPath[0])
        
    
    def checkImage(self,path):
         im = Image.open(path)
         width, height = im.size
         self.path = path
         img = cv2.imread(path)
         img = Image.fromarray(img)
         img2 = cv2.imread('test2.jpg')
         img2 = Image.fromarray(img2)
         #print(type(img))
         self.showArrayImage(self.label1(),img,10,10)
         
             
        
    def showArrayImage(self,label,img,x,y):
        qimage = ImageQt(img)
        pixmap = QPixmap.fromImage(qimage)
        label.setPixmap(pixmap)
        label.setGeometry(x,y,128,128)
        label.mousePressEvent = self.getPixel
        label.show()
       
       
    def getPixel (self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(x,y)
       
    def conver3dTo2dArray(arr,index):
       arr2 = np.array(np.zeros([len(arr),len(arr[0])]))
       for i in range(len(arr2)):
           for j in range(len(arr2[0])):
               arr2[i][j] = arr[i][j][index]
       return arr2 
            
    
    
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
