import cv2 as cv

img = cv.imread('soccer.jpg')

cv.imshow('', img)

h, w, l = img.shape
print(h, w, l)

print(w*h)

p = 0

for i in range(h):
    for j in range(w):
        p += 1

print(p)

cv.waitKey()
cv.destroyAllWindows()