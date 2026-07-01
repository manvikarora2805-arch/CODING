import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('computer vision\OIP.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
(h,w)=image.shape[:2]
centre=(w//2,h//2)
m=cv2.getRotationMatrix2D(centre,45,1)
r=cv2.warpAffine(image,m,(w,h))
r_rgb = cv2.cvtColor(r, cv2.COLOR_BGR2RGB)
plt.imshow(r_rgb)
plt.title("RGB image")
plt.show()
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()