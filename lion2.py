import numpy as np
import cv2
img = cv2.imread('exercise_images/lion.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res = np.hstack((img,cl1))
cv2.imwrite('newlion.jpg',res)

cv2.imshow('New',cl1)
cv2.imshow('Orignal',img)

#cv2.imwrite('clahe_2.jpg',cl1)
