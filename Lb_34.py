import random
F = 0
E = 0

while True:
    A = str(random.randrange(1, 10))
    B = str(random.randrange(1, 10))

    C = int(A) + int(B)
    D = input(A + " + " + B + " = ")

    if int(C) == int(D):
        F += 1
    else:
        E += 1

    if E == 3:
        print("Конец! Ответов", str(F))
        break