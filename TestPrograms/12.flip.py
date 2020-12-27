import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')

cv.imshow('Orignal', img)

# virtical flip code 0
virtical = cv.flip(img, 0)
cv.imshow("vertical", virtical)

#horizontal flip code 1
horizontal = cv.flip(img, 1)
cv.imshow("horizontal", horizontal)

#both code -1
both = cv.flip(img, -1)
cv.imshow('Both', both)
cv.waitKey(0)