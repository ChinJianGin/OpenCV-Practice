import numpy as np
import cv2 as cv
import os
import random

canvas = np.zeros((255,510,3), dtype='uint8')

for x in range(255):
    cv.line(canvas,(x,0), (x,255), (0,0,x))
    cv.line(canvas, (509-x, 0), (509-x, 255), (0, 0, x))

f = os.popen('cat /proc/cpuinfo | grep \'model name\' | uniq | cut -c 14-')
m = os.popen('cat /proc/meminfo | grep MemFree')

cpu = f.read()[:-1]
memfree = m.read()[:-1]

print(cpu)
print(memfree)

cv.rectangle(canvas, (45,156), (450,95), (255,255,255), -1)

font = cv.FONT_HERSHEY_PLAIN

cv.putText(canvas,cpu,(60,123),font,1,(0,0,0),2,cv.LINE_AA)
cv.putText(canvas,memfree,(60,145),font,1,(0,0,0),2,cv.LINE_AA)

cv.imshow('Canvas', canvas)

path = '/home/gin/VSCode/python-opencv/Photos'
cv.imwrite(os.path.join(path,'newimage.jpg'), canvas)

cv.waitKey(5000)