import cv2
import sys

face = cv2.imread("rohitcamera.jpg")

cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

faces = face_cascade.detectMultiScale(
        face,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

cropped = None
for x,y,w,h in faces:
    cv2.rectangle(face, (x,y), (x+w,y+h), (0, 255, 0), 3)
    cropped = face[y:y+h,x:x+w]

cv2.imshow('Just Face', cropped)

cv2.setWindowProperty('Just Face', cv2.WND_PROP_TOPMOST, 1)

cv2.imwrite("justface.png",cropped)

cv2.waitKey(0)

cv2.destroyAllWindows()
