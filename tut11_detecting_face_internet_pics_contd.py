'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Detecting faces
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

from wand.image import Image

from wand.display import display

import urllib

import cv2

url = 'http://vis-www.cs.umass.edu/lfw/images/Bob_Bowlsby/Bob_Bowlsby_0001.jpg'

urllib.urlretrieve(url,'bob.png')

with Image(filename='bob.png') as img:

    print(img.size)

    for r in 1, 2, 3:

        with img.clone() as i:

            i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))

            i.rotate(90 * r)

            i.save(filename='bob-{0}.png'.format(r))

            display(i)

# windows to display image

cv2.namedWindow("Image")

image = cv2.imread('bob.png')

h,w = image.shape[:2]

print h,w

# show image

cv2.imshow("Image", image)

# save image

cv2.imwrite('/home/cesco/Desktop/python/bob.png',image)
