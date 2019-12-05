'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Fourier Transform Application
Date: 2019. 11. 29. (금) 10:52:16 KST
Video Lecture(s):
link(s):
    [1] https://docs.google.com/document/d/14QZo1Xo1To-J-q96D05ntvMnC1u2m2mGuk_MIFZHvqo/pub

Reference(s):
    [1] http://www.stemapks.com/opencv_python.html


NB: Some examples of filters used: Box, Guassian, Laplace
'''

tut09_changiing_pic_name.py

#!/usr/bin/env python

import subprocess

import argparse

# parse command line arguments

parser = argparse.ArgumentParser(description='Batch change filenames.')

parser.add_argument('inputFileName', metavar='baseNameIn')

parser.add_argument('outputFileName', metavar='baseNameOut')

args = parser.parse_args()

# Run a bash cmd and send output to a list separated by line

def runBash(cmd):

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        out = p.stdout.read().strip()

        return out.split('\n')

# Change new function

def changePictureName(oldPictureName, newPictureNameBase):

        temp    = oldPictureName.split('.')

        newPictureName = newPictureNameBase + '.' + temp[1] + '.' + temp[2]

        subprocess.call(["mv", oldPictureName, newPictureName])

# Change names of all files matching base

def changeAllPictureNames(oldPictureNameBase, newPictureNameBase):

        files = runBash("ls")

        for afile in files:

                if afile.split('.')[0] == oldPictureNameBase:

                        changePictureName(afile, newPictureNameBase)

changeAllPictureNames(args.inputFileName, args.outputFileName)

groupPictureRenameRE.py

#!/usr/bin/env python

import subprocess

import argparse

import re

# parse command line arguments

parser = argparse.ArgumentParser(description='Batch change filenames.')

parser.add_argument('inputFileName', metavar='baseNameIn')

parser.add_argument('outputFileName', metavar='baseNameOut')

args = parser.parse_args()

# Run a bash cmd and send output to a list separated by line

def runBash(cmd):

 p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

 out = p.stdout.read().strip()

 return out.split('\n')

# Change new function

def changePictureName(oldPictureName, newPictureNameBase):

 temp    = re.split('([0-9]+)', oldPictureName)

 newPictureName = newPictureNameBase  + temp[1] + temp[2]

 subprocess.call(["mv", oldPictureName, newPictureName])

# Change names of all files matching base

def changeAllPictureNames(oldPictureNameBase, newPictureNameBase):

 files = runBash("ls")

 for afile in files:

  temp = re.split('([0-9]+)', afile)

  if temp[0] == oldPictureNameBase:

   changePictureName(afile, newPictureNameBase)

changeAllPictureNames(args.inputFileName,args.outputFileName)
