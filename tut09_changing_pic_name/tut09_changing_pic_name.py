'''
Author: Kwadwo Boateng Ofori-Amanfo
Purpose: Learn how to download a lot of images and change the file names automatically
Date: 2019. 11. 28. (목) 14:08:53 KST
Video Lecture(s): OpenCV Programming with Python on Linux Ubuntu Tutorial-9 Changing Names of Pictures
link(s):
    [1] 

Reference(s):
    [1] 

'''

#!/usr/bin/env python3

import subprocess
import argparse

# parse command line arguments

parser = argparse.ArgumentParser(description='Batch change filenames.')
parser.add_argument('inputFileName', metavar='baseNameIn')
parser.add_argument('outputFileName', metavar='baseNameOut')
args = parser.parse_args()

# Run a bash cmd and send output to a list separated by Line

def runBash(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out.split('\n')

# Change new function

def changePictureName(oldPictureName, newPictureNameBase):
    temp = oldPictureName.split('.')
    newPictureName = newPictureNameBase + '.' + temp[1] + '.' + temp[2]
    subprocess.call(["mv", oldPictureName, newPictureName])

# Change names of all files matching base

def changeAllPictureNames(oldPictureNameBase, newPictureNameBase):
    files = runBash("ls")

    for afile in files:
        if afile.split('.')[0] == oldPictureNameBase:
            changePictureName(afile, newPictureNameBase)




changeAllPictureNames(args.inputFileName, args.outputFileName)
                    
