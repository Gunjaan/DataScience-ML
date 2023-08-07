import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # ret is used to return if the camera is available
    width=int(cap.get(3))
    height=int(cap.get(4))
    # properties of cap. (3 for width, 4 for height)

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame



    cv2.imshow("frame", image)

    if cv2.waitKey(1) == ord('q'):
      break
    # enter q to quit the window

cap.release()
cv2.destroyAllWindows()