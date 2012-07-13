'''
python-opencv tutorial
Resize image to half size and
convert to gray scale image.
Usage:
	01_resize_and_convertColor.py imagefile


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

  
