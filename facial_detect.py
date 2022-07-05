import cv2
import sys

import compare_two_images

cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

rohit = cv2.imread("justface.png")

if len(sys.argv) < 2:
    video_capture = cv2.VideoCapture(0)
else:
    video_capture = cv2.VideoCapture(sys.argv[1])

while True:
    cropped = None
    ret, image = video_capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cropped = image[y:y+h,x:x+w]

    if cropped is not None:
        cv2.imshow('cropped', cropped)
        cv2.setWindowProperty('cropped', cv2.WND_PROP_TOPMOST, 1)
        difference = compare_two_images.compare_two(cropped, rohit)
        print(difference)



    cv2.putText(image, "Faces found: {}".format(len(faces)), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow('Video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()