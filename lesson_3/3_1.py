a = input("Введите число: ")

if a.isdigit() or a[0] == '-' and a[1:].isdigit():
    a = int(a)
    if a > 0:
        print("Положительное")
    elif a == 0:
        print("Ноль")
    elif a < 0:
        print("Отрицательное")
else:
    print("Введите число!")