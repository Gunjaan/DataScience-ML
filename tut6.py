# corner detection

import numpy as np
import cv2

img = cv2.imread('/Users/gunjan/Desktop/opencvtut/assets/naruto.jpeg')
# img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(img, 50, 0.1, 10)
# source image, number of corners, minimum quality, minimum euclidean distance

corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img, (x,y), 4, (255,0,0), lineType=2)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
