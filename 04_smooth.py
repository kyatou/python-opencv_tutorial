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



cv2.destroyAllWindows() 




				
