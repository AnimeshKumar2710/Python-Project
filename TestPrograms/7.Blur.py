import cv2 as cv

img = cv.imread('car.jpg')

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

cv.waitKey(0)