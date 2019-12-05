'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Learn how apply filters to images. The Sobel filter here is vital for edge detection. It is one
         of the most popular first derivative filters.
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s): OpenCV Programming with Python on Linux Ubuntu Tutorial-7 Filters
link(s):
    [1] 

Reference(s):
    [1] 


NB: Some examples of filters used: Box, Guassian, Laplace
'''

from PIL import Image
import numpy as np
from pylab import *
from matplotlib import pyplot as plt
import cv2 # computer vision library


#read image
img = imread("miches.jpeg",cv2.IMREAD_GRAYSCALE)

# windows to display image
cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)
cv2.imshow('Mices',img)
cv2.waitKey(10000)

# Sobel operator cv2
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


abs_grad_x = cv2.convertScaleAbs(sobelx)
abs_grad_y = cv2.convertScaleAbs(sobely)
img_grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv2.imshow("Miches Sobel",img_grad)
cv2.waitKey(10000)
cv2.imwrite("new_miches_sobel.png",img_grad)
cv2.destroyAllWindows("rose")
