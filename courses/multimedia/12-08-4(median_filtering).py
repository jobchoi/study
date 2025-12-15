import numpy as np
import cv2 as cv
from imgaug import augmenters as iaa

def my_gray(img):
    img_R=img[:,:,2]*0.299
    img_G=img[:,:,1]*0.587
    img_B=img[:,:,0]*0.114

    img_GRAY=img_R+img_G+img_B
    img_uint8=np.uint8(img_GRAY)

    return img_uint8

im = cv.imread('soccer.jpg')

im_arr = np.asarray(im)
aug = iaa.SaltAndPepper(p = 0.05)
im_arr = aug.augment_image(im_arr)

gim = my_gray(im)
gim_arr = np.asarray(gim)
gim_arr = aug.augment_image(gim_arr)

cv.imshow('color_y', im_arr)
cv.imshow('gray_n', gim)
cv.imshow('gray_y', gim_arr)

h, w = gim_arr.shape
print(h, w)

fngimg = np.zeros((h, w))

for i in range(h):
    for j in range(2, w-2):
        # pimg = np.array(gim_arr[i, j-2:j+3])
        pimg = gim_arr[i, j-2:j+3]
        pimg_sort = np.sort(pimg)
        fngimg[i, j] = np.median(pimg_sort)

fngimg_uint8=np.uint8(fngimg)

cv.imshow('median_filter', fngimg_uint8)

cv.waitKey()
cv.destroyAllWindows()