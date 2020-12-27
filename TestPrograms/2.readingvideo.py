import cv2 as cv

capture= cv.VideoCapture('car.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)

    if cv.waitKey(20) & 0xFF== ord(' '): 
        break

capture.release()
cv.destroyAllWindows()
