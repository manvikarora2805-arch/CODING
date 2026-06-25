import cv2
image = cv2.imread('computer vision\OIP.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey scale', gray_image)
key=cv2.waitKey(0)
if key==ord("s"):
    cv2.imwrite("computer vision\OIP2.jpg", gray_image)
    print("image saved")
else:
    print("image not saved")
cv2.destroyAllWindows()