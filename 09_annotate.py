'''
python-opencv tutorial
Annotate message to image.
Usage:
  09_annotate.py imagename
  
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


#putText(...)
#    putText(img, text, org, fontFace, fontScale, color[, thickness[, linetype[, bottomLeftOrigin]]]) -> None

msg='HELLO,OpenCV!'
location=(0,30)

fontface=cv2.FONT_HERSHEY_PLAIN
fontscale=1.0
color=(255,190,0) #sky blue
cv2.putText(img,msg,location,fontface,fontscale,color)


#big size
fontscale=2.0
location=(0,img.shape[0]/2)
thickness=2
cv2.putText(img,msg,location,fontface,fontscale,color,thickness)

cv2.imshow('Annotated Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
                    
