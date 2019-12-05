'''
Author: 
Purpose: Implementing the DCT (Discrete Cosine Transform)
Date: 2019. 11. 29. (금) 10:52:16 KST
Video Lecture(s): 
link(s):
    [1] https://docs.google.com/document/d/1Ga1dKIBx61gVphSqlq2c9mbipYWAFgGdcro1zdeQ8YI/pub

Reference(s):
    [1] http://www.stemapks.com/opencv_python.html


NB: Same code as found in 'JPEG_DCT_Demo2.py' file
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.cm as cm

# cut an image up into blocks of 8x8 pixels blocksize
# print height and width
# the image is cropped, such that its height and width is a multiple of blocksize
B=8
fn3= 'lichtenstein.png'
img1 = cv2.imread(fn3, cv2.IMREAD_GRAYSCALE)
h,w=np.array(img1.shape[:2])/B * B
print(h)
print(w)
h=int(h)
w=int(w)
img1=img1[:h,:w]

# run each block through an 8x8 2D Discrete Cosine Transform (cv2.dct())
# the transformed image is stored in a variable (trans) and saved into the file 'transformed.jpg'
blocksV=h/B
blocksH=w/B
vis0 = np.zeros((h,w), np.float32)
trans = np.zeros((h,w), np.float32)
vis0[:h, :w] = img1

for row in range(int(blocksV)):
    for col in range(int(blocksH)):
        currentblock = cv2.dct(vis0[row*B:(row+1)*B,col*B:(col+1)*B])
        trans[row*B:(row+1)*B,col*B:(col+1)*B]=currentblock

cv2.imwrite('transformed.jpg', trans)

plt.imshow(img1,cmap="gray")
point=plt.ginput(1)
block=np.floor(np.array(point)/B) #first component is col, second component is row
print(block)
col=block[0,0]
row=block[0,1]
plt.plot([B*col,B*col+B,B*col+B,B*col,B*col],[B*row,B*row,B*row+B,B*row+B,B*row])
plt.axis([0,w,h,0])
plt.title("Original Image")

# the selected block and its DCT-transform are then plotted into a second Matplotlib-figure

plt.figure()
plt.subplot(1,2,1)

slicer_begin = int(row*B)
slicer_middle1 = int((row+1)*B)
slicer_middle2 = int(col*B)
slicer_end = int((col+1)*B)
selectedImg=img1[slicer_begin:slicer_middle1,slicer_middle2:slicer_end]

N255=Normalize(0,255) #Normalization object, used by imshow()
plt.imshow(selectedImg,cmap="gray",norm=N255,interpolation='nearest')
plt.title("Image in selected Region")
plt.subplot(1,2,2)

slicer_begin = int(row*B)
slicer_middle1 = int((row+1)*B)
slicer_middle2 = int(col*B)
slicer_end = int((col+1)*B)
selectedTrans=trans[slicer_begin:slicer_middle1,slicer_middle2:slicer_end]

plt.imshow(selectedTrans,cmap=cm.jet,interpolation='nearest')
plt.colorbar(shrink=0.5)
plt.title("DCT transform of selected Region")

# the IDCT is applied to reconstruct the original image from the transformed representation.
# the reconstructed image is stored in the variable back0 and it is saved to the file 'BackTransformed.jpg'
# rebuild an image in the spatial domain from the frequencies obtained

back0 = np.zeros((int(h),int(w)), np.float32)
for row in range(int(blocksV)):
    for col in range(int(blocksH)):
        currentblock = cv2.idct(trans[row*B:(row+1)*B,col*B:(col+1)*B])
        back0[row*B:(row+1)*B,col*B:(col+1)*B]=currentblock

cv2.imwrite('BackTransformed.jpg', back0)

# verify that DCT and IDCT are lossless, the Mean Absolute Difference (MAD) between the original and the reconstructed image is calculated and printed to the console
diff=back0-img1
print(diff.max())
print(diff.min())
MAD=np.sum(np.abs(diff))/float(h*w)
print("Mean Absolute Difference: ",MAD)
plt.figure()
plt.imshow(back0,cmap="gray")
plt.title("Backtransformed Image")
plt.show()

