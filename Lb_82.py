from PIL import Image

dict = {"пасха": "HS.jpg", "день рождения": "DR.jpg", "новый год": "NG.jpg"
}

A = str(input("Введите праздник: ")).lower()
img = Image.open(dict[A])
img.show()


