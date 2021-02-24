# import the necessary packages
import cv2
import numpy as np
from matplotlib import pyplot as plt

# define the lower and upper boundaries of the "red"
lower = (0, 100, 80)
upper = (10, 255, 255)

# read the file
original_img = cv2.imread('red3.png')
cv2.imshow('original_img', original_img)

# HISTOGRAM EQUALISATION
"""
# HSV
hsv = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# Split HSV
h, s, v1 = cv2.split(hsv)
# cv2.imshow('h', h)
# cv2.imshow('s', s)
cv2.imshow("v1",v1)

# V equalize
v_hist = cv2.equalizeHist(v1)
cv2.imshow('v_hist', v_hist)

# merge hsv back and convert the bgr
hsv = cv2.merge([h, s, v_hist])
res = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('bgr', res)
"""

# GAMMA correction
# """
lookUpTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookUpTable[0, i] = np.clip(pow(i / 255.0, 0.6) * 255.0, 0, 255)
res = cv2.LUT(original_img, lookUpTable)
cv2.imshow('gamma', res)

hsv_merge = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
# """

# ADAPTIVE FILTER
"""
# HSV
HSV = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', HSV)

# HSV2GRAY
h, s, v1 = cv2.split(HSV)
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow("v1",v1)

# Traditional Thresholding
ret,th1 = cv2.threshold(GRAY,127,255,cv2.THRESH_BINARY)
cv2.imshow('globalThresholding', th1)

# Adaptive Mean Thresholding
th2 = cv2.adaptiveThreshold(GRAY,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,11,2)
cv2.imshow('adaptiveMeanThresholding', th2)

# Adaptive Gaussian Thresholding
th3 = cv2.adaptiveThreshold(GRAY, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 2)
cv2.imshow('adaptiveGaussianThreshold', th3)

# Gaussian Blur + Otsu Thresholding
blur = cv2.GaussianBlur(GRAY, (11, 11), 0)
ret4,th4 = cv2.threshold(blur,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu', th4)

# Gaussian Blur + Otsu_HSV Thresholding
blur = cv2.GaussianBlur(v1, (11, 11), 0)
ret4,th4 = cv2.threshold(blur,255,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu_HSV', th4)
"""

# construct a mask for colour, perform erosion & dilation
mask = cv2.inRange(hsv_merge, lower, upper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
cv2.imshow('mask', mask)

# perform Hough Transform
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=1000,
                           param1=1, param2=1, minRadius=0, maxRadius=0)
# param1=50, param2=30
# draw circles
for i in circles[0, :]:
    cv2.circle(res, (i[0], i[1]), i[2], (255, 255, 255), 2)

cv2.imshow('hough', res)

# display histogram
# plt.hist(res.ravel(), 256, [0,256])
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()