from PIL import Image
from numpy import asarray
# load the image
image = Image.open('New1.png')
# convert image to numpy array
data = asarray(image)
# print(type(data))

# # summarize shape
# print(data.shape)
print (data)

# create Pillow image
# image2 = Image.fromarray(data)
# print(type(image2))
