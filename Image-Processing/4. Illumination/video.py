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
    cv2.imshow('original frame', frame)
    # convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    # split HSV
    h, s, v = cv2.split(hsv)
    cv2.imshow('v', v)
    # histogram equalize on value range
    v_hist = cv2.equalizeHist(v)
    cv2.imshow('v_hist', v_hist)
    # merge back to hsv
    hsv_merge = cv2.merge([h, s, v_hist])
    cv2.imshow('hsv_merge', hsv_merge)
    bgr = cv2.cvtColor(hsv_merge, cv2.COLOR_HSV2BGR)
    cv2.imshow('bgr', bgr)
    # construct a mask for colour, perform erosion & dilation
    mask = cv2.inRange(hsv_merge, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask', mask)
    # perform Hough Transform
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=1000,
                               param1=50, param2=15, minRadius=0, maxRadius=0)
    # original parameters: (minDist=1000,param1=50, param2=15, minRadius=0, maxRadius=0)
    # proceed if there is a circle
    if circles is not None:
        circles = np.uint16(np.around(circles))
        # draw circles
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(bgr, (i[0], i[1]), i[2], (255, 255, 255), 2)
            # draw the center of the circle
            cv2. circle(bgr, (i[0], i[1]), 2, (255, 255, 255), 3)
        center = (i[0], i[1])
        # update the points queue
        pts.appendleft(center)

        # loop over the set of tracked points
        for i in range(1, len(pts)):
            # if either of the tracked points are None, ignore them
            if pts[i - 1] is None or pts[i] is None:
                continue

            # otherwise, compute the thickness of the line and draw connecting lines
            # thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
            # cv2.line(frame, pts[i - 1], pts[i], (255, 255, 255), thickness)
    cv2.imshow('Hough Transform', bgr)
    key = cv2.waitKey(1) & 0xFF

cv2.destroyAllWindows()
