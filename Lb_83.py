from PIL import Image,ImageDraw,ImageFont

Name = str(input("Введите имя: "))
Title = Name + ", Поздравляю!"

image = Image.open('DR.jpg')
draw = ImageDraw.Draw(image)

T = int(input("Вариант вставки: "))
if T == 1:
    font = ImageFont.truetype( "ComicSansMS3.ttf", 50)
    draw.text((200, 30), Title, (0, 0, 0), font=font)
    image.show()
    #img.save('otkrytka_title1.png')
if T == 2:
    font = ImageFont.truetype("comicz.ttf", 60)
    draw.text((100, 500), Title, (0, 0, 0), font=font)
    image.show()
    #img.save('otkrytka_title2.png')