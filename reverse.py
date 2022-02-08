import cv2
image =cv2.imread('skaleten.png')

imagem = cv2.bitwise_not(image)

cv2.imshow('original', imagem)
cv2.waitKey()