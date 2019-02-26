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


class hiThread(QThread):

    def __init__(self,name):
        QThread.__init__(self)
        

    def __del__(self):
        self.wait() 
        
    
    def stopConverting(self):
        btn = QPushButton("Convert InOut",self)
        btn.setToolTip('This is an example button')
        btn.move(390,200)
        #print('this is the convert in outbutton function')
        btn.show()
        #threading.Thread(target=btn.clicked.connect,args=(self.changeConvertStatus,)).start()
        btn.clicked.connect(self.changeConvertStatus)
        
    def hello(self):
        while 1 :
            
            print('hello ')
            time.sleep(1)
            
    def run(self):
        self.hello()

    
        
        
 



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
        self.pause = 1
        self.changeConvertStatus()
        name = QFileDialog()
        imgPath = name.getOpenFileName(self,'open file','','Image files (*.jpg *.png *.jpeg)')
        self.checkImage(imgPath[0])
        
    
    def checkImage(self,path):
         im = Image.open(path)
         width, height = im.size
         if width > 128 or height > 128 :
             
             self.imgFalseMsg()
         else :
             self.path = path
             self.openImage(path)
             fourierImage = self.fourierTransform(path)
             #InverseImage = self.inverseFourier(fourierImage)
             
             #print('fourier type ',type(fourierImage))
             #InverseImage=np.fft.ifft(fourierImage)
             #print('invfourier type ',InverseImage[0][0])
             self.fimg = fourierImage
             modifiedImage = self.convertArrayToImage(fourierImage)
             self.showArrayImage(modifiedImage,362,50)
             
             #thread2 = threading.Thread(target=self.showArrayImage, args=(modifiedImage,50,150,),daemon = True).start()
             self.convertButton()
             self.stopConverting()
             self.pauseOp()
             self.resumeOp()
             #self.helloThread = hiThread('ahmed')
             #self.connect(self.helloThread, SIGNAL("finished()"), self.sc)
             #self.helloThread.stopConverting()
             #self.helloThread.start()
             #self.helloThread.hello('ahmed')
             #threading.Thread(target=self.stopConverting,args=()).start()
             #self.stopConverting()
             #threading.Thread(target=self.convertButton).start()
             #self.stop = self.stopConverting()
             #self.stop.show()
             #self.thread = QThread()
             #self.window = Window()
             #self.window.moveToThread(self.thread)
             #self.stop.clicked.connect(self.thread.start)
             #self.thread.started.connect(self.window.changeConvertStatus)
             
             
             
             
        
    def imgFalseMsg(self):
        #QMessageBox.about(self,'warning','invalid picture')
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')
 
        self.show()
        
        
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
        img = Image.open(path)
        
        arrayImage = self.convertImageToArray(img)
        fourierImage = np.fft.fft2(arrayImage,axes=(0,1))
        fourierImage = np.fft.fftshift(fourierImage)
        magnitude_spectrum = 20*np.log(np.abs(fourierImage))
        magnitude_spectrum = np.uint8(magnitude_spectrum)
        return magnitude_spectrum
    
    def HFT(self,path):
        img = Image.open(path).convert('L')
        arrayImage = self.convertImageToArray(img)
        fourierImage = np.fft.fft2(arrayImage,axes=(0,1))
        fourierImage = np.fft.fftshift(fourierImage)
        return fourierImage
    
    def inverseFourier(self,img):
        fourierImage = np.fft.fftshift(img)
        fourierImage = np.fft.ifft2(fourierImage)
        magnitude_spectrum =    (np.abs(fourierImage))
        magnitude_spectrum = np.uint8(magnitude_spectrum)
        return magnitude_spectrum
    
        
    
    def stopConverting(self):
        btn = QPushButton("Stop",self)
        btn.setToolTip('This is an example button')
        btn.move(200,250)
        #print('this is the convert in outbutton function')
        btn.show()
        #threading.Thread(target=btn.clicked.connect,args=(self.changeConvertStatus,)).start()
        btn.clicked.connect(self.changeConvertStatus)
        #return btn
        
    def changeConvertStatus(self):
        self.allowconvert = 0
        
        
        
        
    
    
    def convertButton(self):
        btn = QPushButton("Convert Image",self)
        btn.setToolTip('This is an example button')
        btn.move(252,10)
        print('this is the convert button function')
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
        
        
        
    def pauseOp(self):
        btn = QPushButton('Pause',self)
        btn.setToolTip('This is an example button')
        btn.move(252,350)
        print('this is the convert button function')
        btn.show()
        btn.clicked.connect(self.makePause)
        
        
    def makePause(self):
        self.pause =0
        
    
        
    def resumeOp(self):
        btn = QPushButton('Resume',self)
        btn.setToolTip('This is an example button')
        btn.move(150,350)
        print('this is the convert button function')
        btn.show()
        btn.clicked.connect(self.makeresume)
    
    def makeresume(self):
        self.pause = 1
        
    def startConverting(self):
        self.allowconvert = 1
        while 1:
            
            #self.stopConverting()
            #time.sleep(0.1)
            QApplication.processEvents()
            if self.allowconvert == 1:
                self.zerosFromOutToIn()
                self.zerosFromInToOut()
                print('you are allowed to convert')
                #time.sleep(1)
