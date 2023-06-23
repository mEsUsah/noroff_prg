try:
    f = open("myfile.txt")
    print(1, end=" ")
    s = f.readline()
    print(2, end=" ")
except IOError as e:
    print(3, end=" ")
else:
    print(4, end=" ")