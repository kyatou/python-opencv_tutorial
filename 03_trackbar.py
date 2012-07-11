'''
python-opencv tutorial
Create trackbar control.

Usage:
	03_trackbar.py
'''

#import opencv library
import cv2
import numpy

#Trackbar callback function
def onTrackbarChange(trackbarValue):
	imgshape=fullcolorimage.shape
	fimg=numpy.zeros(imgshape,numpy.uint8)
	colorval=trackbarValue*10
	diff=trackbarValue*10
	xcenter=imgshape[1]/2
	ycenter=imgshape[0]/2
	color=(colorval,colorval,colorval)
	cv2.rectangle(fimg, (xcenter-diff, ycenter-diff), (xcenter+diff, ycenter+diff), color, -1)
	cv2.imshow(windowName, fimg)

imgwidth=640
imgheight=480
fullcolorimage = numpy.zeros((imgheight,imgwidth,3),numpy.uint8)

windowName="TrackbarSample"
cv2.namedWindow(windowName)
onTrackbarChange(0)

#createTrackbar(...)
#    createTrackbar(trackbarName, windowName, value, count, onChange) -> None
cv2.createTrackbar( 'Trackbarname', windowName, 0, 25, onTrackbarChange )

cv2.waitKey()
cv2.destroyAllWindows() 




				
