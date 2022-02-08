import cv2
import numpy as np

img = cv2.imread('low_C.png')
original = img.copy()
xp = [ 50, 96]
fp = [ 0, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 