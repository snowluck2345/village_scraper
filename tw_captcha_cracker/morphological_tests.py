import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('human6.png',0)

ret,thresh4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(thresh4,240,255,cv2.THRESH_TOZERO_INV)


kernel = np.ones((2,2),np.uint8)
erosion = cv2.erode(thresh5,kernel,iterations = 1)

dilation = cv2.dilate(erosion,kernel,iterations = 1)
closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('test6-2.jpg', closing)


plt.imshow(closing, 'gray')
plt.show()