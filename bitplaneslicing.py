import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image, bit_level):
    # Görüntüyü gri tonlamalı olarak yükle
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Her bir pikselin bit düzeyini belirtilen bit seviyesine göre ayır
    bit_plane = np.bitwise_and(gray_image, 2**bit_level)

    return bit_plane

# Görüntüyü yükle
image = cv2.imread('picture4.jpg')

# Bit plane slicing yap
bit_level = 2  # İstediğiniz bit seviyesini seçebilirsiniz (örneğin: 0, 1, 2, ...)
sliced_plane = bit_plane_slice(image, bit_level)

# Sonuçları göster
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orjinal Görüntü')

plt.subplot(1, 2, 2)
plt.imshow(sliced_plane, cmap='gray')
plt.title(f'Bit Plane {bit_level}')

plt.show()
