import numpy as np
from PIL import Image

array = np.full((1024,720),383,np.uint8)
# array = np.reshape(array, (1024, 720))

im = Image.fromarray(array)
im.save("filename.jpeg")