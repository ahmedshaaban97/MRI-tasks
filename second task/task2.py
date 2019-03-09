import sys
from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget , QApplication,QPushButton,QInputDialog,QSpinBox,QFileDialog,QProgressBar,QMessageBox,QGraphicsView,QSizePolicy,QComboBox
from PyQt5.QtCore import QSize,pyqtSlot,QTimer,QThread,QRect    
from PyQt5.QtGui import QIcon, QPixmap
from PIL import Image
import numpy as np
from numpy import array
from PIL.ImageQt import ImageQt
import time
import threading
from scipy.fftpack import ifft
import cv2
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=50, data = []):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.data = data
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        
        ax = self.figure.add_subplot(111)
        ax.plot(self.data, 'r-')
        self.draw()





class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Converter")
        self.setGeometry(500,500,500,500)
        self.imgSize = 0
        self.path = 'this is empyt pass'
        self.currentPhantom = []
        self.numOfPlots = 0
        self.show = 1
        #self.label1 = QLabel(self)
        self.layout()
        
        
        
    def layout(self):
        #self.label()
        self.browse()
        #self.spinb = self.spinBox()
        self.sizeBox = self.imageSizeCombobox()
        print(type(self.sizeBox.currentText()))
        self.typeBox = self.imageTypeCombobox()
        print(self.typeBox.currentText())
        
        self.showMaximized()
        
        
    def imageSizeCombobox(self):
        sizeBox = QComboBox(self)
        sizeBox.setObjectName(("comboBox"))
        sizeBox.setGeometry(QRect(5, 150, 100, 50))
        sizeBox.addItem("128")
        sizeBox.addItem("256")
        sizeBox.addItem("512")
        return sizeBox
        
    def imageTypeCombobox(self):
        sizeBox = QComboBox(self)
        sizeBox.setObjectName(("comboBox"))
        sizeBox.setGeometry(QRect(5, 250, 100, 50))
        sizeBox.addItem("T1")
        sizeBox.addItem("T2")
        sizeBox.addItem("ProtonDencity")
        sizeBox.addItem("PixelIntencity")
        return sizeBox
        
        
#    def label(self):
#        li = QLabel(self)
#        li.setText('Conversion Speed')
#        li.setGeometry(145,100,120,20)
#        #li.move(145,100)
        
    def label(self):
        li1 = QLabel(self)
        return li1
        
        
    def label2(self):
        li2 = QLabel(self)
        return li2
        
        
    
    def browse(self):
        btn = QPushButton("Select image",self)
        btn.setToolTip('This is an example button')
        btn.clicked.connect(self.on_click)
        btn.move(5,10)
        
        
    
        

        
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
        self.show = 0
        name = QFileDialog()
        imgPath = name.getOpenFileName(self,'open file','','Image files (*.jpg *.png *.jpeg)')
        self.checkImage(imgPath[0])
        
    
    def checkImage(self,path):
         self.show = 1
         self.numOfPlots = 0
         self.imgSize = self.sizeBox.currentText()
         self.imgType = self.typeBox.currentText()
         self.label1 = self.label()
         img = Image.open(path).convert('L')
         arrayImage = self.convertImageToArray(img)
         phantonArray = self.genrate_total_phantom(arrayImage)
         self.currentPhantom = phantonArray
         
         im = Image.open(path)
         width, height = im.size
         self.path = path
         #img = cv2.imread(path)
         while self.show == 1 :
             
             self.imgSize = self.sizeBox.currentText()
             self.imgType = self.typeBox.currentText()
             index  = self.getPropertyIndex(self.imgType)
             
             indexedArray = self.conver3dTo2dArray(phantonArray,index)
             #print('this is index array', indexedArray)
             imgArray = Image.fromarray(indexedArray)
             QApplication.processEvents()
         #print(type(img))
             self.showArrayImage(self.label1,imgArray,200,200)
             QApplication.processEvents()
         
    def showArrayImage(self,label,img,x,y):
        #label = QLabel(self)
        qimage = ImageQt(img)
        pixmap = QPixmap.fromImage(qimage)
        label.setPixmap(pixmap)
        label.setGeometry(128,10,int(self.imgSize),int(self.imgSize))
        label.mousePressEvent = self.getPixel
        label.show()
        
        
        
    def clearLabel(self):
        print('clear called')
        self.label1.setVisible(False)
             
    def getPropertyIndex(self,imgType):
        if imgType == 'T1':
            return 0
        elif imgType == 'T2':
            return 1 
        elif imgType == 'ProtonDencity':
            return 2 
        else:
            return 3
        
