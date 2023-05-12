import random

C = 0
K = 0
massA = []
MassB = []

while C < 10:
    A = random.randrange(0, 10)
    if A in massA:
        MassB.append(A)
    massA.append(A)
    C += 1

for I in range(0,15):
    for J in range(0, len(MassB)):
        if I == MassB[J]:
            K += 1
    if K > 0:
        K += 1
        print("Число", str(I), "повторяется", str(K), "раза!")
    K = 0