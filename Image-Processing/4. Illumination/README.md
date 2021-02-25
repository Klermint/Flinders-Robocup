# Illumination
In the previous Hough Transform Programs, one of the limitations occured when the frame is underexposed and the image is dark. Because of this, the ball appears black instead of a shade of red therefore, it is not detected by the HSV segmentation. To overcome this issues, several techniques were applied including Histogram Equalisation, Gamma Correction and Adaptive Filtering.

Similar to the previous Hough Transform folder, this folder contains two python files, main.py and video.py. Main.py allows the user to test different illumination techniques on any image they. THe video.py file allows the user to test the different illumination techniques of live video feed from the webcam.

## Histogram Equalisation
When looking at the histogram of the underexposed image, the histogram is biased towards the left and low intensity range. Histogram Equalisation evenly distributes the clustered histogram bringing more contrast to the image. Histogram Equalisation can only be applied to a single channel such as greyscale however, once the image/frame is converted from BGR to grayscale, it cannot be converted back into BGR again because BGR is a three channel image. Instead, histogram equalisation is applied to the value channel of its HSV range. This distributes the illumination of the image whilts keeping the Hue and Saturation of the image. The new value range is merged back into the hue and saturation to produce an image with better illumination to detect the ball.

## Gamma Correction
Gamma Correction is another techni

## Adaptive Filtering


## Additional Links
Histogram Equalisation
* https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html 
* https://docs.opencv.org/master/d5/daf/tutorial_py_histogram_equalization.html 

Gamma Correction
* https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html

Adaptive Filtering
* https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
* https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
