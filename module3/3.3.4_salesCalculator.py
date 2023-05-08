def task() -> None:
    """
    The script should request 10 sales values from the user using a loop. 
    - If the value entered by the user is less than 5000, the rest of 
    the current loop iteration shouldn't be performed. 
    - If the value is higher than 5000 and less than 10001, the user's current 
    sales total and sales average should be printed to screen. 
    - If the value is higher than 10000, the loop should stop entirely, and 
    a message should be displayed that a possible data entry error has occurred.
    """
    
    sum = 0
    for i in range(10):
        sale = int(input("Enter a sale: "))
        if sale <= 5000:
            sum += sale
            continue
        elif sale > 5000 and sale < 10001:
            sum += sale
            print(f"Total: {sum}, average sale: {sum/i}")
        else:
            print("...a possible data entry error has occurred.")
            break
    print("Ok, thats 10 entries.")


if __name__ == "__main__":
    task()