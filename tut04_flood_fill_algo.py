'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Learning how to use the flood fill algorithm
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s): OpenCV Programming with Python on Linux Ubuntu Tutorial-5 Flood Fill Algorithm
link(s):
    [1] https://www.youtube.com/watch?v=oMYeeGdmNfQ&list=PLS1lqxOwNjObDAH-ymnep3XLljhb2pUL-&index=5

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
h,w = im.shape[:2] # getting the images height and width
#print(h, w) 

# flood fill example
diff = (6,6,6)
mask = zeros((h+2,w+2),uint8)
cv2.floodFill(im,mask,(10,10),(145,255,0),diff,diff)

# save image
cv2.imwrite("einstein_floodfill.jpg",im)

# show the result in an OpenCV window
cv2.imshow("Flood Fill Image",im)
cv2.waitKey(0)
cv2.destroyAllWindows()


