import cv2 as cv
import numpy as np

img = cv.imread('car.jpg')

cv.imshow('Orignal', img)

def rotate(img, angle, point= None):
    height, width = img.shape[:2]
    if point is None:
        point = (width//2, height//2)
    Matrix = cv.getRotationMatrix2D(point, angle, 1)
    dimention = (width, height)

    return cv.warpAffine(img, Matrix, dimention)


rotated = rotate(img, 45)
cv.imshow('rotated', rotated)
cv.waitKey(0)