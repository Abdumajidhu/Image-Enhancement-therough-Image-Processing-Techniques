import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('exercise_images/breakin.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

median = cv2.medianBlur(img,5)
gausian = cv2.GaussianBlur(img,(5,5),0)
blur = cv2.blur(img,(5,5))
bilateral = cv2.bilateralFilter(img,9,75,75)

median = cv2.medianBlur(img,5)
#cv2.imwrite('median.jpg',median)
blur = np.hstack((img,blur))
median = np.hstack((img,median))
gausian = np.hstack((img,gausian))
bilateral = np.hstack((img,bilateral))

cv2.imwrite('1blur.jpg',blur)
cv2.imwrite('2median.jpg',median)
cv2.imwrite('3gausianmedian.jpg',gausian)
cv2.imwrite('4bilateral.jpg',bilateral)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
#plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blured')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.imshow('Blur Blur',blur)
cv2.imshow('Median Blur',median)
cv2.imshow('Gausian Blur',gausian)
cv2.imshow('Bilateral Blur',bilateral)

