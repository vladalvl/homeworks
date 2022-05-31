str_1 = input("Введите строку №1: ")
str_2 = input("Введите строку №2: ")
str_3 = input("Введите строку №3: ")
str_4 = input("Введите строку №4: ")

with open('file.txt', 'w+') as f:
    f.write(str_1 + '\n')
    f.write(str_2 + '\n')


with open('file.txt', 'a+') as f:
     f.write(str_3 + '\n')
     f.write(str_4 + '\n')


