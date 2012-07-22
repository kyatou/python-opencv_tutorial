'''
python-opencv tutorial
Example of mouse callback
draw a circle or rectangle to clicked point.

Usage:
  10_mouse_callback.py imagename
  
  Copyright Kouji Yatou <kouji.yatou@gmail.com>

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

import cv2
import sys

argvs=sys.argv
if (len(argvs) != 2):
    print 'Usage: # python %s imagefilename' % argvs[0]
    quit()
 
imagefilename = argvs[1]
try:
     img=cv2.imread(imagefilename, 1)
except:
     print 'faild to load %s' % imagefilename
     quit()

usage='left click to draw a circle.\nright click to draw a rectangle.\n'
usage=usage+'press any key to exit.'
print(usage)



windowName="mouse"
cv2.namedWindow(windowName)
  
def onMouse(event, x, y, flags, param):
     """
        Mouse event callback function.
        left click -> draw circle
        right click -> draw rectangle
     """ 
     if event == cv2.EVENT_MOUSEMOVE:return 
 
     if event == cv2.EVENT_LBUTTONDOWN:
         center=(x,y) 
         radius=10
         color=(255,255,0)
         cv2.circle(img,center,radius,color)
     
     if event == cv2.EVENT_RBUTTONDOWN:
         rect_start=(x-10,y-10)
         rect_end=(x+10,y+10)
         color=(100,255,100)
         cv2.rectangle(img,rect_start,rect_end,color)

     cv2.imshow(windowName,img)


#setMouseCallback(...)
#    setMouseCallback(windowName, onMouse [, param]) -> None
cv2.setMouseCallback(windowName,onMouse)

cv2.imshow(windowName,img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

