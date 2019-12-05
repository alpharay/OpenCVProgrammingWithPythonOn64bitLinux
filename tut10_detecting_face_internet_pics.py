'''
Author:  Francesco Piscani (Original Author)
Purpose: Detecting faces and retrieve specific image
Date: 2019. 11. 29. (금) 10:52:16 KST
Video Lecture(s):
link(s):
    [1] http://www.stemapks.com/gallery.html  
    [2] https://docs.google.com/document/d/1lk7sNHgqV6ukapiHZgKm-YTj2vNbxoD_9nrodGVKLZE/pub

Reference(s):
    [1] http://www.stemapks.com/opencv_python.html


NB: Some examples of filters used: Box, Guassian, Laplace
'''

from PIL import Image

from numpy import *

from pylab import *

import urllib.request

import cv2

url = 'http://vis-www.cs.umass.edu/lfw/images/Bob_Bowlsby/Bob_Bowlsby_0001.jpg'

#urllib.urlretrieve(url,'filename.png')
urllib.request.urlretrieve(url,'filename.png')

# windows to display image

cv2.namedWindow("Image")

image = cv2.imread('filename.png')

h,w = image.shape[:2]

print(h,w)

# show image

cv2.imshow("Image", image)

# save image

cv2.imwrite('/home/cesco/Desktop/images/retrieve_result.png',image)

# exit at closing of window

cv2.waitKey(0)

cv2.destroyAllWindows()

