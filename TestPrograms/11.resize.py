import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')

cv.imshow('Orignal', img)
height, width = img.shape[:2]
dimetion = (width, height)
resized = cv.resize(img, (500, 500))
cv.imshow('Smalled', resized)

enlarging = cv.resize(img, dimetion, interpolation= cv.INTER_CUBIC)
cv.imshow("enlarged", enlarging)
cv.waitKey(0)