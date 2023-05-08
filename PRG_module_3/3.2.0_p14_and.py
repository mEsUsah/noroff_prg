value1 = int(input('enter a value: '))
value2 = int(input('enter a value: '))

if value1 and value2:
    print(1)
elif value1 and not value2:
    print(0)
elif not value1 and value2:
    print(0)