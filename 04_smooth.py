'''
python-opencv tutorial
Create trackbar control.
Usage:
	04_smooth.py imagename
'''

#import opencv library
import cv2
import sys
import numpy

argvs=sys.argv
if (len(argvs) != 2):
    print 'Usage: # python %s filename' % argvs[0]
    quit()
 

imagefilename = argvs[1]
try:
	img=cv2.imread(imagefilename, 1)
except:
	print 'faild to load %s' % imagefilename
	quit()

#GaussianBlur(...)
#    GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst
# ksize must pair of odd. (5,5),(7,7),(9,9)...
bluredimg=cv2.GaussianBlur(img,(11,11),0)

cv2.imshow('Gaussian',bluredimg)
cv2.imshow('Source',img)

cv2.waitKey(0)


cv2.destroyAllWindows() 




				
