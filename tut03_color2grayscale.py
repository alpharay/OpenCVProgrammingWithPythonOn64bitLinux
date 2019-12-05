'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: To read and display image file
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s):OpenCV Programming with Python on Linux Ubuntu Tutorial-3 From Color to Grayscale
link(s):
    [1] https://www.youtube.com/watch?v=gSe8wiDxc2Q&list=PLS1lqxOwNjObDAH-ymnep3XLljhb2pUL-&index=3

Reference(s):
    [1] 
'''

from PIL import Image
from numpy import *
from pylab import *

import cv2 # computer vision library

# windows to display image
cv2.namedWindow("Image")

# read image
im = cv2.imread("einstein.jpeg")
#h,w = image.shape[:2] # getting the images height and width
#print(h, w) 

# create a grayscale version
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# save image
cv2.imwrite("cameraman_gray_version.tif",gray)

# show image
cv2.imshow("Image",im)


#exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
