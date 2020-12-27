import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')

cv.imshow('Orignal', img)

def translate(img, x, y):
    Matrix = np.float32([[1, 0, x],[0, 1, y]])
    width = img.shape[1]
    height = img.shape[0]
    dimention = (width, height)
    return cv.warpAffine(img, Matrix, dimention)

#shift down-right
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)
cv.waitKey(0)