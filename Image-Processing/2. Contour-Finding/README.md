# Contour Finding
This program is a continuation from the previous GUI Segmentation code. Instead of applying HSV segmentation to an image, this program applies HSV segmentation to a live video from a webcam. 

To connect a webcam, plug the usb from the webcam into your laptop/computer. You might have to disable the integrated webcam from your laptop. To do so, go to device manager -> camera -> Right Click Integrated Webcam -> Disable.

Using the mask for the HSV segmentation, contours were located. The program finds the contour with the largest area and draws a circle around the contour. In most cases, this would be the ball therefore, the ball's location is located. In addition, the ball's previous positions were tracked and displayed.

## Additional Links
* https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
* https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
