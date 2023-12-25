import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image, gamma=1.0):
    normalized_image = image / 255.0
    corrected_image = np.power(normalized_image, gamma)
    corrected_image = (corrected_image * 255).astype(np.uint8)

    return corrected_image


img = cv2.imread('./Pictures/picture3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Görüntüyü RGB formatına dönüştür

# Gamma düzeltme işlemi
gamma_value = 1.5  # İstediğiniz gamma değerini seçin
corrected_img = gamma_correction(img, gamma_value)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Orijinal Görüntü')

plt.subplot(1, 2, 2)
plt.imshow(corrected_img)
plt.title(f'Gamma Düzeltme (γ={gamma_value})')

plt.show()
