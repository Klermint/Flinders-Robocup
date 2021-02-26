# Hough Transform

In the contour finding method, the ball was detected using the largest contour however, if another similarly red object is within the frame, the program would detect that object instead of the ball. To overcome this, Hough Circle Transform is applied on the mask instead of contour detection. **(Explain how Hough Circle Transform works, Work in progress, see documentation in microsoft teams)**

This folder contains two seperate piece of code. The main.py file applies Hough Transform to an image. Here, you can test out different parameters of the Hough Transform with your own images. The video.py file applyies Hough Transform to a live video feed from the webcam similar to the Contour finding code.

## Limitations
Some limiations with the Hough Transform include:
* when the video feed is underexposed, the image is dark and the ball appears black. Since the program still uses the HSV range of the ball, the ball cannot be detected therefore, Hough Transform cannot be applied to the mask.

## Errors
Currently, the line tracking in the video.py file sometimes goes to the (0,0) position (top left) of the screen when no circles are detected. The line tracking is currently commented out.

## Links to Hough Circle Transform 
* https://docs.opencv.org/master/da/d53/tutorial_py_houghcircles.html 
* https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html 
* https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php 
* https://docs.opencv.org/3.4/d3/de5/tutorial_js_houghcircles.html 
* https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/ 
