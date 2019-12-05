'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Learn how to resize images from one format to another. We will use this file to perform the resizing action done with image magic as outlined in the 'NB:' section below
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
import numpy as np
from pylab import *

import cv2 # computer vision library

# windows to display image
cv2.namedWindow("Image")

# read image
#original = cv2.LoadImage("rose.jpeg")
original = cv2.imread("rose.jpg",cv2.IMREAD_GRAYSCALE)
print('Original Dimensions : ',original.shape) 
print(type(original))
cv2.namedWindow("rose", cv2.WINDOW_AUTOSIZE)

#resized = cv2.CreateMat(original.rows/5, original.cols/5, cv2.CV_BUC3)
new_height = int(original.shape[0]/2)
new_width = int(original.shape[1]/2)

new_dim = (new_width,new_height)
#resized = cv2.Resize(original/ resized)
print(new_dim)
resized = cv2.resize(original,new_dim, interpolation = cv2.INTER_AREA)

#cv2.ShowImage("New rose", original)
cv2.imshow("New rose", original)

#cv2.WaitKey(10000)
cv2.waitKey(10000)

#cv2.SaveImage("new_rose.png",original)
cv2.imwrite("resized_rose.png",resized)
print('Resize Dimensions : ',resized.shape) 
#cv2.DestroyWindow("rose")
cv2.destroyAllWindows("rose")
