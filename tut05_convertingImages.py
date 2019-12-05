'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Learn how to convert images from one format to another. We will use this file to perform the same actions done with image magic as outlined in the 'NB:' section below
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s): OpenCV Programming with Python on Linux Ubuntu Tutorial-6 Converting Images
link(s):
    [1] 

Reference(s):
    [1] 

NB: You'll need to install the imagemagick software. You can verify if it is already installed on you machine by typing the command into your terminal <identify -version>
    Afterwards, the command(s):
               1.  <convert old_image.jpg new_image.png> for example, could be used to do a conversion of a 'jpg' image to a 'png' image
               2.  <convert old_image.jpg -resize 50% new_image.png>, could also be used to resize the image
'''

from PIL import Image
from numpy import *
from pylab import *

import cv2 # computer vision library

# windows to display image
cv2.namedWindow("Image")

# read image
#im = cv2.LoadImage("rose.jpeg")
im = cv2.imread("rose.jpg")
print(type(im))
cv2.namedWindow("rose", cv2.WINDOW_AUTOSIZE)

#cv2.ShowImage("New rose", im)
cv2.imshow("New rose", im)

#cv2.WaitKey(10000)
cv2.waitKey(10000)

#cv2.SaveImage("new_rose.png",im)
cv2.imwrite("new_rose.png",im)
#cv2.DestroyWindow("rose")
cv2.destroyAllWindows("rose")
