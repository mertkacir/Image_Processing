import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image, window_size, Q):
    padded_image = cv2.copyMakeBorder(image, window_size // 2, window_size // 2, window_size // 2, window_size // 2, cv2.BORDER_CONSTANT, value=0)

    result_image = np.zeros_like(image, dtype=np.float32)

    for i in range(window_size // 2, padded_image.shape[0] - window_size // 2):
        for j in range(window_size // 2, padded_image.shape[1] - window_size // 2):
            window = padded_image[i - window_size // 2:i + window_size // 2 + 1, j - window_size // 2:j + window_size // 2 + 1]

            # Contraharmonic mean filtresi uygulama
            numerator = np.sum(np.power(window, Q + 1))
            denominator = np.sum(np.power(window, Q))

            if denominator != 0:
                result_image[i - window_size // 2, j - window_size // 2] = numerator / denominator
            else:
                result_image[i - window_size // 2, j - window_size // 2] = 0

    return result_image.astype(np.uint8)


img = cv2.imread('./Pictures/picture3.jpg', 0)

window_size = 3
Q = 1.5

filtered_img = contraharmonic_mean_filter(img, window_size, Q)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Orijinal Görüntü')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img, cmap='gray')
plt.title(f'Contraharmonic Mean Filtre (Window Size = {window_size}, Q = {Q})')

plt.show()
