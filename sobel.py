import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_sobel_filter(image, sobel_kernel_size=3):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Sobel filtresi uygulama
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=sobel_kernel_size)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=sobel_kernel_size)

    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    gradient_angle = np.arctan2(np.abs(sobely), np.abs(sobelx))

    return gradient_magnitude, gradient_angle

img = cv2.imread('./Pictures/picture1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Sobel filtresi uygulama
sobel_magnitude, sobel_angle = apply_sobel_filter(img)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')

plt.subplot(1, 3, 2)
plt.imshow(sobel_magnitude, cmap='gray')
plt.title('Sobel Filtre - Magnitüd')

plt.subplot(1, 3, 3)
plt.imshow(sobel_angle, cmap='gray')
plt.title('Sobel Filtre - Açı')

plt.show()
