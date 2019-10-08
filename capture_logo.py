import cv2
import glob as gb
import numpy as np
import os

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    cv2.imshow("PREVIEW CAM", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('starbuko_logo/logo1.jpg',frame)
        break

cam.release()
cv2.destroyAllWindows()