'''
python-opencv tutorial
Resize image to half size and
convert to gray scale image.
Usage:
	01_resize_and_convertColor.py imagefile
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


#define small image size
imgsize=img.shape

#(height,width,depth)

simg_width=imgsize[1]/2
simg_height=imgsize[0]/2


#half size and grayscale image
simg=cv2.resize(img,(simg_width,simg_height))
gimg=cv2.cvtColor(simg,cv2.COLOR_BGR2GRAY)

cv2.imshow('Half Size',simg)
cv2.imshow('GrayScale',gimg)

print 'Press any key to exit.'

cv2.waitKey(0)

  
