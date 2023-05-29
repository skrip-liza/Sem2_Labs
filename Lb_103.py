Rus_Eng = {}
S_Rus_Eng = {}

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for i in file:
        p = i.strip().split('-')
        Eng = p[0].strip()
        Rus = p[1].strip()
        Rus_Eng[Rus] = Eng
    Sort = sorted(Rus_Eng.items())
    for i in Sort:
        S_Rus_Eng[i[0]] = i[1]
with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for A, B in S_Rus_Eng.items():
        file.write(f"{A} - {B}\n")