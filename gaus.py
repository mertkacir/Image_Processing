import cv2
import numpy as np

image = cv2.imread("face.png")

blurred_image = cv2.GaussianBlur(image,(5,5),0)

laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image (Gaussian Filter)", blurred_image)
cv2.imshow("Laplacian Image", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
