tuple1 = ('hello', 'fddf', 'bbbbnnnn', 'world', "werttrew", "Dad")

tuple1 = tuple(map(str.lower, tuple1))
new_tuple = tuple(filter(lambda elem: elem == elem[::-1], tuple1))
print(new_tuple)
