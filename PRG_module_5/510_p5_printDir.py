import os

def task():
    '''
    Create a Python script to display all the files in your current working directory.
    '''
    for item in os.listdir():
        print(item)


if __name__ == '__main__':
    task()