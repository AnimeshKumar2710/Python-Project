import cv2 as cv

img = cv.imread('car.jpg')
cv.imshow('car', img)
scale = 0.5
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)

dimentions = (width, height)
resize= cv.resize(img, dimentions)
cv.imshow('resize', resize)

cv.waitKey(0)