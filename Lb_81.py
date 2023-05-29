from PIL import Image

img = Image.open('HS.jpg')

img_crop = img.crop((10,30,400,135))
img_crop.show()
#3img_crop.save('otkrytka_crop.jpg')



