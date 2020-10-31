
import cv2 as cv
import sys
from matplotlib import pyplot as plt

objImg = cv.imread('forme3.png',cv.IMREAD_GRAYSCALE)

ret, thresh_forme3 = cv.threshold(objImg, 90, 255, cv.THRESH_BINARY)
cv.imshow("Forme 3", thresh_forme3)

key = cv.waitKey(0)
