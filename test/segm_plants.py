# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 2   2 2 2 R

src = cv2.imread('E:/20200712/IMG_20200712_100857.jpg')
cv2.imshow('src', src)

#
fsrc = np.array(src, dtype=np.float32) / 255.0
(b, g, r) = cv2.split(fsrc)
gray = 2 * g - b - r

#       и минимальные значения
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# Рассчитайте гистограмму
hist = cv2.calcHist([gray], [0], None, [256], [minVal, maxVal])
plt.plot(hist)
plt.show()
cv2.waitKey()

# Преобразовать в тип U8, бинаризация OSU
gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
(thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
# plt.savefig("C:/Users/Admin/Desktop/1.jpg")
cv2.imwrite('C:/Users/Admin/Desktop/1.jpg', bin_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.imshow('bin_img', bin_img)

# Получить цветные изображения
(b8, g8, r8) = cv2.split(src)
color_img = cv2.merge([b8 & bin_img, g8 & bin_img, r8 & bin_img])
cv2.imwrite('C:/Users/Admin/Desktop/2.jpg', color_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.imshow('color_img', color_img)