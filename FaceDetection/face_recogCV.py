import os
import cv2 as cv
import numpy as np

people = []
dir = r"\faces"
for i in os.listdir(dir):
    people.append(i)

print(people)
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
features = []
labels = []

for person in people:
    path = os.path.join(dir, person)
    label = people.index(person)

    for img in os.listdir(path):
        img_path = os.path.join(path, img)

        img_array = cv.imread(img_path)
        scale = 0.25
        width = int(img_array.shape[1] * scale)
        height = int(img_array.shape[0] * scale)

        dimentions = (width, height)
        resize = cv.resize(img_array, dimentions)
        gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 11)

        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y+h][x:x+w]
            features.append(faces_roi)
            labels.append(label)

features = np.array(features, dtype= 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save('GOTmain.yml')
np.save("features.npy", features)
np.save("labels.npy", labels)
