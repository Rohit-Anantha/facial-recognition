import cv2
import numpy as np
import sys

imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

original = cv2.imread(imagePath)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(original, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", original)
cv2.waitKey(0)
cv2.destroyAllWindows()