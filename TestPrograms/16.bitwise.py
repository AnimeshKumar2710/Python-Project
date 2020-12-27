import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype= 'uint8')

rectangle = cv.rectangle(blank.copy(), (0,0), (200, 200),(255, 255, 255), thickness= -1)
circle = cv.circle(blank.copy(), (200, 200), 100, (255, 255, 255), -1)
cv.imshow('Circle', circle)
cv.imshow('rectangle', rectangle)

#bitwise AND
A = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise And", A)

#bitwise OR
O = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", O)

#bitwise XOR
X = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', X)

#Bitwise NOT
N= cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", N)

cv.waitKey(0)
