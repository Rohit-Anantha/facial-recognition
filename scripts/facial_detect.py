import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

import scripts.compare_two_images as compare_two_images

cascPath = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

rohit = cv2.imread("justface.png")

if len(sys.argv) < 2:
    video_capture = cv2.VideoCapture(0)
else:
    video_capture = cv2.VideoCapture(sys.argv[1])

data = []

while True:
    cropped = None
    ret, image = video_capture.read()

    rohit_found = False

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
        # cv2.imshow('cropped', cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY))
        # cv2.setWindowProperty('cropped', cv2.WND_PROP_TOPMOST, 1)
        difference, sum = compare_two_images.compare_two(cropped, rohit)
        data.append(sum)
        if sum < 1.75e6:
            rohit_found = True
        # cv2.imshow('difference', difference)
        # cv2.setWindowProperty('difference', cv2.WND_PROP_TOPMOST, 1)


    cv2.putText(image, "Faces found: {}".format(len(faces)), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    if rohit_found:
        cv2.putText(image, "Rohit found!", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        cv2.putText(image, "Rohit not found!", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow('Video', image)
    cv2.setWindowProperty('Video', cv2.WND_PROP_TOPMOST, 1)

    rohit_found = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

n, bins, patches = plt.hist(x=data, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()