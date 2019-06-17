import time
from PIL import Image ,ImageEnhance , ImageFilter
import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog , QMessageBox,QApplication
from PyQt5.QtGui import QPixmap , QPainter, QPen
from mostafa import Ui_MainWindow
import sys
import qimage2ndarray
import pyqtgraph as pg
np.set_printoptions(threshold=np.nan)





class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_logan_2.clicked.connect(self.logan_clicked) 
        self.ui.lbl_phantom.mousePressEvent = self.getPixel
        self.ui.lbl_phantom.mouseDoubleClickEvent = self.draw_curve
        self.ui.lbl_phantom.mouseMoveEvent = self.brightness_control
        self.ui.btn_browse_2.clicked.connect(self.browse_clicked)
        self.ui.kspace.clicked.connect(self.generate_kspace)
        self.ui.pushButton.clicked.connect(self.image_of_Kspace)
        self.ui.pushButton.setEnabled(False)
        self.result = ''
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
        self.ks_image=""
        self.aaa=""


 
    

    def draw_curve (self, event):
        x = event.pos().x()
        label_width= self.ui.lbl_phantom.width()
        y = event.pos().y()
        label_hight= self.ui.lbl_phantom.height()
        get_x = int ((x/label_width)*self.size)
        get_y = int ((y/label_hight)*self.size)
        t1=self.t1_array[get_x][get_y]        
        t2=self.t2_array[get_x][get_y]        
        unitVector=[[0],[0],[1]]
        theta=90
        alpha=10
        delta_t=500
        x_curve , y_curve , z_curve =self.draw_curves(unitVector, delta_t , t1 , t2 , theta , alpha)
        
        self.ui.graphicsView_2.plot(x_curve)
        self.ui.graphicsView_3.plot(y_curve)
        img = self.draw(get_x,get_y,self.aaa)
        self.ui.lbl_phantom.setPixmap(img)
        
        







        
        



        

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
        print (self.i)
        self.ratio=self.i
        self.ratio_cont=self.j
        array_phantom=self.phantom_array
        self.aaa=self.adding_image_to_lbl(array_phantom,1)
        self.ui.lbl_phantom.setPixmap(self.aaa)

      


        
    def browse_clicked (self ):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open file", "", "Image files (*.bmp *.png *.gif *.jpg)")
        self.path = fileName
        if fileName:
            
            self.ui.graphicsView_2.clear()
            self.ui.graphicsView_3.clear()      
            self.ui.pushButton.setEnabled(False)
            self.br=.1
            self.ratio=self.i=1
            self.ratio_cont=self.j=1
            array=self.convert_image_to_array(fileName)
            self.size=len (array)
            self.phantom_choose (self.size , fileName)   
            
            
    def logan_clicked (self):

        self.ui.graphicsView_2.clear()
        self.ui.graphicsView_3.clear()      
        self.ui.pushButton.setEnabled(False)
        self.ratio=self.i=1
        self.ratio_cont=self.j=1
        
        
        
        if self.ui.CBox_size_2.currentText()== "20*20" :
            self.size=20
            p=self.phantom (n = 20)	
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom20.jpg")
            path="phantom20.png"
            self.br=.01
            
        elif self.ui.CBox_size_2.currentText()== "32*32" :
            self.size=32
            p=self.phantom (n = 32)	
            p=(p)*200
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom32.jbg")
            path="phantom32.png"
            self.br=.02
            
        if self.ui.CBox_size_2.currentText()== "64*64" :
            self.size=64
            p=self.phantom (n = 64)	
            p=(p)*200
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom64.jpg")
            path="phantom64.png"
            self.br=.03
            
        elif self.ui.CBox_size_2.currentText()== "128*128" :
            self.size=128
            p=self.phantom (n = 128)	
            p=(p)*200
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom128.jpg")
            path="phantom128.png"
            self.br=.05
        elif self.ui.CBox_size_2.currentText()== "256*256" :
            self.size=256
            p=self.phantom (n = 256)	
            #p=(p)*200
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom256.jpg")
            path="phantom256.png"     
            self.br=.1
        elif self.ui.CBox_size_2.currentText()== "512*512" :
            self.size=512
            p=self.phantom (n = 512)	
            #p=(p)*200
            mostafa = qimage2ndarray.array2qimage(np.absolute(p))
            mostafa.save("phantom512.jpg")
            path="phantom256.png"
            self.br=.2

        self.phantom_choose (self.size , path)   
         
    def phantom_choose (self , lbl_size , path):
        array=self.convert_image_to_array(path)
        self.phantom_array,self.t1_array,self.t2_array=self.genrate_total_phantom (array)
