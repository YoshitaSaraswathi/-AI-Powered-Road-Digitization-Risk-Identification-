hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
green_lower = np.array([40, 100, 50])
green_upper = np.array([80, 255, 255])
mask_green = cv2.inRange(hsv, green_lower, green_upper)

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([40, 255, 255])
mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

# Blue minor roads
blue_lower = np.array([90, 50, 50])
blue_upper = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

# Binary Mask Creation & Merging
mask_all = cv2.bitwise_or(mask_green, mask_yellow)
mask_all = cv2.bitwise_or(mask_all, mask_blue)

# Morphological Operations
kernel = np.ones((3, 3), np.uint8)  # Small kernel for thin lines
mask_open = cv2.morphologyEx(mask_all, cv2.MORPH_OPEN, kernel)  # Noise removal
mask_closed = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel)  # Gap filling

# Visualize
plt.imshow(mask_closed, cmap='gray')
plt.title('Extracted Roads Mask')
plt.show()

cv2.imwrite('roads_mask.png', mask_closed)  
