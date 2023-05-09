from time import *

def activity():
    '''
    Write a script that displays a paragraph of text to the user (any paragraph of text).

    Make use of a timer to record how long it takes a user to retype the paragraph. 
    To start the timer, ask the user to press Enter.

    Also, inform the user that the timer will stop once they press Enter again at 
    the end of the paragraph. 
    
    Display in seconds how long it took the user to retype the paragraph.
    '''

    print("Moby-Dick; or, The Whale is an 1851 novel by American writer Herman Melville.")
    input("Press enter to start timer, and start typing: ")
    start_time = time()
    input("")
    end_time = time()

    time_string = "%.2f" % (end_time - start_time)
    print(f"You typed for {time_string} seconds")


if __name__ == "__main__":
    activity()