# GUI Segmentation

This program goes through the basics of image segmentation using the opencv library on python. The program uses Gaussian Blur to blur the image

The program achieves this by first converting the BGR image (pycharm/opencv uses BGR instead of RGB because RGB was copyrighted) into its HSV range (Hue, Saturation, Value). Using the inRange function, the HSV values in range are masked. Morphological Operations are applied to the 

## Additional Links
Gaussian Blur
* https://www.adobe.com/au/creativecloud/photography/discover/gaussian-blur.html
* https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm

OpenCV BGR Colour Space
* https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/

Links for HSV Segmentation
* https://stackoverflow.com/questions/16472716/why-is-color-segmentation-easier-on-hsv
* https://realpython.com/python-opencv-color-spaces/

Morphological Operations (Dilation & Erosion)
* https://www.mathworks.com/help/images/morphological-dilation-and-erosion.html#:~:text=Morphology%20is%20a%20broad%20set,process%20images%20based%20on%20shapes.&text=In%20a%20morphological%20operation%2C%20the,input%20image%20with%20its%20neighbors
