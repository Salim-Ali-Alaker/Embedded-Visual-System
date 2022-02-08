import cv2
import numpy as np
image =cv2.imread('New.png')

# c=255/np.log(1+255)
# # print(c)
c=60
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype = np.uint8)

cv2.imshow('LOG_Tran', log_image)
cv2.waitKey()

# Inv_log= np.exp(image**1/c)-1
# Inv_log= np.array(Inv_log, dtype = np.uint8)

# cv2.imshow('inv_original', Inv_log)
# cv2.waitKey()