import csv

SS = 0
check = True

print("Нужно купить:")

with open("file.csv") as file:
    file = csv.reader(file)
    for i in file:
        if check:
            check = False
        else:
            j = i[0].split(";")
            T = j[0]
            K = j[1]
            P = j[2]
            S = int(P) * int(K)
            SS = SS + (int(K) * int(P))
            print(T + " - " + K + " шт. за " + str(S) + " руб.")
print("Итоговая сумма: " + str(SS) + " руб.")