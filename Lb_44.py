def d():
    S1 = 0
    S2 = 0
    c = 0
    while True:
        T = str(input("Билет "))
        if len(T) % 2 == 0:
            print("Не счастливый")
            break
        TL = int(len(T)/2)
        TL1 = T[:TL]
        TL2 = T[TL:]
        M1 = list(TL1)
        M2 = list(TL2)
        while len(M1) > c:
            S1 += int(M1[c])
            S2 += int(M2[c])
            c += 1
        if S1 == S2:
            print("Счастливый")
            break
        else:
            print("Не счастливый")
d()

