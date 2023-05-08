input1 = input("Enter a number: ")
input2 = input("Enter a second number: ")

try:
    print(int(input1) * int(input2))
except:
    print("One of the numbers were not a number")