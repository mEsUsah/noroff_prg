def summing_machine() -> None:
    """Sum every number the user inputs until they enter 's'."""
    total = 0
    while True:
        user_input = input("Enter a number to add or 's' to se sum: ")
        if user_input == 's':
            break

        if user_input.isdigit():
            total += int(user_input)
        else:
            print("Not a valid number, try again.")

    print(f"The total sum is: {total}")


if __name__ == "__main__":
    summing_machine()