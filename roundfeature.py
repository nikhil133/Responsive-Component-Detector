# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2

img=cv2.imread('C:/Users/Nikhil/Desktop/test1.jpg')
filtered=cv2.pyrMeanShiftFiltering(img,1,3)
grey=cv2.cvtColor(filtered,cv2.COLOR_BGR2GRAY)
#m,n=grey.shape
#for i in range(0,m):
 ##   for j in range(0,n):
   #         if grey[i][j]>=138 and grey[i][j]<=166:
    #                    grey[i][j]=255 
     #       else:             
      #          grey[i][j]
edge=cv2.Canny(grey,cv2.THRESH_BINARY,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

ret, thresh = cv2.threshold(edge,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, contours,_ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contour_list=[]
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 7) & (len(approx) < 15) &(area >110) ):
        contour_list.append(contour)
        cv2.drawContours(img, contour_list,  -1, (255,0,0), 2)
#print(" %d"%len(contours))
#cv2.drawContours(img,contours,50,(0,0,255),10)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()