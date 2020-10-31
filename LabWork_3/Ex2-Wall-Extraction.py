import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

objImg = cv.imread('cadastre2.png',cv.IMREAD_GRAYSCALE)

ret,obj = cv.threshold(objImg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

ret,thickObj = cv.threshold(objImg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
thickObj = cv.dilate(thickObj,kernel,iterations = 1)

thinObj2 = obj - thickObj
ret,thinObj2 = cv.threshold(thinObj2,0,255,cv.THRESH_BINARY_INV)

titles = ['Original','obj','thickest','thinnest']
images = [objImg,obj,thickObj,thinObj2]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
