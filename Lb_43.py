def c():
    D = input("Дата ")
    S = D.split(".")
    A = int(S[0])
    B = int(S[1])
    C = int(S[2][2:])
    if A * B == C:
        print(True)
    else:
        print(False)
c()

