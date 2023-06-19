my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x > 1, my_tuple))

print(foo)