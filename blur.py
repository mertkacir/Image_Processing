import cv2

image = cv2.imread("face.png")
kernel_size = (10,10)

blurred_image = cv2.blur(image,kernel_size)
#Ancak cv2.boxFilter işlevi, farklı çekirdekler kullanarak
#özelleştirilmiş bulanıklaştırma işlemleri yapmak için daha fazla esneklik sunar.Ayrıca daha hızlı
box_filtered_image = cv2.boxFilter(image,-1,kernel_size)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Also Blurred Image", box_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()