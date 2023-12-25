import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_median_filter(image, kernel_size):
    smoothed_image = cv2.medianBlur(image, kernel_size)
    return smoothed_image

def apply_laplace_sharpening(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sharpened_image = image - laplacian
    return sharpened_image

img = cv2.imread('./Pictures/picture1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel_size = 5
smoothed_img = apply_median_filter(img, kernel_size)

sharpened_img = apply_laplace_sharpening(img)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')

plt.subplot(1, 3, 2)
plt.imshow(smoothed_img)
plt.title(f'Median Filtre (Kernel Size = {kernel_size})')

plt.subplot(1, 3, 3)
plt.imshow(sharpened_img, cmap='gray')
plt.title('Laplace Keskinleştirme')

plt.show()
