import cv2 as cv

capture = cv.VideoCapture('car.mp4')
while True:
    isTrue, frame = capture.read()
    width = int(frame.shape[1] * 0.75)
    height = int(frame.shape[0] * 0.75)
    dimention = (width, height)
    reshape = cv.resize(frame, dimention)
    cv.imshow('reshape', reshape)
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xFF== ord(' '):
        break
capture.release()
cv.destroyAllWindows()