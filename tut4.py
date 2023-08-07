import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    img=cv2.line(frame, (0,0), (width,height), (0,255,2), 3)
    img=cv2.line(img, (0,height), (width,0), (0,255,2), 3)
    # DRAWING A LINE: (imgname, points to draw line, color, thickness of line)

    img=cv2.rectangle(img, (100,140), (170,90), (0,255,2), 2)
    # DRAWING A RECTANGLE: (imgname, top-left, bottom-right, color, thickness)
    # thickness -1 for complete fill

    img=cv2.circle(img, (700,100), 20, (255, 192, 203), -1)

    # text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img, "Hi, I am Gunjan!", (200,(height-100)), font, 4, (255, 192, 203), 6, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1)==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()