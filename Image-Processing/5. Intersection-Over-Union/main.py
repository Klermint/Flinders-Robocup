import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

# IoU for ball detection
"""
# define lower and upper boundaries
lower = (0, 100, 80)
upper = (10, 255, 255)
# read, blur, contert to HSV
ball = cv2.imread('ball1.jpg')
ball = cv2.resize(ball, (1080, 810))
blurred = cv2.GaussianBlur(ball, (11, 11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
# construct a mask for colour, perform erosion & dilation
mask = cv2.inRange(hsv, lower, upper)
# cv2.imshow('inRange', mask)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
"""

# histogram equalization
# """
lower = (0, 100, 80)                                # define lower boundary
upper = (10, 255, 255)                              # define upper boundary
ball = cv2.imread('ball63.jpg')                      # read ball
x, y, r = 533, 242, 11
ball = cv2.resize(ball, (1080, 810))                # resize
# cv2.imshow('ball', ball)
hsv = cv2.cvtColor(ball, cv2.COLOR_BGR2HSV)         # convert to hsv
h, s, v = cv2.split(hsv)                            # split hsv
v_hist = cv2.equalizeHist(v)                        # perform equalize on v
hsv_merge = cv2.merge([h, s, v_hist])               # merge h, s and equalize v
# bgr = cv2.cvtColor(hsv_merge, cv2.COLOR_HSV2BGR)
# cv2.imshow('bgr', bgr)
mask = cv2.inRange(hsv_merge, lower, upper)         # inrange
mask = cv2.erode(mask, None, iterations=2)          # erosion
mask = cv2.dilate(mask, None, iterations=2)         # dilation
# cv2.imshow('mask', mask)
# """

# gamma correction
"""
lower = (0, 100, 80)                                # define lower boundaries
upper = (10, 255, 255)                              # define upper boundaries
ball = cv2.imread('ball63.jpg')                      # read file
x, y, r = 533, 242, 11
ball = cv2.resize(ball, (1080, 810))                # resize
# Gamma Correction
lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(pow(i / 255.0, 0.6) * 255.0, 0, 255)
res = cv2.LUT(ball, lookUpTable)
# cv2.imshow('res', res)
hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)          # convert to hsv
mask = cv2.inRange(hsv, lower, upper)               # inrange
mask = cv2.erode(mask, None, iterations=2)          # erosion
mask = cv2.dilate(mask, None, iterations=2)         # dilation
# cv2.imshow('mask', mask)
"""

# Contour
"""
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
    # draw the circle and centroid on the frame
    contour = cv2.inRange(hsv, (255, 255, 255), (255, 255, 255))
    cv2.circle(contour, (int(x), int(y)), int(radius), (255, 255, 255), -1)
# Inserts the mask over the original image that was uploaded
predicted = cv2.bitwise_and(ball, ball, mask=contour)
cv2.imshow('predicted', predicted)
"""

# Hough Transform
# """
# perform Hough Transform
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=1000,
                           param1=1, param2=1, minRadius=0, maxRadius=0)
# draw circles
for i in circles[0, :]:
    hough = cv2.inRange(hsv, (255,255,255), (255,255,255))
    # cv2.circle(ball, (i[0], i[1]), i[2], (255, 255, 255), 2)
    cv2.circle(hough, (i[0], i[1]), i[2], (255, 255, 255), -1)
    print(i[0], i[1], i[2])                                         # *** this prints the x, y, and radius of the Hough***
# Inserts the mask over the original image that was uploaded
predicted = cv2.bitwise_and(ball, ball, mask=hough)
# display images
cv2.imshow('predicted', predicted)
# """

# actual ball location
actual = cv2.inRange(hsv, (255,255,255), (255,255,255))
cv2.circle(actual, (x, y), r, (255,255,255), -1)               # *** change the x, y and radius of the actual ball***
# cv2.circle(ball, (554, 412), 25, (0, 255, 0), 2)
actual = cv2.bitwise_and(ball, ball, mask=actual)
cv2.imshow('actual', actual)
# cv2.imshow('original', ball)

# Intersection over Union calculations
intersection = np.logical_and(predicted, actual)
union = np.logical_or(predicted, actual)
iou_score = np.sum(intersection) / np.sum(union)
print('IoU: %s' % iou_score)

cv2.waitKey(0)

"""
# IoU for goal post detection
goalpost = cv2.imread('goal.jpg')

predicted = [[245, 80], [550, 80], [550, 320], [245, 320]]
stencil = numpy.zeros(goalpost.shape).astype(goalpost.dtype)
contours = [numpy.array(predicted)]
color = [255, 255, 255]
cv2.fillPoly(stencil, contours, color)
result1 = cv2.bitwise_and(goalpost, stencil)
cv2.imshow('result1', result1)

actual = [[280, 190], [438, 190], [438, 390], [280, 390]]
stencil = numpy.zeros(goalpost.shape).astype(goalpost.dtype)
contours = [numpy.array(actual)]
color = [255, 255, 255]
cv2.fillPoly(stencil, contours, color)
result2 = cv2.bitwise_and(goalpost, stencil)
# cv2.imshow('result2', result2)

cv2.waitKey(0)

"""
