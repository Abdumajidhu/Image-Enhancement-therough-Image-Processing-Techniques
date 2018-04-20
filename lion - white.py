# import opencv
import numpy as np
import cv2
 
# Read image
src = cv2.imread("exercise_images/lion.jpg",0)
 
# Set threshold and maxValue
thresh = 25
thresh3 = 255
thresh4 = 205
thresh5 = 105
thresh2 = 155

maxValue = 255
 
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);
th, dsts = cv2.threshold(src, thresh2, maxValue, cv2.THRESH_BINARY);
th, dsts1 = cv2.threshold(src, thresh3, maxValue, cv2.THRESH_BINARY);
th, dsts2 = cv2.threshold(src, thresh4, maxValue, cv2.THRESH_BINARY);
th, dsts3 = cv2.threshold(src, thresh5, maxValue, cv2.THRESH_BINARY);
improved = np.hstack((src,dsts)) #stacking images side-by-side
improvedmore = np.hstack((src,dsts)) #stacking images side-by-side
imp = np.hstack((dst,dsts)) #stacking images side-by-side


cv2.imshow('Have You of 165',dst)
cv2.imshow('Got You of 155',dsts2)
cv2.imshow('Have You of 255',dsts3)
cv2.imshow('Got You of 205',dsts1)
cv2.imshow('Have You of 100',dsts)
cv2.imwrite('doc.jpeg',improved)
cv2.imwrite('doc2.jpeg',improvedmore)
cv2.imwrite('alike.jpeg',imp)


#cv2.imshow('Image',src)
