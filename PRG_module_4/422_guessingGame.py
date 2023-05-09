import moduleTwo as myModules

if __name__ == '__main__':
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