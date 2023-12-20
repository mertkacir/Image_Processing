import cv2
import numpy as np
import matplotlib.pyplot as plt

def split_rgb(image, channel):
    # Renkli (RGB) görüntüyü yükle
    b, g, r = cv2.split(image)

    # Belirli renk bileşenine göre bölütlenmiş görüntüyü oluştur
    if channel == 'red':
        split_image = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
    elif channel == 'green':
        split_image = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
    elif channel == 'blue':
        split_image = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])
    else:
        raise ValueError("Geçersiz renk kanalı. 'red', 'green' veya 'blue' kullanın.")

    return split_image

# Görüntüyü yükle
image = cv2.imread('picture2.jpg')

# Belirli renk bileşenine göre bölütlenmiş görüntüyü al
color_channel = 'red'  # 'red', 'green', veya 'blue' seçebilirsiniz
split_image = split_rgb(image, color_channel)

# Sonuçları göster
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Görüntü')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(split_image, cv2.COLOR_BGR2RGB))
plt.title(f'{color_channel.capitalize()} Bileşenine Göre Bölütlenmiş Görüntü')

plt.show()
