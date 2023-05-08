# /bin/env pyhton3
import datetime

correct_asnwer = 543
while True:
    user_answer = int(input("Enter a number: "))
    if user_answer == correct_asnwer:
        print(f"You guessed the number! It is {correct_asnwer}")
        break
    elif user_answer > correct_asnwer:
        print("Your number is too high")
    elif user_answer < correct_asnwer:
        print("Your number is too low")


while True:
    user_answer = int(input("Enter an hour: "))
    if user_answer >= 8 and user_answer <= 17:
        print("Inside the working hours")
        break

min_number = 0
max_number = 3

message = [
    'Coding is fun',
    'Python is not code, but a way of life',
    'We learn Python the fun way',
    'We code, because we can'
]

while True:
    user_answer = int(input(f"Enter a number between {min_number} and {max_number}: "))
    if user_answer >= min_number and user_answer <= max_number:
        print(message[user_answer])
        break