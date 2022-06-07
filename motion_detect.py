import cv2
import sys
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

ret, last_frame = video_capture.read()
ret, current_frame = video_capture.read()

i = 0

while True:
    last_frame = current_frame
    ret, current_frame = video_capture.read()
    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    
    diff = cv2.absdiff(last_frame, current_frame)

    if(i % 20 == 0):
        print("original:", np.mean(gray))
        print("difference:" , np.mean(diff))
        i = 0

    if np.mean(diff) > 5:
        cv2.imshow('Motion Detected :D', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1

video_capture.release()
cv2.destroyAllWindows()