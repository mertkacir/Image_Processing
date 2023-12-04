import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('face.png')

original = image.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')

img = cv2.LUT(image, table)

hist_original = cv2.calcHist([original], [0], None, [256], [0, 256])
hist_stretched = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.title('Original Image Histogram')
plt.plot(hist_original)
plt.xlim([0, 256])

plt.subplot(122)
plt.title('Stretched Image Histogram')
plt.plot(hist_stretched)
plt.xlim([0, 256])
plt.show()
cv2.imshow("original", original)
cv2.imshow("Output", img)

cv2.waitKey(0)
cv2.destroyAllWindows()



