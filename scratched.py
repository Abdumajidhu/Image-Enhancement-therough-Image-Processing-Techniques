import numpy as np
import cv2

img = cv2.imread('exercise_images/scratched_image.jpeg',0)
kernel = np.ones((6,6),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

ero = np.hstack((img,erosion))
dil = np.hstack((erosion,dilation))
ope = np.hstack((dilation,opening))

cv2.imwrite('erosion.jpeg',ero)
cv2.imwrite('dilation.jpeg',dil)
cv2.imwrite('opening.jpeg',ope)

cv2.imshow('Orignal',img)
cv2.imshow('Siok',erosion)
cv2.imshow('Dialation',dilation)
cv2.imshow('Opening',opening)



