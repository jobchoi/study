# test_cv.py
import cv2
import numpy as np

# 빈 이미지(검정 배경) 만들기
img = np.zeros((300, 400, 3), dtype=np.uint8)

# 파란색 사각형 그리기
cv2.rectangle(img, (50, 50), (350, 250), (255, 0, 0), -1)

# 저장 (imshow 대신 파일로 확인)
cv2.imwrite("blue_rect.jpg", img)
print("✅ blue_rect.jpg 파일이 생성되었습니다.")
