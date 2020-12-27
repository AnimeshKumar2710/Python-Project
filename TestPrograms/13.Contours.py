import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')

cv.imshow("Img", img)

blank = np.zeros(img.shape, dtype= 'uint8')

#blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blur= img
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(gray, 100, 200)
cv.imshow('Canny', canny)

contour, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contour), "number of contours")

cv.drawContours(blank, contour, -1, (255, 255, 255))
cv.imshow('Contour', blank)

cv.waitKey(0)