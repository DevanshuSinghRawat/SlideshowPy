import os
import numpy as np
import cv2

base_path=R"""Users\Slideshow\Sources"""
img_names=os.listdir(base_path)
for img_name in img_names:
    path=base_path + "\\" + img_name
    img=cv2.imread(path)
    # img=cv2.resize(img_name,(1280,720))
    img=cv2.resize(img,(400,400))
    cv2.imshow("Image",img)
    if cv2.waitKey(1000) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
