import cv2 as cv
img = cv.imread('car.jpg')
cv.imshow('car', img)
cv.waitKey(0)