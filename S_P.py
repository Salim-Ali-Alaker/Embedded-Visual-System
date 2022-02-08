from statistics import mode
import cv2 
from matplotlib import pyplot as plt 
from skimage.util import random_noise 
from PIL import Image, ImageFilter as IF

# Img =cv2.imread('ballon.png',1)
# sp=random_noise(Img,mode="s&p")
# cv2.imshow("Image",sp)
# # cv2.imwrite('ballon_s_p.png',sp)
# cv2.waitKey(0)
# filteredImg = cv2.medianBlur(Img, ksize=5)
# cv2.imshow("Image",filteredImg)
# cv2.waitKey(0)
Img=Image.open(r"C:\Users\PAVILION 15\OneDrive\Desktop\work\ballon_s_p.png")
Img.show()
cv2.waitKey(0)
im2 = Img.filter(IF.MedianFilter(size = 3)) 
im2.show()