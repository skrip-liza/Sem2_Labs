def b():
    n = 0
    try:
        n = float(input("Число "))
        if n == 0:
            print("ZeroDivisionError")
        else:
            n = n / 100
            print(n)
    except ValueError:
        print("ValueError")
b()