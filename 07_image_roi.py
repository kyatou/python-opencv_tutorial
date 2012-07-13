'''
python-opencv tutorial
Create image ROI(Region of Interest)
Usage:
    07_image_roi.py imagename
  
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

imgshape=img.shape
roiWidth=imgshape[1]/4
roiHeight=imgshape[0]/4
sx=imgshape[1]/2-roiWidth
sy=imgshape[0]/2-roiHeight
ex=imgshape[1]/2+roiWidth
ey=imgshape[0]/2+roiHeight

#extract roi as array
roi=img[sy:ey,sx:ex]

#invert roi area
img[sy:ey,sx:ex]=cv2.bitwise_not(roi)

cv2.imshow('roi image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
				
