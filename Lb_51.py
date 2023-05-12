import random

C = 0
Mass = []

while C < 5:
    B = random.randrange(0, 9)
    Mass.append(B)
    C += 1

N = int(input("Введите число: "))

if N in Mass:
    print("Вы угадали число!")
else:
    print("Вы не угадали число!")