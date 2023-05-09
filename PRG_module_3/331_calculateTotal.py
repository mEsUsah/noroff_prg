def task() -> None:
    """
    The script should continuously ask a user to enter an integer value. 
    This should continue until the user has entered the value -1. 
    Once the loop has ended, print the total of all the values 
    entered by the user (excluding -1).
    """

    sum = 0
    while True:
        user_input = input("Enter an integer: ")
        if user_input.lstrip('-').isdigit():
            if int(user_input) == -1:
                break
            else:
                sum += int(user_input)
        else:
            print("ERROR: You did not enter a number...")
    

    print(f"The values you enterd total to: {sum}")


if __name__ == "__main__":
    task()