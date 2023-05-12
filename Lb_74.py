from PIL import Image
im = Image.open('Picture1.jpg')
im2 = Image.open('Picture2.jpg')
im2 = im2.resize((im2.width // 5, im2.height // 5))
im.paste(im2)
im.show()
im.save("Picture3.jpg")