a = input("Введите число: ").replace(',', '.')

if a.isdigit() or a.count("-") <= 1 and a.count(".") <= 1 or a[0] == '-' and a[1:].isdigit():
    a = float(a)
    if a > 0:
        print("Положительное")
    elif a == 0:
        print("Ноль")
    elif a < 0:
        print("Отрицательное")
else:
    print("Введите число!")