import time
from PIL import Image ,ImageEnhance , ImageFilter
from PIL.ImageQt import ImageQt
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap,QPen,QPainter,QColor, QBrush,QImage
from mostafa import Ui_MainWindow
import sys
import qimage2ndarray
import pyqtgraph as pg
np.set_printoptions(threshold=np.nan)
import cv2





class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_logan_2.clicked.connect(self.logan_clicked) 
        self.ui.lbl_phantom.hide()
        self.ui.lbl_phantom.mousePressEvent = self.getPixel
        self.ui.lbl_phantom.mouseDoubleClickEvent = self.draw_curve
        self.ui.lbl_phantom.mouseMoveEvent = self.brightness_control
        self.ui.btn_browse_2.clicked.connect(self.browse_clicked)
        self.ui.kspace.clicked.connect(self.generate_kspace)
        self.img = ''
        self.ratio=""
        self.size=""
        self.phantom_array=""
        self.t1_array=""
        self.t2_array=""
        self.pd_array=""
        self.ratio_cont=""
        self.xx=""
        self.yy=""
        self.i =""
        self.i =1
        self.br=""
        self.j=""
        self.j=1
        self.x = 0
        self.y = 0
    


 
    

    def draw_curve (self, event):
        x = event.pos().x()
        self.x = x
        label_width= self.ui.lbl_phantom.width()
        y = event.pos().y()
        self.y = y
        label_hight= self.ui.lbl_phantom.height()
        get_x = int ((x/label_width)*self.size)
        get_y = int ((y/label_hight)*self.size)
        print (self.phantom_array[get_x][get_y]) 
        t1=self.t1_array[get_x][get_y]        
        t2=self.t2_array[get_x][get_y]        
        unitVector=[[0],[0],[1]]
        theta=90
        alpha=10
        delta_t=500
        x_curve , y_curve , z_curve =self.draw_curves(unitVector, delta_t , t1 , t2 , theta , alpha)
        
        self.ui.graphicsView_2.plot(x_curve)
        self.ui.graphicsView_3.plot(y_curve)
#        img = self.frame(self.img)
#        img = Image.fromarray(img)
#        img = ImageQt(img)
#        img = QPixmap.fromImage(img)
#        #newImg = self.frame(self.img)
#        self.ui.lbl_kspace.setPixmap(img)
#        self.img = ImageQt(self.img)
#        self.img = QPixmap.fromImage(self.img)
        #self.img = Image.fromarray(self.img)
        #self.img = QImage(self.img)
        img = Image.fromarray(self.img).convert('RGB')
        img = np.array(img)
        img = self.frame(img)
        img = Image.fromarray(img).convert('RGB')
        qimage = ImageQt(img)
        pixmap = QPixmap.fromImage(qimage)
        self.ui.lbl_kspace.setPixmap(pixmap)

        

    def getPixel (self, event):
#        x=self.ui.lbl_phantom.height()
        self.xx = event.pos().x()
        self.yy = event.pos().y()
        
        
    def brightness_control (self, event):
#        x=self.ui.lbl_phantom.height()
        x = event.pos().x()
        y = event.pos().y()
        if self.xx in range (x-10 , x+10) and self.yy>y:
            self.i=self.i+self.br
        elif self.xx in range (x-10 , x+10) and self.yy<y:
            self.i=self.i-self.br
        elif self.yy in range (y-10 , y+10) and self.xx>x:
            self.j=self.j+10       
        elif self.yy in range (y-10 , y+10) and self.xx<x:
            self.j=self.j-10



#        ratio=()
#        print(y)
#        print(x)
        #print (x , y)
      
        
    def browse_clicked (self ):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.bmp *.png *.gif *.jpg)")
        self.path = fileName
        if fileName:
            if self.ui.CBox_size_2.currentText()== "128*128" :
                self.size=20
            elif self.ui.CBox_size_2.currentText()== "256*256" :
                self.size=256
            elif self.ui.CBox_size_2.currentText()== "512*512" :
                self.size=512
            self.phantom_choose (self.size , fileName)   
            
            
    def logan_clicked (self):

        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_3.clear()      
        
        
        self.ratio=self.i=1

        self.ratio_cont=self.j=1
        if self.ui.CBox_size_2.currentText()== "128*128" :
            self.size=20
            path="test.jpg"
            #self.img = cv2.imread("test.jpg",cv2.IMREAD_COLOR)
            #self.img = Image.open("test.jpg").convert('RGB')
            self.img = np.load('30PixelPhantom_images_arrays.npy')
            print('this is np array',np.array(self.img))
            self.br=.05
        elif self.ui.CBox_size_2.currentText()== "256*256" :
            self.size=256
            path="phantom256.png"
            self.br=.1
        elif self.ui.CBox_size_2.currentText()== "512*512" :
            self.size=512
            path="phantom512.png"
            self.br=.2

        self.phantom_choose (self.size , path)   
         
    def phantom_choose (self , lbl_size , path):
        self.ui.lbl_phantom.show()
        #array=self.convert_image_to_array(path)

        self.phantom_array,self.t1_array,self.t2_array=self.genrate_total_phantom (self.img)
        while 1:
            self.ratio=self.i

            self.ratio_cont=self.j

            if self.ui.comboBox_2.currentText()== "phantom" :
                array=self.phantom_array
            elif self.ui.comboBox_2.currentText()== "T1 effect" :
                array=self.t1_array
            elif self.ui.comboBox_2.currentText()== "T2 effect" :
                array=self.t2_array
            elif self.ui.comboBox_2.currentText()== "PD effect" :
                array=self.pd_array
                
                
                
            aaa=self.adding_image_to_lbl(array , self.ratio)
            self.ui.lbl_phantom.setPixmap(aaa)
            QApplication.processEvents()






