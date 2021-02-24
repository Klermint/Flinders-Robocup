# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import cv2
import numpy as np
import imutils
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "red"
lower = (0, 100, 80)
upper = (10, 255, 255)
pts = deque(maxlen=args["buffer"])

# get webcam
camera = VideoStream(src=0).start()

# keep looping
while True:
    # get the current frame
    frame = camera.read()
    # resize, blur and convert to HSV
    frame = imutils.resize(frame, width=700)
    cv2.imshow('original frame', frame)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    cv2.imshow('GaussianBlur', blurred)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)
    # construct a mask for colour, perform erosion & dilation
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cv2.imshow('mask', mask)
    # find contours in the mask and initialize the current
    # (x,y) center of the ball
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None
    # proceed if one contour found
    if len(contours) > 0:
        # find the largest contour, compute the minimum enclosing circle and centroid
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # if the radius meets minimum size
        if radius > 8:
            # draw the circle and centroid on the frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 255, 255), 2)
            cv2.circle(frame, center, 5, (255, 255, 255), -1)
    # update the points queue
    pts.appendleft(center)

    # loop over the set of tracked points
    for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore them
        if pts[i - 1] is None or pts[i] is None:
            continue

        # otherwise, compute the thickness of the line and draw connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (255, 255, 255), thickness)

    # display frame
    #frame = cv2.resize(frame, (700, 400))
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

# close all windows
cv2.destroyAllWindows()