import cv2 as cv

img = cv.imread('car.jpg')

edge = cv.Canny(img, 100, 200)
cv.imshow('Edge Detection', edge)

cv.waitKey(0)