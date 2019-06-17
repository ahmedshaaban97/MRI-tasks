# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:31:43 2019

@author: Mostafa Hisham
"""
import qimage2ndarray
from PIL import Image
import numpy as np
zero_array = np.zeros((20,20))
zero_array[5:15,5:15] = 140
#        zero_array[random.randint(30,70):random.randint(180,250),random.randint(30,70):random.randint(180,250)] = 120
        
mostafa = qimage2ndarray.array2qimage(zero_array)
mostafa.save("test.jpg")
