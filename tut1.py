import cv2

img = cv2.imread('assets/naruto.jpeg', 0)
# -1: colored image, transparency discarded
# 0: grayscale
# +1: honors transparency, alpha channel

# DISPLAYING IMAGE
# cv2.imshow('image', img)
# cv2.waitKey(0) # 0 means make the window wait for infinite time until we press any key on keyboard
# cv2.destroyAllWindows()

# RESIZING THE IMAGE
# img = cv2.resize(img, (400, 400))
# or
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) # -> will multiply both height and width by 0.5

# ROTATING AN IMAGE
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# WRITING AN IMAGE: the process of saving an image file to disk after applying some image processing operations to it.

cv2.imwrite("new_img.png", img)

cv2.imshow('image', img)
cv2.waitKey(0) # 0 means make the window wait for infinite time until we press any key on keyboard
cv2.destroyAllWindows()