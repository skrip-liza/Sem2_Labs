from PIL import Image
image = Image.open('May.jpg')
image.show()
print("Размер:", image.size)
print("Формат:", image.format)
print("Модель:", image.mode)
