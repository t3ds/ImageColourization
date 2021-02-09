from PIL import Image
import os
from os.path import isfile

path = "G:\\Datasets\\COCO val2017\\val2017"
destination = "G:\\Datasets\\COCO val2017\\val2017_processed\\"
size = (256,256)

imgs = []
for root, dirs, files in os.walk(path, topdown=True):
    for file in files:
        #print(dirs)
        imgs.append(root + '/' + file)

print(len(imgs))
os.makedirs(os.path.dirname(destination), exist_ok=True)
for i in range(len(imgs)):
    #assert isfile(img[i])
    if os.path.exists(destination + str(i)):
        continue
    img  = Image.open(imgs[i])
    img = img.resize(size, resample = Image.HAMMING)
    img.save(destination + str(i) + '.jpg', 'JPEG')
