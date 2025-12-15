import numpy as np
import cv2 as cv

num = np.array([4, 9, 1, 7, 50])
print(num)

num_sort = np.sort(num)
print(num_sort)

num_median = np.median(num_sort)
print(num_median)