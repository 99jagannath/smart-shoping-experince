from imutils import paths
import argparse
import time
import sys
import cv2
import os
def dhash(image, hashSize=8):
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hashSize + 1, hashSize))
	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]
	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
# construct the argument parse and parse the arguments
image1 = cv2.imread('cat.33.jpg',1)
image2 = cv2.imread('2.jpeg',1)
image3 = cv2.imread('1.jpeg',1)
cv2.imshow('original image1',image1)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
imageHash1= dhash(image1)
cv2.imshow('original image2',image2)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
imageHash2= dhash(image2)
cv2.imshow('original image3',image3)
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
imageHash3= dhash(image3)
print(type(imageHash1))
print(imageHash2)
print(imageHash3)
print(imageHash2-imageHash3)
print(imageHash2-imageHash1)
cv2.waitKey(0)