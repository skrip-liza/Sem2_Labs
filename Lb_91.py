import os
from PIL import Image,ImageFilter

os.mkdir("Picture")

for i in os.listdir("Pictures"):
    im = Image.open(str(i))
    new_im = im.filter(ImageFilter.SMOOTH)
    new_im.show()
    #new_im.save(r"C:\Users\159950\PycharmProjects\Labs_8-12\Picture\img" + str(i) +".jpg")