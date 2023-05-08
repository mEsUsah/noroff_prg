def assignment():
    '''
    Create a section of code that requests sales numbers from a user. 
    The user should be able to enter as many sales values as they choose to. 
    All sales values should always be entered as float values. 
    Each value entered should be added to a list of sales values.

    Provide a means for the user to stop entering sales values. 
    Once all the sales values have been entered, the user wants to calculate 
    the total of the sales figures. 
    
    Still, the user should be allowed to specify how many sales figures should 
    be added to the total, i.e. if the user requests that five sales figures 
    be added to the total, the program should sum the first five values in the list. 
    
    There are multiple places in this program where errors may occur. 
    Ensure that any exceptions that occur are handled.
    '''
    total_sales = 0.0

    while True:
        input_value = input("Enter a sale: ")
        
        try:
            if input_value.lower() =="q":
                break
        except:
            pass

        try:
            total_sales += float(input_value)
        except:
            print("Whoopsie! You did not enter a number. Enter 'q' to quit.")
    
    print(total_sales)


if __name__ == '__main__':
    assignment()