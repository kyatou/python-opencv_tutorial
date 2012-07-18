'''
python-opencv tutorial
Make gaussian pyramid
Usage:
	05_GaussianPyramid.py

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

imgwidth=800
imgheight=800
img_original= numpy.zeros((imgheight,imgwidth,1),numpy.uint8)

#draw some circle
for i in range(1,6):
	cv2.circle(img_original,(20*2**i,20*2**i),i*10,(255,255,255),2)

#pyrDown(...)
#   pyrDown(src[, dst[, dstsize[, borderType]]]) -> dst

#make half size and quater size
img_half=cv2.pyrDown(img_original)
img_quat=cv2.pyrDown(img_half)

cv2.imshow('original',img_original)
cv2.imshow('Half size',img_half)
cv2.imshow('Quater size',img_quat)

cv2.waitKey()
cv2.destroyAllWindows() 

