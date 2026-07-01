import cv2
import matplotlib.pyplot as plt
image = cv2.imread('computer vision\cricketbat.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("cricket equipments")
plt.show()
starting_point=(1122,564)
ending_point=(1383,773)
thickness = 4
image_annoted=cv2.rectangle(image_rgb,starting_point,ending_point,(0,0,255),thickness)
Label="cricket ball"
txt_origin=(1140,786)
font=cv2.FONT_HERSHEY_COMPLEX
font_scale=1.5
color=(255,255,255)
cv2.putText(image_annoted,Label,txt_origin,font,font_scale,color,2,cv2.LINE_AA)


start_point=(696,543)
end_point=(211,922)
thickness = 4
cv2.line(image_annoted,start_point,end_point,(0,0,255),thickness)

cv2.line(image_annoted,(211,922),(526,964),(0,0,255),thickness)

cv2.line(image_annoted,(526,964),(895,613),(0,0,255),thickness)

cv2.line(image_annoted,(895,613),(694,535),(0,0,255),thickness)

Label="cricket bat handle"
txt_origin=(344,1000)
font=cv2.FONT_HERSHEY_COMPLEX
font_scale=1.5
color=(255,255,255)
cv2.putText(image_annoted,Label,txt_origin,font,font_scale,color,2,cv2.LINE_AA)
plt.imshow(image_annoted)
plt.title("cricket equipments")
plt.show()