'''
python-opencv tutorial
Load image file from disk.
Usage:
	00_loadImage.py imagefile
'''
#coding:utf-8


#import opencv library
import cv2
import sys

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

#show image
windowName= 'LoadImage'
cv2.imshow(windowName, img)
print 'Press any key to exit.'

cv2.waitKey(0)

  