#    def Set_T1(self,phantom_array):
#        t1_array=np.ones((self.size,self.size))
#        t2_array=np.ones((self.size,self.size))
#        phantom=np.ones((self.size,self.size))
#        Max_value= np.max (phantom_array)
#        Min_Value= np.min (phantom_array)
#        for x in range(0,self.size):
#            for y in range(0,self.size):
#                if (phantom_array[x][y] ==Max_value) :
#                    t1_array[x][y]=1090
#                    t2_array[x][y]=1
#                    phantom[x][y]=phantom_array[x][y]
#                else:
#                    if (phantom_array[x][y]==Min_Value):
#                        t1_array[x][y]=1
#                        t2_array[x][y]=1090
#                        phantom[x][y]=phantom_array[x][y]
#
#
#                    else:
#                        t1_array[x][y]=int(1+(phantom_array[x][y]*1090)/Max_value)
#                        t2_array[x][y]=int(1090-(phantom_array[x][y]*1090)/Max_value)
#                        phantom[x][y]=phantom_array[x][y]
#
#        return phantom,t1_array , t2_array 




        

    def genrate_total_phantom (self , phantom_array ):
        t1_array = np.ones((self.size,self.size))
        t2_array = np.ones((self.size,self.size))
        pd_array = np.ones((self.size,self.size))
        phantom_arrray = np.ones((self.size,self.size))
        for i in range (0 , self.size) :
            for j in range (0,self.size):
                if phantom_array[i][j]< 255 and phantom_array[i][j] >80 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=np.abs(int(1+ (phantom_array[i][j]*(2))))
                    t2_array[i][j]=np.abs(1+(256-t1_array[i][j]))
                    pd_array[i][j]=0
                elif phantom_array[i][j]< 100 and phantom_array[i][j] >20 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=np.abs(int (1+(phantom_array[i][j]*3)))
                    t2_array[i][j]=np.abs(1+(256-t1_array[i][j]))
                    pd_array[i][j]=100

                else :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=60+(phantom_array[i][j])
                    t2_array[i][j]=40+(phantom_array[i][j])
                    pd_array[i][j]=200
            QApplication.processEvents()
            aaa=self.adding_image_to_lbl(phantom_arrray , self.ratio)
            self.ui.lbl_phantom.setPixmap(aaa)
        
        
        return phantom_array,t1_array,t2_array

    
    def convert_image_to_array(self , path):
        img=Image.open(path).convert('L')
        img_array = np.asarray(img)
        np.save("30PixelPhantom_images_arrays", img_array)
        return img_array


    def adding_image_to_lbl(self , aarray , bright_ratio):
        mostafa = qimage2ndarray.array2qimage(np.absolute(aarray))
        mostafa.save("output.jpg")
        
        im = Image.open("output.jpg")
        xxxx=self.change_contrast(im , self.ratio_cont)
        xxxx.save("output.jpg")
        im = Image.open("output.jpg")
        enhancer = ImageEnhance.Brightness(im)
        enhanced_im = enhancer.enhance(bright_ratio)
        enhanced_im.save("enhanced.sample5.png")
        im = Image.open("enhanced.sample5.png")
        pixmap = QPixmap("enhanced.sample5.png")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        return pixmap


    def change_contrast(self,img, level):
        factor = (259 * (level + 255)) / (255 * (259 - level))
        def contrast(c):
            value = 128 + factor * (c - 128)
            return max(0, min(255, value))
        return img.point(contrast)

        
    def draw_curves(self,unitVector, delta , t1 , t2 , theta , alpha):
        x_curve=[]
        y_curve=[]
        z_curve=[]
        theta = ((theta * 22/7 )/180)
        rotationx = [[1,0,0],[0,np.cos(theta),np.sin(theta)],[0,-np.sin(theta),np.cos(theta)]]
        rotationxy = [[np.cos(alpha),-np.sin(alpha),0],[-(np.sin(alpha)),np.cos(alpha),0],[0,0,1]]
        for delta_t in range (delta):    
            decayRecoveryArray = [[np.exp(-delta_t/t2),0,0], [0,np.exp(-delta_t/t2),0],[0,0,np.exp(-delta_t/t1)]]
            finaldrArray = [[0],[0],[(1-(np.exp(-delta_t/t1)))]]
            rotatedVector = np.matmul(rotationx,unitVector)
            rotatedVector = np.matmul(rotationxy,rotatedVector)
            rotatedVector = np.matmul(decayRecoveryArray,rotatedVector)
            rotatedVector = finaldrArray+rotatedVector
            x_curve.extend(rotatedVector[0])
            y_curve.extend(rotatedVector[1])
            z_curve.extend(rotatedVector[2])
        return x_curve , y_curve , z_curve
    
    
    def generate_kspace (self):
        unitVector=[[0],[0],[1]]
        theta=45
        alpha=10
        tr=self.ui.SP_TE.value()
        te=self.ui.SP_TR.value()
        array=self.creare_Kspace(unitVector, te , tr, theta , alpha)
        aaa=self.adding_image_to_lbl(array , 1)
        self.ui.lbl_kspace.setPixmap(aaa)

    
    
    
    def creare_Kspace(self,unitVector, te ,tr ,  theta , alpha):
        
        t2=((self.t1_array)+1000)
        t1=(self.t2_array+10)

        k_space=np.zeros((self.size,self.size), dtype = np.complex)
        
        signal = np.ones((self.size,self.size))
        
        for kspacerow in range(self.size):
            

            signal = signal * np.exp(-te/t2)
            
            for kspacecol in range(self.size):
                GX= 2*np.pi*kspacerow / self.size
                GY= 2*np.pi*kspacecol / self.size
    
                for i in range(self.size):
                    for j in range(self.size):
                        total_theta=(GX*i+GY*j)
                        k_space[kspacerow, kspacecol] += signal[i,j]*np.exp(-1j*total_theta)
                        QApplication.processEvents()

            signal = 1 - np.exp(-tr/t1)
        test1 = np.absolute(np.fft.ifft2(k_space))
        maxi=np.max(test1)
        mini=np.min(test1)
        test1=((test1-mini))*(255/(maxi-mini))
        return test1