#    def showArrayImage(self,label,img,x,y):
#        qimage = ImageQt(img)
#        pixmap = QPixmap.fromImage(qimage)
#        label.setPixmap(pixmap)
#        label.setGeometry(x,y,256,256)
#        label.mousePressEvent = self.getPixel
#        label.show()
       
    def convertImageToArray(self,img):
         arr = np.asarray(img, np.uint8)
         #print('this is image pixel function')
         return arr
       
    def getPixel (self, event):
        x = event.pos().x()
        y = event.pos().y()
        t1,t2 = self.getPhantomPixelData(y,x)
        print(x,y)
        self.plot(t1,t2)
        
    def getPhantomPixelData(self,row,col):
        t1 = self.currentPhantom[row][col][0]
        t2 = self.currentPhantom[row][col][1]
        return t1,t2
       
    def conver3dTo2dArray(self,arr,index):
       arr2 = np.array(np.zeros([len(arr),len(arr[0])]))
       for i in range(len(arr2)):
           for j in range(len(arr2[0])):
               arr2[i][j] = arr[i][j][index]
       arr2N = np.uint8(arr2)
       return arr2N 
   
    
    
    def plot(self,t1,t2):
        if(self.numOfPlots >4):
            return
        else:
            t1CurveData = np.exp(range(int(t1)))
            t2CurveData = np.exp(range(int(-1*t2)))
            m = PlotCanvas(self, width=4, height=4, data = t1CurveData)
            m.move(400,(10+self.numOfPlots * 200))
            m.show()
            m2 = PlotCanvas(self, width=4, height=4, data = t2CurveData)
            m2.move(700,(10+self.numOfPlots * 200))
            m2.show()
            self.numOfPlots = self.numOfPlots + 1
        
        
        
    def genrate_total_phantom (self , phantom_array ):
        print('this is phantom array type ',phantom_array[0][0])
        t1_array = np.ones((int(self.imgSize),int(self.imgSize)))
        t2_array = np.ones((int(self.imgSize),int(self.imgSize)))
        pd_array = np.ones((int(self.imgSize),int(self.imgSize)))
        for i in range (0 , int(self.imgSize)) :
            for j in range (0,int(self.imgSize)):
                if phantom_array[i][j]< int(self.imgSize) and phantom_array[i][j] >80 :
                    t1_array[i][j]=int (phantom_array[i][j]*(.2))
                    t2_array[i][j]=256-t1_array[i][j]
                    pd_array[i][j]=0

                elif phantom_array[i][j]< 100 and phantom_array[i][j] >20 :
                    t1_array[i][j]=int (phantom_array[i][j]*3)
                    t2_array[i][j]=256-t1_array[i][j]
                    pd_array[i][j]=100

                else :
                    t1_array[i][j]=60+(phantom_array[i][j])
                    t2_array[i][j]=40+(phantom_array[i][j])
                    pd_array[i][j]=200
                QApplication.processEvents()
            QApplication.processEvents()
        #return phantom_array,t1_array,t2_array,pd_array
        phantomArray = self.convert2dArraysTo3d(phantom_array,t1_array,t2_array,pd_array)
        return phantomArray

            
    def convert2dArraysTo3d(self,pixelsArray,t1Array,t2Array,pdArray):
        phantomArray = np.array(np.zeros([int(self.imgSize),int(self.imgSize),4]))
        for i in range(int(self.imgSize)):
            for j in range(int(self.imgSize)):
                phantomArray[i][j][0] = t1Array[i][j] 
                phantomArray[i][j][1] = t2Array[i][j]
                phantomArray[i][j][2] = pdArray[i][j]
                phantomArray[i][j][3] = pixelsArray[i][j]
                QApplication.processEvents()
            QApplication.processEvents()
        return phantomArray
                
    
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
