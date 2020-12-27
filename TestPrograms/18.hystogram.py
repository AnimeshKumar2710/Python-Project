import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('car.jpg')
img= cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grayscale', gray)

gray_hist = cv.calcHist(gray, [0],None, [256], [0,256])

plt.figure()
plt.title('Grayscale Hystogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)