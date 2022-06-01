import json


family = {
    '123456': ('david', 35),
    '345678': ('kate', 28),
    '876543': ('bob', 78),
    '765309': ('emma', 45),
    '326784': ('ava', 18),
    '657189': ('mia', 78)
}

with open('family.json', 'w') as file:
    json.dump(family, file)




# file = open('family.json')
# family = json.load(file)
# file.close()

