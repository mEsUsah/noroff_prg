import schedule
import time
import os

def task():
    '''
    Create a script that uses task scheduling to open up a 
    text editor, such as Notepad, every day at 14:00.
    '''
    schedule.every().day.at('14:00').do(run_program)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        'closing'

def run_program():
    os.system('notepad')

if __name__ == '__main__':
    task()