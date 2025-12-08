import cv2 as cv
import numpy as np
from imgaug import augmenters as iaa


# img = cv.imread('/Users/comedumac21/cv/study/courses/multimedia/soccer.jpg')

# gimg = 컬러 이미지를 흑백으로 

img = cv.imread('soccer.jpg')
gimg = cv.imread('soccer.jpg',cv.IMREAD_GRAYSCALE)

# img2 = np.asarray(img)
img2 = np.asarray(gimg)
aug = iaa.SaltAndPepper(p=0.05)
img2 = aug.augment_image(img2)
ngimg = aug.augment_image(img2)





d = img.shape
hCnt = 0
wCnt = 0
height = img.shape[0]
width = img.shape[1]

# print(f'total : {height * width}')
# print(f'height : {height}')
# print(f'width : {width}')

Total_px = 0 

for i in range(0, height, 1) :
    # for j in range(0, width, 1) :
    for j in range(2, width, -2) : # 필터 예제 적용해보기
        Total_px = Total_px +1

# print(f'totla px: {Total_px}')


# 문제
# range(2, w ||h , -2)
# numpy slicing [i,j-2:j+3] 
# pimg = 
# fngimg = np.zero)_ 
# median filtering 한 것을 넣는다. 


cv.imshow(ngimg)
# cv.imshow(fngimg) # 필터
# cv.imshow('test',img)
cv.imshow(img2)

# cv.waitKey()




# pgm 확장자, jpg, png포맷에서는 이미 압축이된것, pgm은 파일포맷 압축이 되지 않은 low format상태


# 새로운 변수를 하나 생성, 사이즈 5에 배열을 생성, 값을 중복되지 않는 무작위로 만들고 값을 대입
# numpy.median 함수 
# median 중앙이라는 뜻 -> 인덱스의 중간 
# 1. 만들때 numpy배열로 만든다.
# 2. 순서없이 믹싱된 값을 정렬(오름,내림이던 중요하지 않음)한다. 
# 3. 정렬된 값을 median메서드를 이용해 중간 값을 찾고, 내가 입력 했던 것과 같은지 비교해본다.

a = np.array(5)
a = [5,2,1,4,10]
print(a)

b = np.sort(a)[::-1]
print(f'정렬후 b : {b}')

c = np.median(b)    
print(f'c - median : {c}')