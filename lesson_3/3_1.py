a = input("Введите число: ").replace(',', '.')


if a.count("." and "-") > 1:
    print("Попробуй еще раз!")
else:
    if '-' or '' in a[0]:
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
        print("Необходимо ввести число!")

# Через try/except

# b = input("Введите число: ").replace(',', '.')
#
#
# try:
#
#     b = float(b)
#     if b > 0:
#         print("Положительное")
#     elif b == 0:
#         print("Ноль")
#     elif b < 0:
#         print("Отрицательное")
#     else:
#         print("Введите число!")
#
# except ValueError:
#     print("Попробуйте еще раз!")