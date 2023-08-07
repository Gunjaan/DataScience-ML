import cv2
import random

img = cv2.imread('assets/naruto.jpeg', -1)

# print(img.shape) 
# (266, 190, 3) -> height, width, channels

# print(img[252][50:400])

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]


# CUTTING A PART OF IMAGE AND PLACING IT AT SOME OTHER LOCATION IN THE IMAGE
tag= img[100:150, 50:100]
img[40:90, 30:80] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()