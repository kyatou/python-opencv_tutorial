'''
python-opencv tutorial
Create new blank two image(grayscale and fullcolor).
Draw a rectangle to grayscale image, draw a circle to fullcolor image.
Usage:
	02_makeImage.py


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


'''
zeros(...)
    zeros(shape, dtype=float, order='C')    
    Return a new array of given shape and type, filled with zeros.
    
    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.    
    Returns
    -------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.
'''

#create new image data
imgwidth=640
imgheight=480
grayscaleimage = numpy.zeros((imgheight,imgwidth), numpy.uint8)
fullcolorimage = numpy.zeros((imgheight,imgwidth,3),numpy.uint8)


#draw rectangle and circle

#rectangle(...)
#    rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> None
x1=100
y1=100
x2=400
y2=400
color=(255,255,255)
cv2.rectangle(grayscaleimage, (x1, y1), (x2, y2), color, 2)

#circle(...)
#    circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> None
color=(0,255,0)	#Blue,Green,Red
thickness=5
cv2.circle(fullcolorimage,(imgwidth/2,imgheight/2),100,color,thickness)

#Show image
wnGrayScale='Gray Scale'
wnFullColor='Full Color'
cv2.imshow(wnGrayScale,grayscaleimage)
cv2.imshow(wnFullColor,fullcolorimage)

#moveWindow(...)
#    moveWindow(winname, x, y) -> None
cv2.moveWindow(wnFullColor,imgwidth,0)

print 'Press any key to exit.'

cv2.waitKey(0)

  
