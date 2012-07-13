'''
python-opencv tutorial
Get image from web camera
Usage:
	06_webcamera.py

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


#VideoCapture(...)
#      VideoCapture() -> <VideoCapture object>
#  or  VideoCapture(filename) -> <VideoCapture object>
#  or  VideoCapture(device) -> <VideoCapture object>

#get capture object
cameraid=0
capture=cv2.VideoCapture(cameraid)

isopen=capture.isOpened()
if(False==isopen):
    #retry to open camera
    capture.open(cameraid)
    isopen=capture.isOpened()
    if(False==isopen):
        #could not open camera...
        print 'Could not open camera.' 
	exit()

#get camera attribute
imwidth=capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
imheight=capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
print 'img width %d height %d ' % (imwidth,imheight)

print 'press ESC or q to quit'

#capture image and display to monitor
while True:
    ret,frame=capture.read()
    if not ret:
        print 'Could not capture frame.'
        exit()

    cv2.imshow('Captured Frame',frame)
    inputkey=cv2.waitKey(100)
    c=chr(inputkey & 255)
    if c in ['q',chr(27)]:
	break

#release capture
if(capture.isOpened()):
    capture.release()

cv2.destroyAllWindows() 
