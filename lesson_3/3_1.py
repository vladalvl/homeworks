a = input("Введите число: ").replace(',', '.')


if a.count('-') <= 1 and a[0] == '-' and a.count('.') <= 1:
    if a.replace('.', '').replace('-', '').isdigit():
        a = float(a)
        if a > 0:
            print("Положительное")
        elif a == 0:
            print("Ноль")
        elif a < 0:
            print("Отрицательное")
    else:
        print("Введите число!")
else:
    print("Попробуй еще раз!")
