# генератор геометрической прогресии

def geom_progression(number: int, q: int, length_progression: int):
    counter = 1
    while length_progression > 0:
        if counter != 0:
            number *= q
            length_progression -= 1
            counter += 1
            yield number
        else:
            length_progression -= 1
            counter += 1
            yield number


gen_five = geom_progression(2, 3, 5)
print(next(gen_five))
print(next(gen_five))
print(next(gen_five))
print(next(gen_five))
print(next(gen_five))