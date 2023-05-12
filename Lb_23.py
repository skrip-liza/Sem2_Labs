A = int(input("Год "))
if (A % 4 == 0 and A % 100 != 0) or (A % 4 == 0 and A % 400 == 0):
    print(A, "високосный")
else:
    print("Не високосный")