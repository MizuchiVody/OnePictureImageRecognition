from shapedetection import ShapeDetector
import numpy as np
import imutils
from sys import *
from numpy import *
from cv2 import *

image = imread('shapes.jpg',-1)
#imshow('shapes', image)
#waitKey(0)
img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
# ratio = image.shape[0] / float(image.shape[0])
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
# blurred = cv2.GaussianBlur(img, (5, 5), 0)
HSV = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([170, 255, 255])
HSVblueThresh = cv2.inRange(HSV, lower_blue, upper_blue)

lower_yellow = np.array([13, 90, 90])
upper_yellow = np.array([30, 255, 255])
HSVyellowThresh = cv2.inRange(HSV, lower_yellow, upper_yellow)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
HSVredThresh = cv2.inRange(HSV, lower_red, upper_red)
cv2.imshow("yellow", HSVyellowThresh)
cv2.imshow("blue", HSVblueThresh)
cv2.imshow("red", HSVredThresh)
cv2.waitKey(0)
Threshes = [HSVredThresh, HSVblueThresh, HSVyellowThresh]
counter = 0
tail = ""
for thresh in Threshes:
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    print(image.shape)
    # initialize the shape detector and color labeler in initial shape and initial color
    iShape = ShapeDetector()
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)
        else:
            cX = 0
            cY = 0

        shape = ""
        color = ""

        shape = iShape.DetectTheShape(c)

        print(image[cY, cX])
        # counter = 0
        color = ""
        while color == ""
            print (counter)
            if counter == 0:
                color = "Red"
            elif counter == 1:
                color = "Blue"
            elif counter == 2:
                color = "Yellow"
            else :
                color = "X"
        if shape == "Triangle":
            if color == "Red":
                tail = "UH8"
            elif color == "Yellow":
                tail = "L6R"
            elif color == "Red":
                tail = "G7C"
        elif shape == "Rectangle":
            if color == "Red":
                tail = "S1P"
            elif color == "Yellow":
                tail = "JW3"
            elif color == "Blue":
                tail = "A2X"
        if shape != "" and color != "X" and color != "":
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            text = "{} {} {}".format(tail ,color, shape)
            cv2.drawContours(image, [c], -1, (0, 255, 0), 1)
            cv2.putText(image, text, (cX, cY),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    counter = counter +1
    # show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