#            
            if(self.allowconvert == 0):
                print('stop is clicked')
                break
        
        
    def restoreOriginalImage(self) : 
        img = self.fimg
        mimg = self.convertArrayToImage(img)
        self.showArrayImage(mimg,10,200)
        
    def giveOriginalImage(self) : 
        img = self.fimg
        return img
        
    def zerosFromOutToIn(self):
        label = QLabel(self)
        label1 = QLabel(self)
        
        #while 1 :
        fourierFImage = self.HFT(self.path)
            
        #print(fourierImage)
        
        spinValue = self.spinb.value()
        
        value = 64
        step = 2
            #label = QLabel(self)
            #print('this is the mult ', 100/value)
        
        for i in range(64):
            while(self.pause ==0 ): 
                QApplication.processEvents()
                pass
            
            if self.allowconvert == 1:
            #print('first run')
                upFrameZeros = self.upFrameZeros(fourierFImage,i)
                downFrameZeros = self.downFrameZeros(upFrameZeros,-1-i)
                
                img = Image.fromarray(downFrameZeros.astype('uint8'))
                img.save('my.png')
                
                #qimage = ImageQt(fsimg)
                #pixmap = QPixmap.fromImage(qimage)
                if i % spinValue == 0 :
                    pixmap = QPixmap('my.png')
                    pixmap = pixmap.scaled(int(pixmap.height()),int(pixmap.width()))
                    label.setPixmap(pixmap)
                    label.setGeometry(362,200,128,128)
                    label.show()
                    print (i)
            
                QApplication.processEvents()
                
                imgi = self.inverseFourier(downFrameZeros)
                imgi = Image.fromarray(imgi)
                imgi.save('myi.png')
                if i % spinValue == 0 :
                    pixmap2 = QPixmap('myi.png')
                    pixmap2 = pixmap2.scaled(int(pixmap2.height()),int(pixmap2.width()))
                    label1.setPixmap(pixmap2)
                    label1.setGeometry(10,200,128,128)
                    label1.show()

            #time.sleep(0.009-spinValue*0.001)
                time.sleep(0.009)
                
                
            
            
                
            #fourierImage = self.convertArrayToImage(downRightFrameZeros)
                #self.showArrayImage(newimg,10,200)
            
            #threading.Thread(target=self.showArrayImage, args=(fsimg,10,200,),daemon = True).start()
                #self.showArrayImage(fsimg,10,200)
                #time.sleep(0.2)
                self.progress.setValue(i*(100/(value-1)))
        
        
        
        
                
        
#    def upFrameZeros(self,img,position):
#        #print('this is upFrameZeros')
#        for i in range(128):
#            for j in range(3):
#                img[position][i][j] = 0
#                img[i][position][j] = 0
#            
#        return img

    def upFrameZeros(self,img,position):
         
        #print('this is upFrameZeros')
        for i in range(128):
             img[position][i] = 0
             img[i][position]= 0
                    
        return img
    
#    def downFrameZeros(self,img,position):
#        #print('this is downFrameZeros')
#        for i in range(128):
#            for j in range(len(img[0][0])):
#                img[position][i][j] = 0
#                img[i][position][j] = 0
#            
#        return img
    
    def downFrameZeros(self,img,position):
        #print('this is downFrameZeros')
        for i in range(128):    
            img[position][i] = 0
            img[i][position] = 0
            
        return img



    
    def zerosFromInToOut(self):
        label = QLabel(self)
        label1 = QLabel(self)
    
        #while 1 :
        fourierFImage2 = self.HFT(self.path)
        #print(fourierImage)
        #value = self.spinb.value()
        #value = self.spinb.value()
        spinValue = self.spinb.value()
        value = 64
        step = 2
            #label = QLabel(self)
            #print('this is the mult ', 100/value)
        
        for i in range(64):
            while(self.pause ==0 ): 
                
                QApplication.processEvents()
                pass
           
            if self.allowconvert == 1:
            #print('first run')
                upLeftFrameZeros = self.upLeftFrameZeros(fourierFImage2,step,63-i)
                downRightFrameZeros = self.downRightFrameZeros(upLeftFrameZeros,step,64+i)
                img = Image.fromarray(downRightFrameZeros.astype('uint8'))
                img.save('my.png')
                
                #qimage = ImageQt(fsimg)
                #pixmap = QPixmap.fromImage(qimage)
                if i % spinValue == 0 :
                    pixmap = QPixmap('my.png')
                    pixmap = pixmap.scaled(int(pixmap.height()),int(pixmap.width()))
                    label.setPixmap(pixmap)
                    label.setGeometry(362,200,128,128)
                    label.show()
           
                
                QApplication.processEvents()    
                
                imgi = self.inverseFourier(downRightFrameZeros)
                imgi = Image.fromarray(imgi)
                imgi.save('myi.png')
                if i % spinValue == 0 :
                    pixmap2 = QPixmap('myi.png')
                    pixmap2 = pixmap2.scaled(int(pixmap2.height()),int(pixmap2.width()))
                    label1.setPixmap(pixmap2)
                    label1.setGeometry(10,200,128,128)
                    label1.show()
            
            #time.sleep(0.009-spinValue*0.001)
                time.sleep(0.009)
                step = step + 2
                
                #while(self.pause == 0):
                
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
       
#    def upLeftFrameZeros(self,img,step,position):
#        for i in range(step):
#            for j in range(3):
#                img[position][position+i][j] = 0
#                img[(position+i)][position][j] = 0
#        return img
            
            
    def upLeftFrameZeros(self,img,step,position):
        for i in range(step):
            img[position][position+i] = 0
            img[(position+i)][position] = 0
        return img
            
        
#    def downRightFrameZeros(self,img,step,position):
#        for i in range(step):
#            for j in range(len(img[0][0])):
#                img[position][position-i][j] = 0
#                img[(position-i)][position][j] = 0
#        return img
        
    def downRightFrameZeros(self,img,step,position):
        for i in range(step):
            img[position][position-i] = 0
            img[(position-i)][position] = 0
        return img
        
    
def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

main()        
