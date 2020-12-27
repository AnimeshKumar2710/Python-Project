import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')
img= cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv.imshow('Resized', img)
blank = np.zeros((img.shape[1], img.shape[0]), dtype= 'uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
cv.imshow('masked', mask)

#masking
masked = cv.bitwise_and(img, img, mask= mask)

cv.imshow('Masked', masked)
cv.waitKey(0)