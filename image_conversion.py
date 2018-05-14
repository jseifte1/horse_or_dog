import cv2
import numpy as np
import copy
import os

for filename in os.listdir('dogs'):
    img_in = cv2.imread('dogs/' + filename, 1)
    cv2.imwrite('dogs_png/' + filename[:-4] + '.png', img_in)

i = 0
for filename in os.listdir('horses'):
    img_in = cv2.imread('horses/' + filename, 1)
    cv2.imwrite('horses_png/' + 'horse.' +  str(i) + '.png', img_in)
    i = i + 1