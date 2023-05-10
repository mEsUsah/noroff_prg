def task():
    '''
    Write a Python script that opens a text file, reads its contents, and displays 
    it to the command-line. 
    
    After displaying the contents, the script should request values from a user 
    continuously until they choose to stop. 
    
    All values entered should be appended to the same text file of which the contents 
    were displayed at the start of the script’s execution. 
    
    Ensure that you run the script multiple times to see how the number of values 
    in the file increases.
    '''
    file_path = 'PRG_module_4/myfileOne.txt'

    my_file = open(file_path,'r')
    file_content =  my_file.readlines()
    for line in file_content:
        print(line, end='')

    my_file.close()

    my_file = open(file_path,'a')
    print("#"*120)
    print("Write, and press enter to add new text. to quit, write 'q'")
    print("#"*120)
    while True:
        line = input()
        if line == "q":
            break
        my_file.write(f'{line}\n')

    my_file.close()

if __name__ == '__main__':
    task()

