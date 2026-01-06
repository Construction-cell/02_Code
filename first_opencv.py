import cv2
import numpy as np

# 1. 创建一张黑色图片
img = np.zeros((480, 640, 3), dtype=np.uint8)

# 2. 画一条巡线（黑色）
cv2.line(img, (100, 400), (540, 400), (0, 0, 0), 20)

# 3. 画小车（红色矩形）
cv2.rectangle(img, (320, 350), (340, 370), (0, 0, 255), -1)

# 4. 添加文字
cv2.putText(img, 'Smart Car Simulation', (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 5. 显示图片
cv2.imshow('Smart Car', img)

# 6. 保存图片
cv2.imwrite('car_simulation.jpg', img)

print("按任意键退出...")
cv2.waitKey(0)
cv2.destroyAllWindows()