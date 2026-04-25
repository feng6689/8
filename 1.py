import cv2
import numpy as np

# 创建浅蓝色背景图片 (BGR格式)
width, height = 800, 600
img = np.zeros((height, width, 3), dtype=np.uint8)
img[:] = (255, 200, 150)  # 浅蓝色背景

# 绘制绿色正三角形
side_length = 100
center1 = (200, 200)
# 计算正三角形三个顶点
h = int(side_length * np.sqrt(3) / 2)
tri1_points = np.array([
    [center1[0], center1[1] - h//2],
    [center1[0] - side_length//2, center1[1] + h//2],
    [center1[0] + side_length//2, center1[1] + h//2]
], np.int32)
cv2.fillPoly(img, [tri1_points], (0, 255, 0))  # 绿色

# 绘制黑色正三角形
center2 = (600, 200)
tri2_points = np.array([
    [center2[0], center2[1] - h//2],
    [center2[0] - side_length//2, center2[1] + h//2],
    [center2[0] + side_length//2, center2[1] + h//2]
], np.int32)
cv2.fillPoly(img, [tri2_points], (0, 0, 0))  # 黑色

# 绘制顶角120度的等腰三角形（紫色）
# 等腰三角形，顶角120度，底角30度
base_length = 120
# 计算高：高 = 底/2 * tan(30°) = 底/2 * (1/√3)
iso_height = int((base_length / 2) * (1 / np.sqrt(3)))
center3 = (400, 350)
iso_tri_points = np.array([
    [center3[0], center3[1] - iso_height],  # 顶角
    [center3[0] - base_length//2, center3[1] + iso_height],  # 左下角
    [center3[0] + base_length//2, center3[1] + iso_height]   # 右下角
], np.int32)
cv2.fillPoly(img, [iso_tri_points], (255, 0, 255))  # 紫色

# 绘制粉色圆形
center4 = (400, 150)
radius = 50
cv2.circle(img, center4, radius, (203, 192, 255), -1)  # 粉色

# 保存为1.jpg
cv2.imwrite('1.jpg', img)
print('图片已保存为1.jpg')
