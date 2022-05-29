number = int(input("Введите число: "))
new_number = lambda num: print("чётное") if num % 2 == 0 else print("нечётное")
new_number(number)
