import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

print('hello')

video = cv2.VideoCapture('mitosiscell360.mp4')
(check, I) = video.read()

while True:
    cv2.imshow("frame", I)

    # This delays while waiting for a key to be pressed
    key = cv2.waitKey(50)

    # if the 'q' key is pressed, quit:
    if key == ord("q"):
         break

    # Next Frame:
    (check, I) = video.read()

video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()