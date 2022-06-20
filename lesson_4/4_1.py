a = input("Введите число: ").replace(',', '.')


def my_fun(n: str):

    if n.isdigit() or n.count("-") <= 1 and n.count(".") <= 1 or n[0] == '-' and n[1:].isdigit():
        n = float(n)
        if n > 0:
            print("Положительное")
        elif n == 0:
            print("Ноль")
        elif n < 0:
            print("Отрицательное")
    else:
        print("Введите число!")


print(my_fun(a))