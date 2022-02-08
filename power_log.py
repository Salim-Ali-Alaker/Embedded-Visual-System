import cv2
import numpy as np
image =cv2.imread('A_I.jpg')
Lam=4
P_l=255*(image/255)**Lam

P_l = np.array(P_l, dtype = 'uint8')

cv2.imshow('LOG_Tran', P_l)
cv2.waitKey()
cv2.destroyAllWindows