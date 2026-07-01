import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('computer vision\cricketbat.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("gray image")
plt.show()

sobel_x = cv2.Sobel(src=gray_image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)

sobel_y = cv2.Sobel(src=gray_image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)

abs_sobel_x = cv2.convertScaleAbs(sobel_x)

abs_sobel_y = cv2.convertScaleAbs(sobel_y)

combined_sobel = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

plt.imshow(combined_sobel, cmap="gray")

plt.title("Sobel Edge Detection")

plt.show()

edges=cv2.Canny(image=gray_image, threshold1=255 ,threshold2=255)

plt.imshow(edges, cmap="gray")

plt.title("Canny Edge Detection")

plt.show()

cleaned_image=cv2.medianBlur(src=image_rgb, ksize=25)

plt.imshow(cleaned_image)

plt.title("Median filter")

plt.show()