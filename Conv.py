# from statistics import mode
import cv2
# from cv2 import imread 
# from matplotlib import pyplot as plt 
# from skimage.util import random_noise 
# from PIL import Image, ImageFilter as IF
import numpy as np
image=cv2.imread('ballon.png',0)
kernel1=np.array([
 [-1, -1, -1],
  [-1, 8, -1],
  [-1, -1, -1]
])
id = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
cv2.imshow('filtered',id)
cv2.waitKey()
