import json
import csv



# file = open('family.csv', 'w+')
# csv_file = csv.writer(file)
# for i in family:
#     csv_file.writerow(i)
#
# file.close()


with open('family.json', 'r') as file:
    a = json.load(file)
    print(a)


with open('family.csv', 'w+') as file:
    writer = csv.writer(file, delimiter=" ")
    writer.writerow(('id', 'name', 'age', 'phone'))

    for key, value in a.items():
        writer.writerow([key, *value])

# with open('family.csv', 'a') as file:
#     print(a)