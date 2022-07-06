import cv2
import os
import numpy



abba = '../images/abba.jpg'

abba_image = cv2.imread(abba)

cv2.imshow('abba', abba_image)
cv2.setWindowProperty('abba', cv2.WND_PROP_TOPMOST, 1)

cv2.waitKey(0)

cv2.destroyAllWindows()