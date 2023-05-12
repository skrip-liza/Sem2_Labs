dict = {"1": ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], "2": ["Д", "К", "Л", "М", "П", "У"],
        "3": ["Б", "Г", "Ё", "Ь", "Я"], "4": ["Й", "Ы"], "5": ["Ж", "З", "Х", "Ц", "Ч"],
        "8": ["Ш", "Э", "Ю"], "10": ["Ф", "Щ", "Ъ"]}
A = 0
B = str(input("Введите слово: ")).upper()
Mass = list(B)
for i in range(0, len(Mass)):
    for j in dict.keys():
        MassA = dict[j]
        if str(Mass[i]) in MassA:
            A = A + int(j)
            break
print(A)


