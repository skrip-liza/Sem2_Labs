A = ""
while True:
    B = input("Слово ")
    if B == "stop":
        A = A + " " + B
    else:
        break
print(A)