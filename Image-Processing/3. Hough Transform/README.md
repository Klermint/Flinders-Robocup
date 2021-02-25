# Hough Transform

In the contour finding method, the ball was detected using the largest contour however, if another similarly red object is within the frame, the program would detect that object instead of the ball. To overcome this, Hough Circle Transform is applied on the mask instead of contour detection. 

Limitations

Errors
Currently, the line tracking sometimes goes to the (0,0) position of the screen when no circles are detected. The line tracking is currently commented out.

## Links to Hough Circle Transform 
* https://docs.opencv.org/master/da/d53/tutorial_py_houghcircles.html 
* https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html 
* https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php 
* https://docs.opencv.org/3.4/d3/de5/tutorial_js_houghcircles.html 
* https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/ 
