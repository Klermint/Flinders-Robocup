"""
This program is used to apply Hough Transform on various images
to fine-tune the parameters of the Hough Circle Function.
Best parameters for test_gray: minDist=1000, param1=1, param2=1
Best parameter for red3: minDist=1, param1=50, param2=18
Best parameters to fit any image: minDist=1000, param1=1, param2=1 (accuracy decreases)
"""

# import the necessary packages
import cv2
import numpy as np

# define the lower and upper boundaries of the "red"
lower = (0, 100, 80)
upper = (10, 255, 255)

# read the file
original_img = cv2.imread('red3.png')
cv2.imshow('Inputted Image', original_img)

# blur and convert to HSV
blur = cv2.GaussianBlur(original_img, (11, 11), 0)
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

# construct a mask for colour, perform erosion & dilation
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
cv2.imshow('mask', mask)

# Perform Hough Transform
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp= 1, minDist=1000,
                           param1=1, param2=1, minRadius=0, maxRadius=0)

# Draw a circle for each circle detected by Hough Transform
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(original_img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(original_img,(i[0],i[1]),2,(255,255,255),3)

# Display Circle Found
cv2.imshow('Hough Transform', original_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
