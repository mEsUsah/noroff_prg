import os

def task():
    '''
    Create a Python script that requests a directory path from a user. 
    Display the directory and file structure of the path to the user.

    Ask the user if they wish to display the details of a specific file. 
    If they answer “y” for yes, request the name of a file and display 
    the file’s details using os.stat. If they answer “n”, end the program.
    '''
    while True:
        cwd = input('Please enter a path: ')
        try:
            os.chdir(cwd)
            break

        except:
            print('Error! You entered an invalid path')
    

    files = os.listdir(os.getcwd())
    
    files.sort()
    for file in files:
        print(file)
    

    while True:
        answer = input('Do you want to dispaly details of a spedific file? ')
        if answer.lower() == 'y':
            break
        if answer.lower() == 'n':
            exit()

    while True:
        file = input('Please enter the name of the file/dirname. ')
        
        try:
            file_path = os.path.join(cwd, file)
            print(os.stat(file_path))
            # TODO: how to dynamically loop through os.stat_result object
            break

        except:
            print('Error! You entered an invalid name')
        

if __name__ == '__main__':
    task()