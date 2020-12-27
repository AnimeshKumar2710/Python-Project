import cv2 as cv

img = cv.imread('car.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)
cv.waitKey(0)