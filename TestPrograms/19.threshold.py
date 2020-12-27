import cv2 as cv

img = cv.imread('car.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# simple threshlonding

threshhold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

#adaptive threshhold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow("Adaptive threshhold", adaptive_thresh)
cv.waitKey(0)