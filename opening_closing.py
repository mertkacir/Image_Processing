import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening_closing(image_path, operation_type):
    # Görüntüyü yükle
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Morfolojik kernel'i tanımla
    kernel = np.ones((5, 5), np.uint8)

    if operation_type == 'opening':
        # Açma işlemi (erosion + dilation)
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        title = 'Açma İşlemi'
    elif operation_type == 'closing':
        # Kapanma işlemi (dilation + erosion)
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        title = 'Kapanma İşlemi'
    else:
        raise ValueError("Geçersiz işlem tipi. 'opening' veya 'closing' kullanın.")

    # Sonuçları göster
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü')

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title(title)

    plt.show()

# Örnek olarak bir resim dosyası kullanabilirsiniz
image_path = 'picture3.jpg'

# Açma işlemi
opening_closing(image_path, 'opening')

# Kapanma işlemi
opening_closing(image_path, 'closing')
