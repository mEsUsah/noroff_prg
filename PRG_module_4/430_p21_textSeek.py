def task():
    '''
    Use a text editor to create a text file consisting of multiple lines of text. 
    Create a script that demonstrates how the Python seek() method can be used to 
    modify the contents of the file.
    '''
    my_file = open('PRG_module_4/myfileTwo.txt','r+')
    my_file.seek(10)
    my_file.write("CHANGED!")

if __name__ == '__main__':
    task()
