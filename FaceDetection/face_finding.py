import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features = np.load('features.npy')
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('GOTmain.yml')

people = []
dir = r"C:\Users\Cloud\Documents\GitHub\Python-Project\FaceDetection\faces"
for i in os.listdir(dir):
    people.append(i)


img = cv.read('validation.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

for (x, y, w, h) in faces_rect:
    face_roi = gray[y:y+h][x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness= 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness= 2)

cv.imshow(img)
cv.waitKey(0)