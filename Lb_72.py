from PIL import Image
im = Image.open('May.jpg')
im = im.reduce(3)
S = str(input("Отзеркалить "))
if "Горизонтально" in S:
    new = im.transpose(Image.FLIP_TOP_BOTTOM)
    new.show()
    new.save("May2.jpg")
if "Вертикально" in S:
    new = im.transpose(Image.FLIP_LEFT_RIGHT)
    new.show()
    new.save("May2.jpg")