#    def frame(self,image):
#        QApplication.processEvents()
#        self.result=QPixmap(image)
#        self.painterInstance = QPainter(self.result)
#        self.painterInstance.begin(self)  
#        self.penRectangle =QPen(QtCore.Qt.red)
#        self.penRectangle.setWidth(1)
#        self.penPoint =QPen(QtCore.Qt.blue)
#        self.penPoint.setWidth(1)
#        self.painterInstance.setPen(self.penPoint)
#        self.painterInstance.drawRect(self.x,self.y,1,1)
#        self.painterInstance.setPen(self.penRectangle)
#        self.painterInstance.drawRect(self.x-5,self.y-5,10,10)
#        self.painterInstance.end()
#        #result=self.result.scaled(int(self.result.height()), int(self.result.width()),QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation) #scale 3la elabel
#        self.ui.lbl_kspace.setPixmap(self.result)
#        self.painterInstance.end()
#        QApplication.processEvents()
#        print('end of highlight')
#        return result
#         cv2.rectangle(image,(self.x-1,self.x+1),(self.y-1,self.y+1),(0,255,0),1)
#        return image
#       
        

    def frame(self,image):
#        qp = QPainter(image)
#       # qp.begin(self)
#        #col = QColor(0, 0, 0)
##        #col.setNamedColor('#d4d4d4')
##        qp.setPen(col)
##
##        qp.setBrush(QColor(200, 0, 0))
#        #qp.drawRect(10, 15, 90, 60)
#
#        #qp.setBrush(QColor(255, 80, 0, 160))
#        qp.drawRect(130, 15, 90, 60)
#
#        #qp.setBrush(QColor(25, 0, 90, 200))
#        #qp.drawRect(250, 15, 90, 60)
#        qimage = ImageQt(qp)
#        pixmap = QPixmap.fromImage(qimage)
#        self.ui.lbl_kspace.setPixmap(pixmap)
#        qp.end()

         cv2.rectangle(image,(30,50),(30,50),(0,255,0),1)
         return image


def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
