def print_list(start, end):
    try:
        for i in range(start, end):
            print(i)
    except:
        print("Whooopsie, you did not pass numbers to the print_list function")

def multi(a,b):
    try:
        return a * b
    except:
        print("Whooopsie, you did not pass numbers to the multi function")