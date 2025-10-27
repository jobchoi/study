import numpy as np
import cv2 as cv

# 1. 3채널 이미지를 
# 2. numpy를 이용해서, img를 잘라 본다.
# 3. 그게 익숙해지면, 행(r),열(c) 번호를 입력받아서 부분부분 출력하는거 까지.

def myGray(imgCp):
    fimg = np.array(imgCp)

    if fimg is None:
        print("no img")
    else :
        print("len : ",len(imgCp[:,:,0]))    

        bimgTr = imgCp[:,:,0] * 0.114    
        gimgTr = imgCp[:,:,1] * 0.587
        rimgTr = imgCp[:,:,2] * 0.299

        totalImg = np.uint8(bimgTr + gimgTr +rimgTr)  

        cv.imshow('',totalImg)

        cv.waitKey()


img = cv.imread('soccer.jpg')
# cv.split
# b,g,r = cv.split(img)

# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)


# numpy로 버퍼 만들어서 해보기

# bufnp = np.array(img)자
# bufnp =np.copy(img) # np를 쓸때는 copy.
# print(" bufnp : ",bufnp.shape)

# bImg=img[:,:,0]
# gImg=img[:,:,1]
# rImg=img[:,:,2]

# print("img.shape : ",img.shape)
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


# 영역 나눠서 띄워보기
# cv.imshow('Upper left half',img[0:img.shape[0]//2, 
#                                 0:img.shape[1]//2, 
#                                 :])


# weighted average  : 0.299*R + 0.587*G + 0.114*B
# luminosity method :

# 0~255인지 0~1인지 파일을 읽어서 확인

# cv.imshow('center',
#           img[
#               img.shape[0]//4:
#               3*img.shape[0]//4,img.shape[1]//4:
#               3*img.shape[1]//4,:
#               ])
myGray(img)


# cv.waitKey(0)

