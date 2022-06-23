a = input("Введите строку: ").lower()

a_set = set(a)
max_len = 0

for c in a_set:
    if a.count(c) > max_len:
        max_len = a.count(c)

a_len = len(str(max_len))

for c in a_set:
    if not c.isalpha():
        continue

    print("| {} | {:<{}} |".format(c, a.count(c), a_len))