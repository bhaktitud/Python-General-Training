# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 23:49:54 2018

@author: Bhakti
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image

src_path = "D:\Data Novan\Tutorials\Python General Training\python"

def get_string(img_path):
    img = cv2.imread(img_path)
    
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    
    cv2.imwrite(src_path + "removed_noise.png", img)
    
    cv2.imwrite(src_path + "thres.png", img)
    
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))
    
    return result
    

print('--- Start recoqnize text from image ---')
print(get_string(src_path + "txt.png"))

print("----- Done -----")