import cv2
import numpy as np

# 把彩色图像转换为灰色图像
# 并看看灰度图像在计算机又是怎么样表示得

# 1. 读取彩色图像
rgb_cat = cv2.imread('images/cat.png')
# 2. 把彩色图像转换为灰度图像
gary_cat = cv2.cvtColor(rgb_cat,cv2.COLOR_BGR2GRAY)

print(gary_cat)
print(gary_cat.shape)

cv2.imwrite('images/gary_cat.png', gary_cat)