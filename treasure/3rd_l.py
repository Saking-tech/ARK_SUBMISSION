from PIL import Image
import numpy as np

w, h = 200, 150
data = np.zeros((h, w, 3), dtype=np.uint8)

data[0:256, 0:256] = [255, 255, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()