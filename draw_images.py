import cv2 as cv

import numpy as np

# create blank image
# height width and number of color channels
blank=np.zeros((500,500,3), dtype='uint8')

# paint the image a certain color
blank[:]=255,0,0

# draw rectangle
# parameters-> Initial point, ending point, color, thickness
cv.rectangle(blank,(0,0),(250,250), (0,255,0), thickness=2)

# show in window
cv.imshow('Blank', blank)

cv.waitKey(0)