import cv2 

image =cv2.imread('Ains.png')

cv2.imshow('original', image)
cv2.waitKey()

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite('New.png',gray_image)

cv2.imshow('new',gray_image)

cv2.waitKey(0)
# cv2.destroyAllWindows()

