from zipfile import ZipFile
import os

def task():
    '''
    Write a script that requests the name of the zip file. 
    If the file doesn’t exist, create it.

    Next, request a series of filenames (paths) from a user. 
    Users should be able to add as many as they wish. 
    The files specified by the user should then be added to the specified zip file.

    Use error handling to ensure that the program asks the user for another 
    file name if an error occurs.
    '''
    while True:
        filename = input("enter a '.zip' filename: ")
        
        if filename.split(".")[-1] == 'zip':
            break
        else:
            print("Error! Invalid filename")
    
    with ZipFile(filename, 'w') as zipfile:
        while True:
            addFile = input('Enter a filename to add (q to quit): ')
            if (addFile.lower() == 'q'):
                break
            try:
                zipfile.write(addFile)
            except:
                print('Error! Invalid filename')


    pass

if __name__ == '__main__':
    task()