import numpy as np
import cv2

image = np.zeros((300,400),np.uint8)
image.fill(200)

cv2.imshow("Window Title",image)
cv2.waitKey(1000)

