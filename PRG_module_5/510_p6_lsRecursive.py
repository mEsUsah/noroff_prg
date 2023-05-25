import os

def list_directory_tree(path):
    '''
    Create a Python script to display all the files in your current working 
    directory using recursion.
    '''
    
    print(path)

    for current_path, subdirectories, files in os.walk(path):
        files.sort()
        for file in files:
            print(os.path.join(current_path, file))

        subdirectories.sort()
        for directory in subdirectories:
            next_dir = os.path.join(current_path, directory)
            list_directory_tree(next_dir)


if __name__ == '__main__':
    list_directory_tree(os.getcwd())