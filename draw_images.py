import cv2 as cv

import numpy as np

# create blank image
# height width and number of color channels
blank=np.zeros((500,500,3), dtype='uint8')

# paint the image a certain color
blank[:]=255,0,0

# draw rectangle
# parameters-> Initial point, ending point, color, thickness
# cv.FILLED or -1
# cv.rectangle(blank,(0,0),(250,250), (0,255,0), thickness=cv.FILLED)

# scaled the rectangle to half of original image
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)


# draw circle
cv.circle(blank, center=(blank.shape[1]//2,blank.shape[0]//2), radius=40, color=(0,0,255), thickness=3)

# draw line
cv.line(blank, pt1=(0,0), pt2=(blank.shape[1]//2,blank.shape[0]//2), color=(255,255,255),thickness=3)

# write text on image
cv.putText(blank,text="Hello there",org=(400,400), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0,255,0),thickness=2)

# show in window
cv.imshow('Blank', blank)

cv.waitKey(0)