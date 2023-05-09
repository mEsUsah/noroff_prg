import moduleTwo as myModules

def task():
    '''
    In this script, you need to access the functions created in the mymodules.py script. 
    Furthermore, this script should present the user with a guessing game. 
    The user should be prompted to guess a number between 0 and 10. 
    The system should then randomly generate a number between 0 and 10 using a function 
    from mymodules.py. 
    
    If the user guessed correctly, display a congratulatory message. 
    Otherwise, display a message stating the actual number and wish them luck for their next attempt. 
    The user should be able to play the game as many times as they want. 
    
    If the user has finished playing, the system should display a message stating how many 
    seconds they played.
    '''

    start_time = myModules.create_time()
    while True:
        number = myModules.generate_random(1,10)
        guess = input("Guess a number between 1, and 10: ")
        try:
            if int(guess) == number:
                print("Congratulation, you guessed correctly!")
            else:
                print("Sorry, you guessed wrong")
        except:
            print("you did not enter a number")
        finally:
            if input("Enter 'q' to quit, or just press enter to continue: ") == 'q':
                break

    end_time = myModules.create_time()
    diff_time = myModules.calculate_difference(start_time,end_time)
    print("Thank you for playing! :D")
    print(f"You played for {diff_time.seconds} seconds")

if __name__ == '__main__':
    task()