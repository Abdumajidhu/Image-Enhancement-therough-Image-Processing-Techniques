# import opencv
import numpy as np
import cv2
 
# Read image
src = cv2.imread("exercise_images/document.jpeg",0)
 
# Set threshold and maxValue
thresh = 165
thresh2 = 155

maxValue = 255
 
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);
th, dsts = cv2.threshold(src, thresh2, maxValue, cv2.THRESH_BINARY);
improved = np.hstack((src,dsts)) #stacking images side-by-side
improvedmore = np.hstack((src,dsts)) #stacking images side-by-side
imp = np.hstack((dst,dsts)) #stacking images side-by-side


cv2.imshow('Thresh of 165',dst)
cv2.imshow('Thresh of 155',dsts)
cv2.imwrite('doc.jpeg',improved)
cv2.imwrite('doc2.jpeg',improvedmore)
cv2.imwrite('alike.jpeg',imp)


#cv2.imshow('Image',src)
