import cv2
import os
import numpy

# given two color images, send back if they are similar / confidence levels
def compare_two(img1,img2):

    # convert to grayscale

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    

    # blur the two images

    blur1 = cv2.GaussianBlur(gray1, (5, 5), 0)
    blur2 = cv2.GaussianBlur(gray2, (5, 5), 0)


    # make the two images into a 2d array

    arr1 = numpy.asarray(blur1)
    arr2 = numpy.asarray(blur2)

    # resize the two images to be the same size
    
    arr1 = cv2.resize(arr1, (arr2.shape[1], arr2.shape[0]))
    # compare the two images and display

    difference = cv2.subtract(arr1, arr2)
    # cv2.imshow('difference', difference)

    sum = numpy.sum(difference)

    # print("sum of difference:", sum)

    if sum < 1.75e6:
        print("That is Rohit")
    else:
        print("That is not Rohit")
    
    return difference, sum
