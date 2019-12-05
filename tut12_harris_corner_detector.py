'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Corner detection
Date: 2019. 11. 29. (금) 10:52:16 KST
Video Lecture(s):
link(s):
    [1] http://www.stemapks.com/gallery.html  
    [2] https://docs.google.com/document/d/1lk7sNHgqV6ukapiHZgKm-YTj2vNbxoD_9nrodGVKLZE/pub

Reference(s):
    [1] http://www.stemapks.com/opencv_python.html


NB: Some examples of filters used: Box, Guassian, Laplace
'''

from pylab import *

from numpy import *

from scipy.ndimage import filters

import harris

import cv2

from PIL import Image

import harris_run

im = array(Image.open('lady_in_red_big.jpg').convert('L'))

harrisim = harris.compute_harris_response(im)

filtered_coords = harris.get_harris_points(harrisim,6)

harris.plot_harris_points(im, filtered_coords)

from PIL import Image

from pylab import *

from numpy import *

from scipy.ndimage import filters

def compute_harris_response(im,sigma=3):

    """ Compute the Harris corner detector response function

       for each pixel in a graylevel image. """

   

    # derivatives

    imx = zeros(im.shape)

    filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)

    imy = zeros(im.shape)

    filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)

   

    # compute components of the Harris matrix

    Wxx = filters.gaussian_filter(imx*imx,sigma)

    Wxy = filters.gaussian_filter(imx*imy,sigma)

    Wyy = filters.gaussian_filter(imy*imy,sigma)

   

    # determinant and trace

    Wdet = Wxx*Wyy - Wxy**2

    Wtr = Wxx + Wyy

   

    return Wdet / (Wtr*Wtr)

   

   

def get_harris_points(harrisim,min_dist=10,threshold=0.1):

    """ Return corners from a Harris response image

       min_dist is the minimum number of pixels separating

       corners and image boundary. """

   

    # find top corner candidates above a threshold

    corner_threshold = harrisim.max() * threshold

    harrisim_t = (harrisim > corner_threshold) * 1

   

    # get coordinates of candidates

    coords = array(harrisim_t.nonzero()).T

   

    # ...and their values

    candidate_values = [harrisim[c[0],c[1]] for c in coords]

   

    # sort candidates

    index = argsort(candidate_values)

   

    # store allowed point locations in array

    allowed_locations = zeros(harrisim.shape)

    allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1

   

    # select the best points taking min_distance into account

    filtered_coords = []

    for i in index:

        if allowed_locations[coords[i,0],coords[i,1]] == 1:

            filtered_coords.append(coords[i])

            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),

                        (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0

   

    return filtered_coords

   

   

def plot_harris_points(image,filtered_coords):

    """ Plots corners found in image. """

   

    figure()

    gray()

    imshow(image)

    plot([p[1] for p in filtered_coords],

                [p[0] for p in filtered_coords],'*')

    axis('off')

    show()

   

def get_descriptors(image,filtered_coords,wid=5):

    """ For each point return pixel values around the point

       using a neighbourhood of width 2*wid+1. (Assume points are

       extracted with min_distance > wid). """

   

    desc = []

    for coords in filtered_coords:

        patch = image[coords[0]-wid:coords[0]+wid+1,

                            coords[1]-wid:coords[1]+wid+1].flatten()

        desc.append(patch)

   

    return desc

def match(desc1,desc2,threshold=0.5):

    """ For each corner point descriptor in the first image,

       select its match to second image using

       normalized cross correlation. """

   

    n = len(desc1[0])

   

    # pair-wise distances

    d = -ones((len(desc1),len(desc2)))

    for i in range(len(desc1)):

        for j in range(len(desc2)):

            d1 = (desc1[i] - mean(desc1[i])) / std(desc1[i])

            d2 = (desc2[j] - mean(desc2[j])) / std(desc2[j])

            ncc_value = sum(d1 * d2) / (n-1)

            if ncc_value > threshold:

                d[i,j] = ncc_value

           

    ndx = argsort(-d)

    matchscores = ndx[:,0]

   

    return matchscores

def match_twosided(desc1,desc2,threshold=0.5):

    """ Two-sided symmetric version of match(). """

   

    matches_12 = match(desc1,desc2,threshold)

    matches_21 = match(desc2,desc1,threshold)

   

    ndx_12 = where(matches_12 >= 0)[0]

   

    # remove matches that are not symmetric

    for n in ndx_12:

        if matches_21[matches_12[n]] != n:

            matches_12[n] = -1

   

    return matches_12

def appendimages(im1,im2):

    """ Return a new image that appends the two images side-by-side. """

   

    # select the image with the fewest rows and fill in enough empty rows

    rows1 = im1.shape[0]   

    rows2 = im2.shape[0]

   

    if rows1 < rows2:

        im1 = concatenate((im1,zeros((rows2-rows1,im1.shape[1]))),axis=0)

    elif rows1 > rows2:

        im2 = concatenate((im2,zeros((rows1-rows2,im2.shape[1]))),axis=0)

    # if none of these cases they are equal, no filling needed.

   

    return concatenate((im1,im2), axis=1)

   

   

def plot_matches(im1,im2,locs1,locs2,matchscores,show_below=True):

    """ Show a figure with lines joining the accepted matches

       input: im1,im2 (images as arrays), locs1,locs2 (feature locations),

       matchscores (as output from 'match()'),

       show_below (if images should be shown below matches). """

   

    im3 = appendimages(im1,im2)

    if show_below:

        im3 = vstack((im3,im3))

   

    imshow(im3)

   

    cols1 = im1.shape[1]

    for i,m in enumerate(matchscores):

        if m>0:

            plot([locs1[i][1],locs2[m][1]+cols1],[locs1[i][0],locs2[m][0]],'c')

    axis('off')

import requests

import cv

r = requests.get('http://www.autoshowup.com/stockimg/gable-of-a-half-timbered-house-in-black-and-white-in-a-traditional-german-village.jpg')

with open('imported_pic.jpg','wb') as f:

   f.write(r.content)

#r = requests.get('http://www.free-macrame-patterns.com/image-files/diamond-stitch-medium.jpg')

#with open('imported_pic.jpg','wb') as f:

#   f.write(r.content)

#imcolor = cv.LoadImage('lady_in_red_big.jpg')

#image = cv.LoadImage('lady_in_red_big.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)

imcolor = cv.LoadImage('imported_pic.jpg')

image = cv.LoadImage('imported_pic.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)

cornerMap = cv.CreateMat(image.height, image.width, cv.CV_32FC1)

# OpenCV corner detection

cv.CornerHarris(image,cornerMap,3)

for y in range(0, image.height):

    for x in range(0, image.width):

        harris = cv.Get2D(cornerMap, y, x) # get the x,y value

  # check the corner detector response

        if harris[0] > 10e-06:

    # draw a small circle on the original image

            cv.Circle(imcolor,(x,y),1,cv.RGB(35, 0,165))

cv.NamedWindow('Harris Corner Image', cv.CV_WINDOW_AUTOSIZE)

cv.ShowImage('Harris Corner Image', imcolor) # show the image

cv.SaveImage('harris_corner_image.jpg', imcolor)

cv.WaitKey()

from PIL import Image

from pylab import *

from numpy import *

from scipy.ndimage import filters

def compute_harris_response(im,sigma=3):

    """ Compute the Harris corner detector response function

       for each pixel in a graylevel image. """

   

    # derivatives

    imx = zeros(im.shape)

    filters.gaussian_filter(im, (sigma,sigma), (0,1), imx)

    imy = zeros(im.shape)

    filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)

   

    # compute components of the Harris matrix

    Wxx = filters.gaussian_filter(imx*imx,sigma)

    Wxy = filters.gaussian_filter(imx*imy,sigma)

    Wyy = filters.gaussian_filter(imy*imy,sigma)

   

    # determinant and trace

    Wdet = Wxx*Wyy - Wxy**2

    Wtr = Wxx + Wyy

   

    return Wdet / (Wtr*Wtr)

   

   

def get_harris_points(harrisim,min_dist=10,threshold=0.1):

    """ Return corners from a Harris response image

       min_dist is the minimum number of pixels separating

       corners and image boundary. """

   

    # find top corner candidates above a threshold

    corner_threshold = harrisim.max() * threshold

    harrisim_t = (harrisim > corner_threshold) * 1

   

    # get coordinates of candidates

    coords = array(harrisim_t.nonzero()).T

   

    # ...and their values

    candidate_values = [harrisim[c[0],c[1]] for c in coords]

   

    # sort candidates

    index = argsort(candidate_values)

   

    # store allowed point locations in array

    allowed_locations = zeros(harrisim.shape)

    allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1

   

    # select the best points taking min_distance into account

    filtered_coords = []

    for i in index:

        if allowed_locations[coords[i,0],coords[i,1]] == 1:

            filtered_coords.append(coords[i])

            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),

                        (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0

   

    return filtered_coords

   

   

def plot_harris_points(image,filtered_coords):

    """ Plots corners found in image. """

   

    figure()

    gray()

    imshow(image)

    plot([p[1] for p in filtered_coords],

                [p[0] for p in filtered_coords],'*')

    axis('off')

    show()

   

def get_descriptors(image,filtered_coords,wid=5):

    """ For each point return pixel values around the point

       using a neighbourhood of width 2*wid+1. (Assume points are

       extracted with min_distance > wid). """

   

    desc = []

    for coords in filtered_coords:

        patch = image[coords[0]-wid:coords[0]+wid+1,

                            coords[1]-wid:coords[1]+wid+1].flatten()

        desc.append(patch)

   

    return desc

def match(desc1,desc2,threshold=0.5):

    """ For each corner point descriptor in the first image,

       select its match to second image using

       normalized cross correlation. """

   

    n = len(desc1[0])

   

    # pair-wise distances

    d = -ones((len(desc1),len(desc2)))

    for i in range(len(desc1)):

        for j in range(len(desc2)):

            d1 = (desc1[i] - mean(desc1[i])) / std(desc1[i])

            d2 = (desc2[j] - mean(desc2[j])) / std(desc2[j])

            ncc_value = sum(d1 * d2) / (n-1)

            if ncc_value > threshold:

                d[i,j] = ncc_value

           

    ndx = argsort(-d)

    matchscores = ndx[:,0]

   

    return matchscores

def match_twosided(desc1,desc2,threshold=0.5):

    """ Two-sided symmetric version of match(). """

   

    matches_12 = match(desc1,desc2,threshold)

    matches_21 = match(desc2,desc1,threshold)

   

    ndx_12 = where(matches_12 >= 0)[0]

   

    # remove matches that are not symmetric

    for n in ndx_12:

        if matches_21[matches_12[n]] != n:

            matches_12[n] = -1

   

    return matches_12

def appendimages(im1,im2):

    """ Return a new image that appends the two images side-by-side. """

   

    # select the image with the fewest rows and fill in enough empty rows

    rows1 = im1.shape[0]   

    rows2 = im2.shape[0]

   

    if rows1 < rows2:

        im1 = concatenate((im1,zeros((rows2-rows1,im1.shape[1]))),axis=0)

    elif rows1 > rows2:

        im2 = concatenate((im2,zeros((rows1-rows2,im2.shape[1]))),axis=0)

    # if none of these cases they are equal, no filling needed.

   

    return concatenate((im1,im2), axis=1)

   

   

def plot_matches(im1,im2,locs1,locs2,matchscores,show_below=True):

    """ Show a figure with lines joining the accepted matches

       input: im1,im2 (images as arrays), locs1,locs2 (feature locations),

       matchscores (as output from 'match()'),

       show_below (if images should be shown below matches). """

   

    im3 = appendimages(im1,im2)

    if show_below:

        im3 = vstack((im3,im3))

   

    imshow(im3)

   

    cols1 = im1.shape[1]

    for i,m in enumerate(matchscores):

        if m>0:

            plot([locs1[i][1],locs2[m][1]+cols1],[locs1[i][0],locs2[m][0]],'c')

    axis('off')
