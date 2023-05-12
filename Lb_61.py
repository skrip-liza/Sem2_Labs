dict1 = {"Италия": "Рим", "Япония": "Токио", "Россия": "Москва", "Корея": "Сеул", "США": "Вашингтон"}
dict2 = {}
for key, value in dict1.items():
    print(key, value)
A = str(input("Страна: "))
print(dict1[A])
B = sorted(dict1.items())
for i in range(0, len(B)):
    dict2.update({B[i][0]: B[i][1]})
for key, value in dict2.items():
    print(key, value)


