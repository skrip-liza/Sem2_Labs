from PIL import Image,ImageFilter
for i in range(1, 6):
    K = str(i) + ".jpg"
    with Image.open(K) as im:
        im_fil = im.filter(ImageFilter.SMOOTH)
        im_fil.show()
        im_fil.save("new" + str(i) +".jpg")