import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('/content/Anakapalli.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Original Map')
plt.show()

pixel = img_rgb[300, 400]  
print(f'Sample RGB pixel: {pixel}')


hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
plt.imshow(hsv)
plt.title('HSV Preview')
plt.show()
