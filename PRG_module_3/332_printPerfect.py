def task(max_number: int) -> list:
    """
    Create a script that requests a maximum integer from the user. 
    The script should then calculate every perfect number from 1 to the maximum 
    value entered by the user. 
    
    A number is perfect if it's equal to the sum of all the smaller integers that 
    divide equally into it. 
    
    6 is a perfect number, because 1, 2 and 3 all divide equally into it and 1 + 2 + 3 = 6.
    """
    
    if max_number.isnumeric():
        max_number = int(max_number)
    else:
        return -1
    
    if max_number == 1:
        return 1
    
    i, sum, perfect_numbers = 1, 1, [1]
    while sum <= max_number:
        if sum >= max_number:
            break
        i += 1
        sum = sum + i
        perfect_numbers.append(i)

    return perfect_numbers

if __name__ == "__main__":
    perfect_numbers_list = task(input("Enter a number: "))
    print(perfect_numbers_list)