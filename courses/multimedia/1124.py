# 경영수학 - 실용적인 부분
# 경제수학 - 학문적인 방향

import cv2 as cv
import sys


# print("test")
img = cv.imread('/Users/comedumac21/cv/study/courses/multimedia/soccer.jpg')
cv.imshow('Original',img)


temp = np.zeros((r,c))
gray = np.zeros((r,c))

for i ...
    for j ...
        temp[i,j] = 0.299*red[] 
                    + 0.587*green[] 
                    + 0.114*blue[]

# 내가 만들어 볼것 
# gray() = cv.cvtColor()
# cv.Sobel()

cv.waitKey()