import os

def task():
    '''
    Create a Python script that changes the current working directory 
    using os.path.join() to ensure the script works on multiple platforms.

    NB: The script should be ran from the repo root.
    '''

    pwd  = os.getcwd()
    next_dir = os.path.join(pwd, 'README.md')
    print(next_dir)


if __name__ == '__main__':
    task()