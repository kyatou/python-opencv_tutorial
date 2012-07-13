'''
python-opencv tutorial
Create trackbar control.

Usage:
	03_trackbar.py

   copyright Kouji Yatou <kouji.yatou@gmail.com>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

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




				
