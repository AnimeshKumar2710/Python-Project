import cv2 as cv
import numpy as np
#Blank img
img = np.zeros((500, 500, 3), dtype= 'uint8')
#cv.imshow('Blank', img)

#changing color to white
img[:] = 255, 255, 255    #bgr
#cv.imshow('White', img)

#setting a range of pixels to red
img[0:250, 0:250] = 0, 0, 255
#cv.imshow('Upper Left Red', img)

#drawing a blue rectangle
cv.rectangle(img, (250, 250), (500, 500), (255, 0, 0), thickness= 2)
#cv.imshow('Rectangle', img)

#draw circle
cv.circle(img, (250, 250), 50, (0, 255, 0), thickness= 2)
#cv.imshow("Circle", img)

#draw line
cv.line(img, (250, 250), (0, 500), (100, 100, 100), thickness= 2)
#cv.imshow("line", img)

#adding text
cv.putText(img, 'Hello', (375, 125), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), 2)
#cv.imshow("Text", img)
cv.waitKey(0)