import numpy as np
import cv2 as cv

# 1. 3채널 이미지를 
# 2. numpy를 이용해서, img를 잘라 본다.
# 3. 그게 익숙해지면, 행(r),열(c) 번호를 입력받아서 부분부분 출력하는거 까지.

img = cv.imread('soccer.jpg')
# cv.split
# b,g,r = cv.split(img)

# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)


# numpy로 버퍼 만들어서 해보기

# bufnp = np.array(img)
bufnp =np.copy(img)
print(" bufnp : ",bufnp.shape)

# bImg=img[:,:,0]
# gImg=img[:,:,1]
# rImg=img[:,:,2]

print("img.shape : ",img.shape)
# print("blue : ",bImg.shape)
# print("green : ",gImg.shape)
# print("red : ",rImg.shape)
# cv.imshow('',gray)
# cv.imshow('blue',bImg)
# cv.imshow('green',gImg)
# cv.imshow('red',rImg)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # imgB = cv.imread()
# print(type(img))


# cv.waitKey(0)