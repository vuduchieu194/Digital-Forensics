import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

objImg = cv.imread('cadastre1.png',cv.IMREAD_GRAYSCALE)

ret, thresh= cv.threshold(objImg, 120, 255, cv.THRESH_BINARY) 
ret, thresh_otsu = cv.threshold(objImg, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("Arbitrary", thresh)
cv.imshow("Otsu", thresh_otsu)


titles = ['Original','Arbitrary','Otsu']
images = [objImg,thresh,thresh_otsu]
for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

