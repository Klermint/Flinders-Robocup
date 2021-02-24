# GUI Segmentation

This program goes through the basics of image segmentation using the opencv library on python. The program first uses Gaussian Blur to blur the image to remove noise in the image. The image is then converted from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value/Brightness/Luminance). (Note: OpenCV images are in BGR instead of RGB due to previous copyright issues, it's stupid) HSV is used because it separates color imformation (chroma) from intensity or lighting. The inRange function is used to isolate the 'red' in the HSV image masking the ball. Dilation is used to fill in any black spots within the ball while erosion is used to 'erode' the edges of the mask.

To learn more about HSV Segmentation, feel free to copy this code and insert your own image and play around with the sliders. To insert your own image, add the image into the same folder as the code and replace 'red3.png' with the name of your own image.

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
