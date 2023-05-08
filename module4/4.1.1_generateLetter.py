def generate_letter():
    '''
    Create a function called generate_letter which is to serve as a generator function. 
    The generator should return a letter in the range a to e. 
    If the generator returns the letter e, it should return the letter a the next 
    time the generator function object is used. 
    
    Demonstrate the use of the generator in the main portion of your script by 
    display the letters a to e twice.
    '''
    letter_list = ['a','b','c','d','e']
    i = 0

    while True:
        yield letter_list[i]

        i += 1
        if i >= len(letter_list):
            i = 0


if __name__ == "__main__":
    letters = generate_letter()
    for i in range(5*2):
        print(next(letters))