import schedule
import time
import os

#### Important note! ####
# Create the following files in the directory you run the script:
# - test.txt

def read_file():

    my_file = open('test.txt','r')
    file_content =  my_file.readlines()
    for line in file_content:
        print(line, end='')
    
    print()
    my_file.close()


def open_webpage():
    os.system("start chrome http://www.noroff.no")


if __name__ == '__main__':
    # Schedule a task that will execute every Monday to Friday at 08:00 in the morning. 
    # This task should read the contents of the text file and display the text 
    # to the command line.
    schedule.every().monday.at('08:00').do(read_file)
    schedule.every().tuesday.at('08:00').do(read_file)
    schedule.every().wednesday.at('08:00').do(read_file)
    schedule.every().tuesday.at('08:00').do(read_file)
    schedule.every().friday.at('08:00').do(read_file)
    
    # Schedule a task that will open a web browser every hour and point it to 
    # the address http://www.noroff.no.
    schedule.every(1).hours.do(open_webpage)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        print("Progam exited by user. Goodbye!")
        
