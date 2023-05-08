my_list = ['a','b','c','d','e','f','g','h','i','j']

def my_generator():
    while True:
        if 'i' not in vars():
            i = -1
        
        i += 1
        if i >= len(my_list):
            i = 0

        yield my_list[i]

my_gen = my_generator()
for i in range(30):
    print(next(my_gen))    