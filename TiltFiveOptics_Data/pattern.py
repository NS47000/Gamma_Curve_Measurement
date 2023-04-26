import numpy as np
import cv2

img=np.zeros((720,1280,3),dtype=np.uint8)

line_pair=4
#mtf_v
"""

for i in range(0,1280):
    if i//line_pair%2==1:
        img[:,i]=255
cv2.imwrite("1280x720TestFile.png",img)
"""
"""
#mtf_h
for i in range(0,720):
    if i//line_pair%2==1:
        img[i,:]=255
cv2.imwrite("1280x720TestFile.png",img)

"""
"""
#cross_line
line_width=3
half_line_width=line_width//2
img[:,:]=255
img[360-half_line_width:360+half_line_width,:]=0
img[:,640-half_line_width:640+half_line_width]=0
cv2.imwrite("1280x720TestFile.png",img)
"""
img[:,:,:]=255
cv2.imwrite("1280x720TestFile.png",img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


