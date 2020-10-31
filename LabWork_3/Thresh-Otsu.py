import cv2 as cv
import sys

forme1 = cv.imread('forme1.png',cv.IMREAD_GRAYSCALE)
lena = cv.imread('lena.png',cv.IMREAD_GRAYSCALE)
forme3 = cv.imread('forme3.png',cv.IMREAD_GRAYSCALE)

ret, thresh_forme1 = cv.threshold(forme1, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret, thresh_lena = cv.threshold(lena, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret, thresh_forme3 = cv.threshold(forme3, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)


cv.imshow("Otsu-Forme 1", thresh_forme1)
cv.imshow("Otsu-Lena", thresh_lena)
cv.imshow("Otsu-Forme 3", thresh_forme3)

key = cv.waitKey(0)

