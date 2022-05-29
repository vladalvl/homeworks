a = input("Введите строку: ").lower()

a_set = set(a)

for c in a_set:
    a.count(c)

for c in a_set:
    b = max(c)

a_len = len(str(b))

for c in a_set:
    if not c.isalpha():
        continue

    print("| {} | {:<{}} |".format(c, a.count(c), a_len))