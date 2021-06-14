import os
import sys
import numpy as np
import io
from PIL import Image

global str
str = open('zucky elon ascii.txt', 'r', encoding="utf-8").read()

list1 = []

for char in str:
    list1.append(ord(char))

# str1 = ""
# for item in list1:
#     item1 = "%s " % item
#     str1 += item1


# with open("sample1num.txt", "w", encoding="utf-8") as f:
#     f.write(str1)
# array = np.array(list1, dtype=np.uint8)

# # Use PIL to create an image from the new array of pixels
# new_image = Image.fromarray(array)
# new_image.save('new.png')

w, h = 200, 150
data = np.zeros((h, w, 3), dtype=np.uint8)
for i in list1:
    for j in list1:
        data[0:200,0:150,0] = [list1[i], list[j], 0] # red patch in upper left
        j = j+1
    i = i+1




img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()
