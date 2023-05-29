from tkinter import *

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, flavors, location, open):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
        self.location = location
        self.open = open

    def describe_rest(self):
        print(
            f'Название ресторана: {self.restaurant_name}, Кухня: {self.cuisine_type}\nРасположение ресторана: {self.location}, Часы работы ресторана {self.open} ')

    def flavors(self):
        print('Вкусы мороженного:', B)


B = ['Шоколадное', 'Банановое', 'Фисташковое', 'Ванильное', 'С орехами']

a = Restaurant('ICE&CREAM', 'Французская', B, 'ул. Цветочная 15 ', '10:00 - 22:00')

a.describe_rest()

root = Tk()
root.geometry('300x300')
root.title("Виды мороженного")

frame = Frame(root, bg = 'pink')
frame.place(relx=0.1, rely = 0, relwidth = 0.8, relheight = 0.9)
title = Label(root, text = 'Виды мороженного:', bg = 'pink', font = 50)
title.place(relx=0.15, rely = -0.25, relwidth = 0.7, relheight = 0.7)

C = 0.1
for i in B:
    text = i
    C += 0.10
    a = Label(root, text = text, bg = 'pink', font = 25)
    a.place(relx=0.15, rely = C , relwidth = 0.7, relheight = 0.1)

root.mainloop()