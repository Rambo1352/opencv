import numpy as np
import cv2

images = [
    [[0, 0, 255], [0, 0, 255]],
    [[0, 255, 0], [0, 255, 0]],
    [[255, 0, 0], [255, 0, 0]],
]

image_array = np.array(images)

print(image_array)

cv2.imwrite('images/rgb_image.jpg', image_array)
