'''
python-opencv tutorial
Encode and decode image data.
Usage:
  08_image_encode_decode.py imagename
  
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

#import opencv library
import cv2
import sys
import numpy

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


#encode to jpeg format
#encode param image quality 0 to 100. default:95
#if you want to shrink data size, choose low image quality.
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
result,encimg=cv2.imencode('.jpg',img,encode_param)
if False==result:
    print 'could not encode image!'
    quit()

#decode from jpeg format
decimg=cv2.imdecode(encimg,1)

cv2.imshow('Source Image',img)
cv2.imshow('Decoded image',decimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
                    