#        while 1:
#            self.ratio=self.i
#            self.ratio_cont=self.j
#
#            if self.ui.comboBox_2.currentText()== "phantom" :
#                array_phantom=self.phantom_array
#                aaa=self.adding_image_to_lbl(array_phantom , self.ratio)
#                self.ui.lbl_phantom.setPixmap(aaa)
#                
#                
#                
#            elif self.ui.comboBox_2.currentText()== "T1 effect" :
#                array_t1=self.t1_array
#                aaa=self.adding_image_to_lbl(array_t1 , self.ratio)
#                self.ui.lbl_phantom.setPixmap(aaa)                
#            elif self.ui.comboBox_2.currentText()== "T2 effect" :
#                array_t2=self.t2_array
#                aaa=self.adding_image_to_lbl(array_t2 , self.ratio)
#                self.ui.lbl_phantom.setPixmap(aaa) 
#            QApplication.processEvents()






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
        #pd_array = np.ones((self.size,self.size))
        phantom_arrray = np.ones((self.size,self.size))
        for i in range (0 , self.size) :
            for j in range (0,self.size):
                if phantom_array[i][j]< 255 and phantom_array[i][j] >80 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=np.abs(int(1+ (phantom_array[i][j]*(2))))
                    t2_array[i][j]=np.abs(1+(256-t1_array[i][j]))
                    #pd_array[i][j]=0
                elif phantom_array[i][j]< 100 and phantom_array[i][j] >20 :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=np.abs(int (1+(phantom_array[i][j]*3)))
                    t2_array[i][j]=np.abs(1+(256-t1_array[i][j]))
                    #pd_array[i][j]=100

                else :
                    phantom_arrray[i][j]=phantom_array[i][j]
                    t1_array[i][j]=60+(phantom_array[i][j])
                    t2_array[i][j]=40+(phantom_array[i][j])
                    #pd_array[i][j]=200
            QApplication.processEvents()
            aaa=self.adding_image_to_lbl(phantom_arrray , self.ratio)
            self.ui.lbl_phantom.setPixmap(aaa)
        

        return phantom_array,t1_array,t2_array

    
    def convert_image_to_array(self , path):
        img=Image.open(path).convert('L')
        img_array = np.asarray(img)
        return img_array


    def adding_image_to_lbl(self , aarray , bright_ratio):
        mostafa = qimage2ndarray.array2qimage(np.absolute(aarray))
        mostafa.save("output1.jpg")
        im = Image.open("output1.jpg")
        xxxx=self.change_contrast(im , self.ratio_cont)
        enhanced_im=self.change_brightness(xxxx, self.ratio)
        enhanced_im.save("enhanced.sample5.png")
        pixmap = QPixmap("enhanced.sample5.png")
        pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
        self.pixmap=pixmap
        return self.pixmap


    def change_contrast(self,img, level):
        factor = (259 * (level + 255)) / (255 * (259 - level))
        def contrast(c):
            value = 128 + factor * (c - 128)
            return max(0, min(255, value))
        return img.point(contrast)
    
    def change_brightness(self,img, level):
        enhancer = ImageEnhance.Brightness(img)
        enhanced_im = enhancer.enhance(level)
        return enhanced_im

        
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
        self.ui.lbl_kspace.clear()      
        unitVector=[[0],[0],[1]]
        theta=self.ui.SP_theta.value()
        tr=self.ui.SP_TE.value()
        te=self.ui.SP_TR.value()
        k_space , self.ks_image =self.creare_Kspace(unitVector, te , tr, theta )
        aaa=self.adding_image_to_lbl(k_space , 1)
        self.ui.lbl_kspace.setPixmap(aaa)

    
    
    
    def creare_Kspace(self,unitVector, te ,tr ,  theta ):
        
        t2=((self.t1_array)+1000)
        t1=(self.t2_array+10)

        k_space=np.zeros((self.size,self.size), dtype = np.complex)
        print('theta= ',theta)
        
        signal = np.ones((self.size,self.size))
        signal = signal * np.sin(theta * np.pi / 180. )
        
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
#            signal = np.ones((self.size,self.size))
#            signal = signal * np.sin(theta * np.pi / 180. )
        K_S=k_space
        maxi=np.max(K_S)
        mini=np.min(K_S)
        K_S=((K_S-mini))*(255/(maxi-mini))    
            
            
        test1 = np.absolute(np.fft.ifft2(k_space))
        maxi=np.max(test1)
        mini=np.min(test1)
        test1=((test1-mini))*(255/(maxi-mini))
        self.ui.pushButton.setEnabled(True)
        return K_S , test1
    
    
    def image_of_Kspace(self):
        aaa=self.adding_image_to_lbl(self.ks_image , 1)
        self.ui.lbl_kspace.setPixmap(aaa)

  
    
    
    
    
    
    
    
    
    
    

    def phantom (self,n = 100, p_type = 'Modified Shepp-Logan', ellipses = None):	
    	if (ellipses is None):
    		ellipses = self._select_phantom (p_type)
    	elif (np.size (ellipses, 1) != 6):
    		raise AssertionError ("Wrong number of columns in user phantom")
    	
    	# Blank image
    	p = np.zeros ((n, n))
    
    	# Create the pixel grid
    	ygrid, xgrid = np.mgrid[-1:1:(1j*n), -1:1:(1j*n)]
    
    	for ellip in ellipses:
    		I   = ellip [0]
    		a2  = ellip [1]**2
    		b2  = ellip [2]**2
    		x0  = ellip [3]
    		y0  = ellip [4]
    		phi = ellip [5] * np.pi / 180  # Rotation angle in radians
    		
    		# Create the offset x and y values for the grid
    		x = xgrid - x0
    		y = ygrid - y0
    		
    		cos_p = np.cos (phi) 
    		sin_p = np.sin (phi)
    		
    		# Find the pixels within the ellipse
    		locs = (((x * cos_p + y * sin_p)**2) / a2 
              + ((y * cos_p - x * sin_p)**2) / b2) <= 1
    		
    		# Add the ellipse intensity to those pixels
    		p [locs] += I
            

    	return p
    
    
    def _select_phantom (self,name):
    	if (name.lower () == 'modified shepp-logan'):
    		e = self._mod_shepp_logan ()
    	else:
    		raise ValueError ("Unknown phantom type: %s" % name)
    	
    	return e
    def _mod_shepp_logan (self):
    	#  Modified version of Shepp & Logan's head phantom, 
    	#  adjusted to improve contrast.  Taken from Toft.
    	return [[   1,   .69,   .92,    0,      0,   0],
    	        [-.80, .6624, .8740,    0, -.0184,   0],
    	        [-.20, .1100, .3100,  .22,      0, -18],
    	        [-.20, .1600, .4100, -.22,      0,  18],
    	        [ .10, .2100, .2500,    0,    .35,   0],
    	        [ .10, .0460, .0460,    0,     .1,   0],
    	        [ .10, .0460, .0460,    0,    -.1,   0],
    	        [ .10, .0460, .0230, -.08,  -.605,   0],
    	        [ .10, .0230, .0230,    0,  -.606,   0],
    	        [ .10, .0230, .0460,  .06,  -.605,   0]]
    
    






    def draw (self,x,y,fullImage):
        #fullImage = QPixmap(self.myPath)
        self.painterInstance = QPainter(fullImage)
        self.painterInstance.begin(self)
        self.penRectangle = QPen(QtCore.Qt.red)
        self.penRectangle.setWidth(1)
        #self.penPoint = QPen(QtCore.Qt.black)
        #self.penPoint.setWidth(1)
        #self.painterInstance.setPen(self.penPoint)
        #self.painterInstance.drawRect(x,y,1,1)
        self.painterInstance.setPen(self.penRectangle)
        self.painterInstance.drawRect(x-0,y-0,1,1)
        self.painterInstance.end()
        #result = fullImage.scaled(self.ui.lbl_phantom.width(),self.ui.lbl_phantom.height())
        #result.save('alllllla.png')
        #self.ui.lbl_phantom.setPixmap(fullImage)
        self.painterInstance.end()
        return(fullImage)











def main(): 
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
