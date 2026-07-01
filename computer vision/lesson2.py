import cv2
import matplotlib.pyplot as plt
image = cv2.imread('computer vision\OIP.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.show()
cropped_image = image[100:300, 200:400]
picture_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(picture_rgb)
plt.title("RGB image")
plt.show()
