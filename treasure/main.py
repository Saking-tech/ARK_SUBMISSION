import os, sys, numpy as np, io
from PIL import Image
photo = Image.open('treasure_mp3.png') #your image
photo = photo.convert('RGB')
arr = []
width = photo.size[0]
height = photo.size[1]
def listToString(s): 
    str1 = ""   
    for ele in s: 
        str1 += ele 
    return str1

for y in range(0, height): #each pixel has coordinates
    row = ""
    for x in range(0, width):

        RGB = photo.getpixel((x,y))
        R,G,B = RGB  #now you can use the RGB value
        a=chr(R)
        b=chr(G)
        c=chr(B)
        if 97<=ord(a)<123 or ord(a)==32 or 0<ord(a)<4:
            arr.append(a)

# print(listToString(arr))
# text_file = open("sample.txt", "w")
# n = text_file.write(listToString(arr))
# text_file.close()
with open("audio.txt", "w", encoding="utf-8") as f:
    f.write(listToString(arr))