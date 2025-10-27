import numpy as np
import cv2 as cv

# 1. 3채널 이미지를 
# 2. numpy를 이용해서, img를 잘라 본다.
# 3. 그게 익숙해지면, 행(r),열(c) 번호를 입력받아서 부분부분 출력하는거 까지.

img = cv.imread('soccer.jpg')
# cv.split
# b,g,r = cv.split(img)

# numpy로 해보기
# test0=img[::0]
test1=img[:,:,1]
test2=img[:,:,2]
test0=img[:,:,0]

print("img.shape : ",img.shape)
print("test1.shape : ",test1.shape)
cv.imshow('t1',test1)
cv.imshow('t2',test2)
cv.imshow('t0',test0)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# imgB = cv.imread()
print(type(img))

# cv.imshow('',gray)
# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)

cv.waitKey(0)

