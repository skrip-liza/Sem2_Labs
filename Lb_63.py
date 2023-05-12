dict = {"Женя": ["Итальянский", "Английский"], "Денис": ["Японский", "Русский"],
        "Катя": ["Французский", "Японский", "Китайский"], "Настя": ["Японский", "Испанский", "Китайский"]
}
Mass = []
MassA = []
for i in dict.keys():
    A = list(dict[i])
    for j in range(0, len(A)):
        if "Китайский" in A[j]:
            MassA.append(i)
        if A[j] not in Mass:
            Mass.append(A[j])
Mass = sorted(Mass)
print(len(Mass))
print(*Mass)
print(*MassA)

