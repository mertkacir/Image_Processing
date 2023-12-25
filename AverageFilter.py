import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_filter(image, kernel_size):
    # Ortalama filtresi çekirdeği oluştur
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    # Filtreleme işlemi
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

img = cv2.imread('./Pictures/picture1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Görüntüyü RGB formatına dönüştür

# Ortalama filtresi uygulama
kernel_size = 5  # Filtre çekirdeği boyutu
filtered_img = average_filter(img, kernel_size)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img)
plt.title(f'Ortalama Filtre (Kernel Size = {kernel_size})')

plt.show()
