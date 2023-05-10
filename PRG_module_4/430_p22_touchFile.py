import os

def task():
    '''
    Create a Python script which asks a user for a filename. 
    Once entered, ask the user if they wish to create the file or remove it. 
    
    If they choose to create the file, first test if it already exists. 
    If it does, do nothing, but if it doesn’t exist, create an empty text file 
    using the filename entered by the user. 
    
    If the user chooses to remove a file, then first test if the file exists. 
    If it exists, remove it. Otherwise, do nothing.
    '''
    filename = input("Enter a filename: ")
    
    global create_or_delete
    create_or_delete = None
    while True:
        input_text = input("Do you want to [c]reate or [d]elete the file? ")
        try:
            if input_text.lower() == "c":
                create_or_delete = 'c'
                break
            elif input_text.lower() == 'd':
                create_or_delete = 'd'
                break
        except:
            print("You entered an invalid value. Try again.")

    if create_or_delete == 'c':
        try:
            my_file = open(filename,'r')
            my_file.close()
        except:
            my_file = open(filename,'x')
            my_file.close()

    if create_or_delete == 'd':
        try:
            my_file = open(filename,'r')
            my_file.close()
            os.remove(filename)
        except:
            pass


if __name__ == '__main__':
    task()