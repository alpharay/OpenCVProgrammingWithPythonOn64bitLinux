'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: To read and display image file
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s):OpenCV Programming with Python on Linux Ubuntu Tutorial-2 Display an Image
link(s):
    [1] https://www.youtube.com/watch?v=KBAMHWP7wCQ&list=PLS1lqxOwNjObDAH-ymnep3XLljhb2pUL-&index=2

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
image = cv2.imread("cameraman.tif")
h,w = image.shape[:2] # getting the images height and width
print(h, w) 

# save image
cv2.imwrite("cameraman_copy.tif",image)

# show image
cv2.imshow("Image",image)


#exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
