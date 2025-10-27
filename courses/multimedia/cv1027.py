import numpy
import cv2 as cv

img = cv.imread('soccer.jpg')
print(img.shape)
print("1")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print("2")


cv.imshow('',gray)
print("3")
cv.waitKey(0)