import cv2
import sys


image = cv2.imread(sys.argv[1])
image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(grayscale, (5, 5), 0)

cv2.imshow('image', image)
cv2.imshow('grayscale', grayscale)
cv2.imshow('blur', blur)

cannyLow = cv2.Canny(blur, 10, 30)
cannyHigh = cv2.Canny(blur, 50, 150)

cv2.imshow('cannyLow', cannyLow)
cv2.imshow('cannyHigh', cannyHigh)

# cv2.waitKey(0)

# image = cv2.imread(sys.argv[1])
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grayscale, (5, 5), 0)
Canny = cv2.Canny(blur, 30, 100)
contours, hierarchy= cv2.findContours(Canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
cv2.imshow('contours', image)
cv2.waitKey(0)