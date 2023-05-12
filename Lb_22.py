A = int(input("Номер места "))
if A % 2 == 0:
    B = "Верхнее "
else:
    B = "Нижнее "
if 37 <= A <= 54:
    B = B + "боковое"
else:
    B = B + "купе"
print(B)